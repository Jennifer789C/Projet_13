import pytest
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_model_address():
    address = Address.objects.create(number=250,
                                     street="Main Street",
                                     city="New York City",
                                     state="NY",
                                     zip_code=85263,
                                     country_iso_code="USA")
    assert str(address) == "250 Main Street"


@pytest.mark.django_db
def test_model_letting():
    address = Address.objects.create(number=250,
                                     street="Main Street",
                                     city="New York City",
                                     state="NY",
                                     zip_code=85263,
                                     country_iso_code="USA")
    letting = Letting.objects.create(title="Auberge du soleil",
                                     address_id=address.id)
    assert str(letting) == "Auberge du soleil"
