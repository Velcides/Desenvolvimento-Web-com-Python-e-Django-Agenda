"""
URL configuration for agenda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Adicionando a URL da agenda.
    path('agenda/', views.lista_eventos),
    #path('agenda/lista/', views.json_lista_evento),
    path('agenda/lista/<int:id_evento>/', views.json_lista_evento),
    # Rotas para inserção de dados.
    path('agenda/evento/', views.evento),
    path('agenda/evento/submit', views.submit_evento),
    # Definindo rota para exclusão.
    path('agenda/evento/delete/<int:id_evento>/', views.delete_evento),
    # Definindo uma view para o path padrão, redirecionando-o para o path de agenda.
    path('', RedirectView.as_view(url='/agenda/')),
    # Criando urls de autenticação.
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    # Path de logout.
    path('logout/', views.logout_user)
]
