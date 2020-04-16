from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    # image = models.ImageField(upload_to='blog_app/images/')
    # url = models.URLField(blank=True)
    date = models.DateField(default='None')