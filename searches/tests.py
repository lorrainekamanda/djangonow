from django.test import TestCase
from .models import Image,Category,Location
# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    """
    testing the instation of the image class
    """
    def setUp(self):
        self.image= Image(image= 'default.jpg', description ='Taken in the swiss', name ='Terrian')
        self.new_category = Category(category = 'entertainment')
        self.new_category.save()
        self.new_location= Location(location = 'New York',)
        self.new_location.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    def test_save_image(self):
        self.image.save_images()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_delete_image(self):
        self.image.save_images()
        images = Image.objects.all()
        self.image.delete_images()
        self.assertTrue(len(images) == 0)
    