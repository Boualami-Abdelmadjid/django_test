from django.test import TestCase, Client
from django.contrib.auth.models import User
import json
# Create your tests here.

class TestingUsers(TestCase):
    c = Client()
    
    def setUp(self):
        user = User.objects.create(username = "tester", email = 'tester')
        user.set_password('tester')
        user.save()

    #Check pages that does not require login
    def test_offline_pages(self):
        pages = ['/register/','/login/']
        for page in pages:
            response = self.c.get(page)
            self.assertEqual(response.status_code, 200)