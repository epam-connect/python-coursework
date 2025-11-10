import pytest
from func.Person import Person

@pytest.fixture(scope='module')
def sample_person():
    # Setup code
    print("Fixture")
    yield Person("Ankan", 22, 0)
    
    # Teardown code

@pytest.fixture(scope='function')
def sample_person_with_param(request):
    # print("Creating person")

    yield Person("Ankan", request.param, 18)

    # print("Destroying person")

@pytest.fixture
def sample_output(request):
    print(request.param)
    return request.param
