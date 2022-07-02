from django.db import models
from accounts.models import CustomUser

# Create your models here.


class ItemModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=400)
    description = models.CharField(max_length=5000)
    image = models.ImageField(blank=True, upload_to='item_img')

    def __str__(self):
        return self.title + " " + str(self.id)


class ItemReveiw(models.Model):
    item = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, null=True)
    rating_description = models.TextField(
        blank=True, null=True, max_length=5000)

    def __str__(self):
        return str(self.item) + " " + "Review"
