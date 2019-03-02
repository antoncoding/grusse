from django.urls import path

from . views import inbox, compose
urlpatterns = [
    path('', inbox),
    path('compose', compose)
    # path('template/', views.template, name='template' )
]