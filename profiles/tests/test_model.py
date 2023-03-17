from django.contrib.auth import get_user_model
import pytest
from profiles.models import Profile

User = get_user_model()


@pytest.mark.django_db
def test_model_profile():
    user = User.objects.create(password="mdp",
                               username="test")

    profile = Profile.objects.create(user_id=user.id,
                                     favorite_city="Brooklynn")

    assert str(profile) == "test"
