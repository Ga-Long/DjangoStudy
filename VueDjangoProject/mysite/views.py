from django.views.generic import TemplateView

class HomeView(TemplateView): #HomeView에서 사용하는 template은 home.html
    template_name = 'home.html'