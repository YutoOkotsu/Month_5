"""
URL configuration for shop_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from product.views import CategoryViewSet
from product.views import ProductViewSet
from product.views import ReviewViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', CategoryViewSet.as_view({'get': 'list'})),
    path('api/v1/categories/<int:id>/', CategoryViewSet.as_view({'get': 'retrieve'})),
    path('api/v1/products/', ProductViewSet.as_view({'get': 'list'})),
    path('api/v1/products/<int:id>/', ProductViewSet.as_view({'get': 'retrieve'})),
    path('api/v1/reviews/', ReviewViewSet.as_view({'get': 'list'})),
    path('api/v1/reviews/<int:id>/', ReviewViewSet.as_view({'get': 'retrieve'})),
]
