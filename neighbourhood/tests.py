from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from .models import Post, Business
from users.models import Profile
from django.contrib.auth.models import User

# Create your tests here.


# class TestPost(TestCase):
#     def setUp(self):
#         self.user = User(username='Ndundiro')
#         self.user.save()
#         self.post_test = Post(id=1,post='Emergency numbers', user=self.user, mtaa=self.mtaa)

        
#     def test_instance(self):
#         self.assertTrue(isinstance(self.post_test, Post))

#     def test_save_post(self):
#         self.post_test.save_post()
#         posts = Post.objects.all()
#         self.assertTrue(len(posts) > 0)

#     def test_delete_post(self):
#         before = Profile.objects.all()
#         self.post_test.delete_post()
#         after = Profile.objects.all()
#         self.assertTrue(len(before) == len(after))




# class TestBusiness(TestCase):
#     def setUp(self):
#         self.user = User(username='Ndundiro')
#         self.user.save()
#         self.business_test = Business(id=1,name='Motor Gari sellers',email ='mtot@gari.com', description='the best of the best.', neigbourhood=self.neighbourhood, user=self.user, business_image='default.jpg')

        
#     def test_instance(self):
#         self.assertTrue(isinstance(self.business_test, Business))

#     def test_save_business(self):
#         self.business_test.save_post()
#         businesses = Business.objects.all()
#         self.assertTrue(len(businesses) > 0)

#     def test_delete_business(self):
#         before = Business.objects.all()
#         self.business_test.delete_post()
#         after = Business.objects.all()
#         self.assertTrue(len(before) == len(after))

