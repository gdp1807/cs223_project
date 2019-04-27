from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase) :


    def test_home(self):
        client = Client()
        response = client.get(reverse('codegen:home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'codegen/home.html')


    def test_generate(self):
        client = Client()
        response = client.get(reverse('codegen:generate'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'codegen/generate.html')


    def test_output(self):
        client = Client()
        response = client.get(reverse('codegen:output'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'codegen/output.html')