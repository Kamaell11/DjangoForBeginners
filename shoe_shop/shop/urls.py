from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('indexEight', views.indexEight, name='indexEight'),
    path('indexFive', views.indexFive, name='indexFive'),
    path('indexFour', views.indexFour, name='indexFour'),
    path('indexNine', views.indexNine, name='indexNine'),
    path('indexSeven', views.indexSeven, name='indexSeven'),
    path('indexSix', views.indexSix, name='indexSix'),
    path('indexTen', views.indexTen, name='indexTen'),
    path('indexThree', views.indexThree, name='indexThree'),
    path('indexTwo', views.indexTwo, name='indexTwo'),
]