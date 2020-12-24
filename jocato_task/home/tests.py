from django.test import TestCase, Client
from django.urls import reverse


from jocato_task import urls
from home.views import index, home

# Create your tests here.
class HomeUrlTesting(TestCase):

    def test_default_url(self):
        client = self.client.get("/")
        status_code = client.status_code
        self.assertEquals(status_code, 200)

    def test_home_url(self):
        client = self.client.get("/home/")
        status_code = client.status_code
        self.assertEquals(status_code, 200)

class HomeViewsTesting(TestCase):

    def test_default_view(self):
        client = Client()
        response = client.get(reverse("index"))
        self.assertTemplateUsed(response, "index.html")

    def test_home_view(self):
        client = Client()
        response = client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")