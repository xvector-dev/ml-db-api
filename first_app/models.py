from django.db import models


class TestModel(models.Model):
  # ... Other fields
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


  def __str__(self) -> str:
    return self.created_at