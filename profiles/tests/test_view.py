from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_view_profile_index(client, profile):
    response = client.get(reverse("profiles:index"))
    assert response.status_code == 200
    assert b'<title>Profiles</title>' in response.content
    assert profile in response.context["profiles_list"]


@pytest.mark.django_db
def test_view_profile(client, profile):
    response = client.get(reverse("profiles:profile",
                                  args=[f"{profile.user.username}"]))
    assert response.status_code == 200
    assert profile.user.username == "test"
    assert b'<title>test</title>' in response.content
    assert response.context["profile"] == profile
