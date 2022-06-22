from email.mime import image
from platform import release
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Bikeimage(models.Model):
    image = models.ImageField()
    alt=models.TextField(max_length=140,blank=False)

class Biketable(models.Model):
    Model = models.CharField(max_length=200,default="")
    Year = models.CharField(max_length=200,default="")
    Category = models.CharField(max_length=200,default="")
    Rating = models.CharField(max_length=200,default="")
    Displacement = models.CharField(max_length=200,default="")
    Engine_type = models.CharField(max_length=200,default="")
    Power = models.CharField(max_length=200,default="")
    Top_speed = models.CharField(max_length=200,default="")
    Fuel_system = models.CharField(max_length=200,default="")
    Cooling_system = models.CharField(max_length=200,default="")
    Gearbox = models.CharField(max_length=200,default="")
    Transmission_type = models.CharField(max_length=200,default="")
    Clutch = models.CharField(max_length=200,default="")
    Fuel_consumption = models.CharField(max_length=200,default="")
    Greenhouse_gases = models.CharField(max_length=200,default="")
    Frame_type = models.CharField(max_length=200,default="")
    Front_suspension = models.CharField(max_length=200,default="")
    Rear_suspension = models.CharField(max_length=200,default="")
    Front_tire = models.CharField(max_length=200,default="")
    Rear_tire = models.CharField(max_length=200,default="")
    Front_brakes = models.CharField(max_length=200,default="")
    Rear_brakes = models.CharField(max_length=200,default="")
    Dry_weight = models.CharField(max_length=200,default="")
    Power_weight_ratio = models.CharField(max_length=200,default="")
    Seat_height = models.CharField(max_length=200,default="")
    Overall_height = models.CharField(max_length=200,default="")
    Overall_length = models.CharField(max_length=200,default="")
    Overall_width = models.CharField(max_length=200,default="")
    Wheelbase = models.CharField(max_length=200,default="")
    Fuel_capacity = models.CharField(max_length=200,default="")
    Color_options = models.CharField(max_length=200,default="")
    Starter = models.CharField(max_length=200,default="")
    Factory_warranty = models.CharField(max_length=200,default="")
    Comments = models.CharField(max_length=200,default="")
    Update_specs = models.CharField(max_length=200,default="")
    Insurance_costs = models.CharField(max_length=200,default="")
    Finance_options = models.CharField(max_length=200,default="")
    Parts_finder = models.CharField(max_length=200,default="")
    Maintenance = models.CharField(max_length=200,default="")
    Ask_questions = models.CharField(max_length=200,default="")
    Related_bikes = models.CharField(max_length=200,default="")

class Bikepost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_bikeposts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ForeignKey(Bikeimage, on_delete=models.SET_DEFAULT, default="")
    table=models.ForeignKey(Biketable,on_delete=models.SET_DEFAULT,default="")
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title



