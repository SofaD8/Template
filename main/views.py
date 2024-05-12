from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import ContactForm
from .models import Services, Portfolio, About, Team, Contact


# Create your views here.
class IndexView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services = Services.objects.filter(is_visible=True)
        portfolio = Portfolio.objects.filter(is_visible=True)
        about = About.objects.filter(is_visible=True)
        team = Team.objects.filter(is_visible=True)
        contact = ContactForm()

        context['title_services'] = 'Services'
        context['services_dscr'] = 'Lorem ipsum dolor sit amet consectetur'
        context['title_portfolio'] = 'Portfolio'
        context['portfolio_dscr'] = 'Lorem ipsum dolor sit amet consectetur.'
        context['title_about'] = 'About'
        context['about_dscr'] = 'Lorem ipsum dolor sit amet consectetur.'
        context['services'] = services
        context['portfolio'] = portfolio
        context['about'] = about
        context['team'] = team
        context['contact'] = contact

        return context

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('main:index')




