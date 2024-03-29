from django.urls import path
from product.views import CategoryViewSet
from product.views import ProductViewSet
from product.views import ReviewViewSet
from product.views import UserViewSet

urlpatterns = [
    path('api/v1/categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/categories/<int:id>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/v1/products/', ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/products/<int:id>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/v1/reviews/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/reviews/<int:id>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/v1/users/', UserViewSet.as_view({'post': 'create'})),
    path('api/v1/users/confirm/', UserViewSet.as_view({'post': 'confirm'})),
]
