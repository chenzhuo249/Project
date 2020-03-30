from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(verbose_name="作家", max_length=12)

    def __str__(self):
        return f"{self.id}--{self.name}"

class Wife(models.Model):
    name = models.CharField(verbose_name="妻子", max_length=12)
    husband = models.OneToOneField(Author)

    def __str__(self):
        return f"{self.id}--{self.name}--{self.husband_id}"