from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe import views


router = DefaultRouter()   # Auto generate API endpoints for TagViewSet
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)
router.register('recipes', views.RecipeViewSet)

app_name = 'recipe'    # So that the reverse() can locate the correct urls

urlpatterns = [
    path('', include(router.urls))
]
