from django.urls import path, include

from rest_framework.routers import DefaultRouter

from categories.views import MainCategoryViewSet, SubCategoryViewSet, SubSubCategoryViewSet

router = DefaultRouter()
router.register(r'main-categories', MainCategoryViewSet)
router.register(r'sub-categories', SubCategoryViewSet)
router.register(r'sub-sub-categories', SubSubCategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
] 