# users.forms.py
from allauth.account.forms import *
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User
class MyLoginForm(forms.Form):
    """
        Custom ALL AUTH LOGIN form.
    """
    password = PasswordField(label=("Password"), autocomplete="current-password")
    remember = forms.BooleanField(label=("Remember Me"), required=False)
    user = None

    error_messages = {
        "account_inactive": ("This account is currently inactive."),
        "email_password_mismatch": (
            "The e-mail address and/or password you specified are not correct."
        ),
        "username_password_mismatch": (
            "The username and/or password you specified are not correct."
        ),
    }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(MyLoginForm, self).__init__(*args, **kwargs)
        if app_settings.AUTHENTICATION_METHOD == AuthenticationMethod.EMAIL:
            login_widget = forms.TextInput(
                attrs={
                    "type": "email",
                    "placeholder": (""),
                    "autocomplete": "email",
                }
            )
            login_field = forms.EmailField(label=("E-mail"), widget=login_widget)
        elif app_settings.AUTHENTICATION_METHOD == AuthenticationMethod.USERNAME:
            login_widget = forms.TextInput(
                attrs={"placeholder": ("Username"), "autocomplete": "username"}
            )
            login_field = forms.CharField(
                label=_("Username"),
                widget=login_widget,
                max_length=get_username_max_length(),
            )
        else:
            assert (
                app_settings.AUTHENTICATION_METHOD
                == AuthenticationMethod.USERNAME_EMAIL
            )
            login_widget = forms.TextInput(
                attrs={"placeholder": ("Username or e-mail"), "autocomplete": "email"}
            )
            login_field = forms.CharField(
                label=pgettext("field label", "Login"), widget=login_widget
            )
        self.fields["login"] = login_field
        set_form_field_order(self, ["login", "password", "remember"])
        if app_settings.SESSION_REMEMBER is not None:
            del self.fields["remember"]

    def user_credentials(self):
        """
        Provides the credentials required to authenticate the user for
        login.
        """
        credentials = {}
        login = self.cleaned_data["login"]
        if app_settings.AUTHENTICATION_METHOD == AuthenticationMethod.EMAIL:
            credentials["email"] = login
        elif app_settings.AUTHENTICATION_METHOD == AuthenticationMethod.USERNAME:
            credentials["username"] = login
        else:
            if self._is_login_email(login):
                credentials["email"] = login
            credentials["username"] = login
        credentials["password"] = self.cleaned_data["password"]
        return credentials

    def clean_login(self):
        login = self.cleaned_data["login"]
        return login.strip()

    def _is_login_email(self, login):
        try:
            validators.validate_email(login)
            ret = True
        except exceptions.ValidationError:
            ret = False
        return ret

    def clean(self):
        super(MyLoginForm, self).clean()
        if self._errors:
            return
        credentials = self.user_credentials()
        user = get_adapter(self.request).authenticate(self.request, **credentials)
        if user:
            self.user = user
        else:
            auth_method = app_settings.AUTHENTICATION_METHOD
            if auth_method == app_settings.AuthenticationMethod.USERNAME_EMAIL:
                login = self.cleaned_data["login"]
                if self._is_login_email(login):
                    auth_method = app_settings.AuthenticationMethod.EMAIL
                else:
                    auth_method = app_settings.AuthenticationMethod.USERNAME
            raise forms.ValidationError(
                self.error_messages["%s_password_mismatch" % auth_method]
            )
        return self.cleaned_data

    def login(self, request, redirect_url=None):
        email = self.user_credentials().get("email")
        ret = perform_login(
            request,
            self.user,
            email_verification=app_settings.EMAIL_VERIFICATION,
            redirect_url=redirect_url,
            email=email,
        )
        remember = app_settings.SESSION_REMEMBER
        if remember is None:
            remember = self.cleaned_data["remember"]
        if remember:
            request.session.set_expiry(app_settings.SESSION_COOKIE_AGE)
        else:
            request.session.set_expiry(0)
        return ret


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email','full_name','date_of_birth', 'address1', 'address2', 'zip_code', 'city', 'country', 'mobile_phone', 'additional_information', 'photo','cpf',)
        widgets = {'date_of_birth': forms.DateInput(attrs={'type':'date'})}
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('full_name', 'email', 'password', 'active', 'admin','date_of_birth', 'address1', 'address2',
        'zip_code', 'city', 'country', 'mobile_phone', 'additional_information', 'photo','cpf',)
        widgets = {'date_of_birth': forms.DateInput(attrs={'type':'date'})}
    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class UserEditForms(forms.ModelForm):
    class Meta: 
        model = User 
        fields = (
            'full_name' , 'active' ,'cpf',
            'date_of_birth','address1','address2',
            'zip_code', 'city','country',
            'mobile_phone','additional_information','photo',
            'email'
        ) 

# full_name
# active
# cpf
# date_of_birth
# address1
# address2
# zip_code
# city
# country
# phone_regex
# mobile_phone
# additional_information
# photo