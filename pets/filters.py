import django_filters
from django_filters import DateFilter
from .models import Pet

class PetFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='iexact')
    start_date = DateFilter(field_name = "age", lookup_expr='gte') #greater or equal to
    end_date = DateFilter(field_name = "age", lookup_expr='lte')   #less or equal to
    class Meta:
        model = Pet
        fields = ['age',
                    'pet_type','breed','size', 'sex' ,'vaccinated',
                    'castrated','dewormed','vulnerable', ]
        exclude = ['age']
