from re import sub
from tokenize import blank_re
from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from restaurant.models import Restaurant
# Create your models here.

cat_choice = (
    ("veg", "Veg"),
    ("vegan", "Vegan"),
    ("non-veg", "Non-veg")
)
class SubCategory(models.Model):
    name = models.CharField(choices=cat_choice, max_length=50)

    def __str__(self) -> str:
        return self.name
        
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    class Meta:
        ordering = ['name']
        
    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f"/{self.slug}/"
    
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=255, default="")
    image = models.ImageField(upload_to="images/product/", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="images/product/", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="product")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    class Meta:
        ordering = ['-date_added']
    
    def get_absolute_url(self):
        return f"http://127.0.0.1:8000/api/product/{self.category.slug}/{self.slug}/",
         
        

    # def get_restaurant_url(self):
    #     return f"http://127.0.0.1:8000/api/product/{self.restaurant.slug}/"
    
    def get_image(self):
        if self.image:
            return "http://127.0.0.1:8000" + self.image.url
        return ""
    
    def get_thumbnail(self):
        if self.thumbnail:
            self.thumbnail = self.make_thumbnail(self.image)
            self.save()

            return "http://127.0.0.1:8000" + self.thumbnail.url
        else:
            return ""

    def make_thumbnail(self, image, size = (300, 200)):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)

        thumb_to = BytesIO()
        img.save(thumb_to, "JPEG", quality=85)
        thumbnail = File(thumb_to, name=image.name)
        return thumbnail
        
