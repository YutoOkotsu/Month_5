from rest_framework import viewsets
from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class UserSet(viewsets.ModelViewSet):
    ...
@action(detail=False, methods=['post'])
def confirm(self, request):
    confirmation_code = request.data.get('confirmation_code')
    user = User.objects.filter(confirmation_code=confirmation_code).first()
    if user:
        user.is_active = True
        user.save()
        return Response({'status': 'Пользователь подтвержден'})
    else:
        return Response({'error': 'Неверный код подтверждения'}, status=400)

