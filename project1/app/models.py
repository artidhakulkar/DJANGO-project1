from django.db import models

# Create your models here.

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to="app/images", default="")
    email = models.CharField(max_length=100, default = "")
    name = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=200, default="")
    phone = models.CharField(max_length=14, default="")
    address = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name



