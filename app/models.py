import datetime

from django.db import models


# Create your models here.
class Profile(models.Model):
    nome = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    picture = models.ImageField(
        upload_to='app/static/img/profile_pictures/' + str(hash(datetime.datetime.now())) + "/",
        default='app/static/img/default.jpg')
    morada = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    pais = models.CharField(max_length=25)
    tipo = models.IntegerField()

    def __str__(self):
        return self.nome