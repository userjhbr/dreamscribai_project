from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('interpret_dream', views.interpret_dream, name='interpret_dream'),
]
