
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]


'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]



error


from django.urls import path
from LINEUPAPP import views

urlpatterns = [
    path(r'^, views.index, name='index')
]





'''