from django.db import models
from django.contrib.auth.models import User


class Neighbourhood(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    occupants_count = models.IntegerField()
    Admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    health = models.IntegerField(null=True, blank=True)
    police = models.IntegerField(null=True, blank=True)
    description = models.TextField()



    def __str__(self):
        return f'{self.name} mtaa'

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def find_neighbourhood(cls, neighbourhood_id):
        return cls.objects.filter(id=neighbourhood_id)




class Business(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    description = models.TextField(blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    business_image = models.ImageField(upload_to='images/', default='default2.jpg')

    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls, business_id):
        return cls.objects.filter(id=business_id)


class Post(models.Model):
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')
    mtaa = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='mtaa_post')


    def create_post(self):
        self.save()

    def save_post(self):
        self.save()

    def delete_post(self):
        self.save()