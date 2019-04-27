from django.test import SimpleTestCase
from django.urls import resolve, reverse
from codegen.views import home, generate, output

class TestUrls(SimpleTestCase) :

    def test_home_url_is_resolved(self):
        url = reverse('codegen:home')
        self.assertEquals(resolve(url).func, home)


    def test_generate_url_is_resolved(self):
        url = reverse('codegen:generate')
        self.assertEquals(resolve(url).func, generate)


    def test_output_url_is_resolved(self):
        url = reverse('codegen:output')
        self.assertEquals(resolve(url).func, output)