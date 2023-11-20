from rest_framework import viewsets
from .models import MainCategory, SubCategory, SubSubCategory
from .serializers import MainCategorySerializer, SubCategorySerializer, SubSubCategorySerializer

class MainCategoryViewSet(viewsets.ModelViewSet):
    queryset = MainCategory.objects.all()
    serializer_class = MainCategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class SubSubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubSubCategory.objects.all()
    serializer_class = SubSubCategorySerializer
