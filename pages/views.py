from django.shortcuts import render

def aboutUs(request):
    return render(request, 'pages/about_us.html' )

def infos(request):
    return render(request, 'pages/informations.html')

def HomeView(TemplateView):
    return render(TemplateView, "pages/index.html")
