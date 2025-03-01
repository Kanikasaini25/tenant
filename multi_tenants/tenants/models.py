from django.db import models
from django.contrib.auth.models import AbstractUser



class Tenant(models.Model):
    name=models.CharField(max_length=255,unique=True)
    tenant_id=models.CharField(max_length=50,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    tenant=models.ForeignKey(Tenant,on_delete=models.CASCADE)


class Media(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    file=models.FileField(upload_to='tenant_%(tenant_id)s/media/')
    uploaded_at=models.DateTimeField(auto_now_add=True)


