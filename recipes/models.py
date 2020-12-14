from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    prep_time = models.IntegerField(verbose_name="Prep time (minutes)")
    cook_time = models.IntegerField(verbose_name="Cook time (minutes)")
    instructions = models.TextField(default='')
    image = models.ImageField(default='', upload_to='recipe_images')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if (img.height > 720 and img.width > 1280):
            output_size = (1280, 720)
            img.thumbnail(output_size)
            img.save(self.image.path)