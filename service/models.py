from django.db import models

class Service(models.Model):
    name = models.CharField(max_length =30)
    description =models.TextField()
    image = models.ImageField(upload_to='service/images/') 

    def __str__(self) -> str:
        return self.name
