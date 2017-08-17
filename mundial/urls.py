from django.conf.urls import url

from . import views
from mundial.views import    Bienvenida, LoginView, LogoutView, ControlPanelView


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', LoginView.as_view(), name='Login'),
    url(r'^logout/$', LogoutView.as_view(), name ='Logout'),
    url(r'^login/Bienvenida/$', views.Bienvenida, name = 'Bienvenida')
    
   ]



