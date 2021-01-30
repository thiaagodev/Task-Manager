"""tasks_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from api.views import *

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Task Manager',
        default_version='V1',
        description='Uma API de gerenciamento de tarefas feito com Django Rest Framework, nele é possível se registrar, logar e criar suas tarefas, também é possivel editá-las e excluí-las.',
        contact=openapi.Contact(email='thiaago.dev@gmail.com', url='https://github.com/thiaagodev')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', RegisterUserView.as_view()),
    path('login', LoginView.as_view()),
    path('tasks', TasksListView.as_view()),
    path('task/<int:id>', TasksDetailView.as_view()),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("redoc", schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
