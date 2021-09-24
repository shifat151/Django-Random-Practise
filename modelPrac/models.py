from django.db import models
from account.models import Parent

# Create your models here.
from django.db import models

class Document(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    image = models.FileField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Child(models.Model):
    parents = models.ManyToManyField(
        to = Parent,
        blank = True,
        default = None,
        related_name = 'padres'
    )
    name=models.CharField(blank=True, default='child1', max_length=15)


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        ordering=['-id']

    def __str__(self):
        return self.first_name+' '+self.last_name
    


        


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()

    class Meta:
        ordering=['-id']

    def __str__(self):
        return self.name


class Concert(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    artists=models.ManyToManyField(Musician)

    class Meta:
        ordering=['-id']

    def __str__(self):
        return self.name






