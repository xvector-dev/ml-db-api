from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import TestModel
from .serializers import TestModelSerializer


class TestModelView(ModelViewSet):
  permission_classes = [AllowAny]
  serializer_class = TestModelSerializer

  def get_queryset(self):
    data = TestModel.objects.all()
    return data
