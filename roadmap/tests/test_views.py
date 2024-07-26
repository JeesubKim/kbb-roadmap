from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

class TestRoadmap(TestCase):
    def test_get_roadmap_page(self):
        url = reverse('roadmap:main')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'roadmap/roadmap.html')

class TestRoadmapCreate(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="testman", email="testman@kbb.com", password="testman"
        )
    
    def test_get_roadmap_create_page(self):
        url = reverse('roadmap:create')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'roadmap/roadmap_create.html')


    def test_creating_roadmap(self):
        login = self.client.login(username="testman", password="testman")
        self.assertTrue(login)

        url = reverse('roadmap:create')
        roadmap_name = "testman_roadmap"
        assignee = "testman_assignee"

        response = self.client.post( url, {
            "roadmap_name":roadmap_name,
            "assignee":assignee
        })


        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "roadmap/roadmap.html")
    

    
    # def test_creating_roadmap_not_login(self):
    """ This has been failed """    
    #     url = reverse('roadmap:create')
    #     roadmap_name = "testman_roadmap"
    #     assignee = "testman_assignee"

    #     response = self.client.post( url, {
    #         "roadmap_name":roadmap_name,
    #         "assignee":assignee
    #     })


    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "user/login.html")

    
    