from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class TestCase(TestCase):
    
    def test_index(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:index'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/index.html', 'doctors/layout.html')
        
    def test_maps(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:maps'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/maps.html', 'doctors/layout.html')
        
    def test_news(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:news'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/news.html', 'doctors/layout.html')
        
    def test_about(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:about'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/about.html', 'doctors/layout.html')
        
    def test_healthblog(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:healthblog'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/healthblog.html', 'doctors/layout.html')
        
    # =================================================================================================
    
    def test_mnews(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:mnews'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/mnews.html', 'doctors/adlayout.html')
        
    def test_mpromotion(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:mpromotion'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/mpromotion.html', 'doctors/adlayout.html')
        
    def test_mhealthblog(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:mhealthblog'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/mhealthblog.html', 'doctors/adlayout.html')
        
    def test_mdoctor(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:mdoctor'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/mdoctor.html', 'doctors/adlayout.html')
        
    def test_edithealthblog(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:edithealthblog'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/edithealthblog.html', 'doctors/adlayout.html')
        
    def test_editnews(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:editnews'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/editnews.html', 'doctors/adlayout.html')
        
    # =================================================================================================
    
    def test_umaps(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:umaps'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/umaps.html', 'doctors/layout.html')
        
    def test_unews(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:unews'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/unews.html', 'doctors/layout.html')
        
    def test_userhome(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:userhome'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/userhome.html', 'doctors/layout.html')
        
    def test_uhealthblog(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:uhealthblog'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/uhealthblog.html', 'doctors/layout.html')