from django.urls import path
from . import views
from .views import chatbot_response

urlpatterns = [
    path('projetos/', views.projetos, name='projetos'),
    path('integrantes/', views.integrantes, name='integrantes'),
    path('curso/', views.curso, name='curso'),
    path('fale-conosco/', views.fale_conosco, name='fale_conosco'),
    path('solicitacao-de-projetos/', views.solicitacao_projetos, name='solicitacao_projetos'),
    path('', views.home, name='home'),
    path('chatbot/', chatbot_response, name='chatbot'),
]