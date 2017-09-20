from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from core.forms import SignUpForm
from core.models import Urls

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template_index(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_next_page_link(self):
        expected = 'href="{}"'.format(('/'))
        self.assertContains(self.response, expected)


class LoginViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse('core:login')
        self.client = Client()

    def test_login_ok(self):
        """GET login must return status code 200"""
        response = self.client.get(self.url)
        # self.assertEquals(200, self.response.status_code)
        self.assertEquals(response.status_code, 200)

    def test_template_login(self):
        """Must use login.html"""
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'registration/login.html')


class SignupViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse('core:signup')
        self.client = Client()

    def test_signup_ok(self):
        """GET signup must return status code 200"""
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_signup(self):
        """Must use signup.html"""
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'registration/signup.html')


class SignUpFormTest(TestCase):

    def test_form_has_fields(self):
        """Form must have 4 fields."""
        form = SignUpForm()
        expected = ['username', 'email', 'password1', 'password2']
        self.assertSequenceEqual(expected, list(form.fields))


class UrlsModelTest(TestCase):

    def setUp(self):
        self.obj = Urls(
            short_id = 'mXoCUU',
            httpurl = 'https://bitly.com/',
            pub_date = 'Sept. 20, 2017, 5:03 a.m.',
            count = '0',
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Urls.objects.exists())
