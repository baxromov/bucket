from django.db import models

from apps.models.abstracts import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title