from rest_framework.routers import DefaultRouter
from .views import TestModelView
from django.urls import path, include

router = DefaultRouter()
router.register('test-model', TestModelView, basename='test-model')

urlpatterns = [
  path('', include(router.urls))
]