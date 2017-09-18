from django.test import TestCase, Client


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template_index(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

class LoginViewTestCase(TestCase):

    def setUp(self):
        self.response = self.client.get('login')

    def test_login_ok(self):
        """GET login must return status code 200"""
        self.assertEquals(200, self.response.status_code)

    # def test_template_login(self):
    #     """Must use login.html"""
    #     self.assertTemplateUsed(self.response, 'login.html')
