from django.db import models
from django.utils import timezone


class Owner(models.Model):
    full_name = models.CharField(max_length=60)

    def __str__(self) -> str:
        return f"Господар: {self.full_name}"


class Document(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"Документ: {self.title}"


class CopyrightObject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Об'єкт: {self.name}"


class MainPatent(models.Model):
    owner = models.ForeignKey(to=Owner, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
