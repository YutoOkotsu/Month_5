from django.urls import path
from product.views import CategoryView, ProductView, ReviewView
from product.views import UserViewSet


urlpatterns = [
    path('api/v1/categories/', CategoryView.as_view()),
    path('api/v1/products/', ProductView.as_view()),
    path('api/v1/reviews/', ReviewView.as_view()),
    path('api/v1/users/', UserViewSet.as_view({'post': 'create'})),
    path('api/v1/users/confirm/', UserViewSet.as_view({'post': 'confirm'})),
]
