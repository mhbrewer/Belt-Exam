##### Belt Exam - Login App
##### Mason Brewer
##### November 19th, 2018

from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.loginReg),
    url(r'^login$', views.loginReg),
    url(r'^login/process$', views.processLogin),
    url(r'^reg/process$', views.processReg),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout)
]