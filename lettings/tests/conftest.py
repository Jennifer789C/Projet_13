from django.test import Client
import pytest
from lettings.models import Address, Letting


@pytest.fixture()
def client():
    client = Client()
    return client


@pytest.fixture()
def address():
    address = Address.objects.create(number=250,
                                     street="Main Street",
                                     city="New York City",
                                     state="NY",
                                     zip_code=85263,
                                     country_iso_code="USA")
    return address


@pytest.fixture()
def letting(address):
    letting = Letting.objects.create(title="Auberge du soleil",
                                     address_id=address.id)
    return letting
