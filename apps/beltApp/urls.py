##### Belt Exam - Belt App
##### Mason Brewer
##### November 19th, 2018

from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.home),
    url(r'^home$', views.home),
    url(r'^dashboard$', views.home),
    url(r'^job/new$', views.newJobPage),
    url(r'^job/new/process$', views.newJobProcess),
    url(r'^job/edit$', views.editJobPage),
    url(r'^job/edit/process$', views.editJobProcess),
    url(r'^job/delete$', views.jobDelete),
    url(r'^job/view$', views.viewJobPage),
    url(r'^job/add$', views.jobAdd),
    url(r'^job/giveup$', views.jobRemove),
    url(r'^job/done$', views.jobDone),
]