from django.db import models
from django.urls import reverse # Новый импорт


class Car(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    price = models.TextField()
    year = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self): # Тут мы создали новый метод
        return reverse('post_detail', args=[str(self.id)])
    
class Image(models.Model):
    post = models.ForeignKey(Car, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/post_images/')