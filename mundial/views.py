# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

from django.http import HttpResponse
from django.views.generic import FormView , TemplateView, RedirectView
# Authentication imports

from django.contrib.auth.forms import AuthenticationForm

from django.core.urlresolvers import reverse_lazy

from django.http import HttpResponseRedirect



def index(request):
    return HttpResponse ('Index del Prode')

def Bienvenida(request):
    response = "Bienvenida"
    return HttpResponse (response)




class LoginView(FormView):
    template_name = 'mundial/login.html'
    form_class = AuthenticationForm
    success_url= reverse_lazy(Bienvenida)
    
    def dispatch (self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect (self.get_success_url())
        else: 
            return super(LoginView, self).dispatch(request, *args, **kwargs)
            
    def form_valid (self, form):
        
        '''
        Esta linea comentada estaba pero si la dejo no me manda a la url que yo quiero
        '''
    
        #login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    pattern_name = 'Login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)



class LoginRequiredMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('Login'))
        else:
            return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class ControlPanelView(LoginRequiredMixin, TemplateView):
    template_name = 'mundial/login.html'

    def get_context_data(self, **kwargs):
        context = super(ControlPanelView, self).get_context_data(**kwargs)
         
        return context