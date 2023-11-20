from rest_framework import serializers
from .models import MainCategory, SubCategory, SubSubCategory

class SubSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSubCategory
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    subsubcategories = SubSubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = '__all__'

class MainCategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = MainCategory
        fields = '__all__'
