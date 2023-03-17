from django.contrib.auth import get_user_model
from django.test import Client
import pytest
from profiles.models import Profile

User = get_user_model()


@pytest.fixture()
def client():
    client = Client()
    return client


@pytest.fixture()
def profile():
    user = User.objects.create(password="mdp",
                               username="test")
    profile = Profile.objects.create(user_id=user.id,
                                     favorite_city="Brooklynn")
    return profile
