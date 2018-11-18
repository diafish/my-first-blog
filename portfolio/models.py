from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length = 120)
    post = models.TextField()
    image = models.ImageField(default='default.png',blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.title       
# Create your models here.
