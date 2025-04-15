from django.contrib import admin
from django.urls import path, include
from minha_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('minha_app.urls')),  # Inclui as rotas da sua app
    path('chatbot/', views.chatbot_response, name='chatbot'),  # API do chatbot
]
