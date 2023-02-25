from django.db import models

from apps.models.abstracts import BaseModel


class Department(BaseModel):
    title = models.CharField(max_length=40)
    category = models.ManyToManyField('apps.Category')

    def __str__(self):
        return self.title
