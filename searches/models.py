from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length =160,null = True)

    def __str__(self):
        return self.location
    
class Category(models.Model):
    category = models.CharField(max_length =160,null = True)
 

    def __str__(self):
        return self.category

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/',blank = True)
    name = models.CharField(max_length =160,null = True)
    description = models.TextField(max_length =1060)
    category = models.ForeignKey(Category,on_delete = models.CASCADE,null = True)
    location = models.ForeignKey(Location,on_delete = models.CASCADE,null = True)

    @classmethod
    def search_by_category(cls,search_term):
        imgs = cls.objects.filter(category__category__icontains=search_term)
        return imgs
    
    @classmethod
    def search_by_location(cls,search_term):
        img = cls.objects.filter(location__location__icontains=search_term)
        return img
   
    def __str__(self):
        return self.name

   
    def save_images(self):
        self.save()
   
    def delete_images(self):
        self.delete()

    def get_image_by_id(id):
        image = Image.objects.get(id = image_id)
        return image