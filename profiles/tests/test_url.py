from django.urls import reverse, resolve
from profiles.views import index, profile


def test_url_profile_index():
    url = reverse("profiles:index")
    assert resolve(url).view_name == "profiles:index"
    assert resolve(url).func == index


def test_url_profile():
    url = reverse("profiles:profile", args=[1])
    assert resolve(url).view_name == "profiles:profile"
    assert resolve(url).func == profile
