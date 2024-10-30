from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class List(models.Model):
    list_name = models.CharField(max_length=200)
    list_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def str(self):
        return self.list_name
    
    def get_absolute_url(self):
        return reverse('lista-sida', kwargs={'pk': self.pk})

class Item(models.Model):
    item_name = models.CharField('Varans namn', max_length=255)
    amount = models.IntegerField('Antal',default=1)
    purchased = models.BooleanField(default=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def str(self):
        return self.item_name
    
    def get_absolute_url(self):
        return reverse('lista-sida', kwargs={'pk': self.list.pk})
    
class SharedList(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='list_shared')
    email = models.EmailField()

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user = User.objects.get(email=self.email)
        super().save(*args, **kwargs)

