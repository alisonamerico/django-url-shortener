from django.shortcuts import render, redirect, get_object_or_404
import random, string, json
from core.models import Urls
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.contrib.auth import login, logout, authenticate
from core.forms import SignUpForm
from django.views.generic import ListView
from django.contrib.sites.shortcuts import get_current_site


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST'or None:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('core:index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


class SearchList(ListView):
    template_name = 'search_list.html'
    model = Urls
    context_object = 'url'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Urls.objects.all()
        return Urls.objects.filter(user=self.request.user)



def redirect_original(request, short_id):
    url = get_object_or_404(Urls, pk=short_id) # get object, if not found return 404 error
    url.count += 1
    url.save()
    print(url.httpurl)
    return HttpResponseRedirect(url.httpurl)


def shorten_url(request):
    current_site = get_current_site(request)
    current_site.domain
    url = request.POST.get("url", '')
    if not (url == ''):
        short_id = get_short_code()
        b = Urls(httpurl=url, short_id=short_id, user=request.user)
        b.save()

        response_data = {}
        # response_data['url'] = settings.SITE_URL + "/" + short_id
        response_data['url'] = current_site.domain + "/" + short_id
    return HttpResponse(json.dumps(response_data),  content_type="application/json")
    return HttpResponse(json.dumps({"error": "error occurs"}), content_type="application/json")


def get_short_code():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    # if the randomly generated short_id is used then generate next
    while True:
        short_id = ''.join(random.choice(char) for x in range(length))
        try:
            temp = Urls.objects.get(pk=short_id)
        except:
            return short_id
