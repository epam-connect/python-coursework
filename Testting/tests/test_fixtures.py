import os, sys
import pytest
from func.save_data import save_data
from func.Person import is_eligable



def test_file(tmpdir):
    filepath = os.path.join(tmpdir, 'temp.txt')
    data = "This is saved data"
    save_data(filepath, data)
    
    with open(filepath, 'r') as file:
        assert file.readline() == data

class Test_Person:
    def test_person_age(self, sample_person):
        print(sample_person)
        assert sample_person.getAge() >= 18

    def test_person_setCredit(self, sample_person):
        print(sample_person)
        credit = 10
        sample_person.setCredit(credit)
        assert sample_person.getCredit() == credit

    def test_person_getCredit(self, sample_person):
        print(sample_person)
        credit = 10
        assert sample_person.getCredit() == credit


@pytest.mark.parametrize(
        "sample_person_with_param, sample_output",
        [
            (18, True),
            (20, True),
            (10, False),
            (5, False)
        ],
        indirect=['sample_person_with_param', 'sample_output']      # inputes are passed to fixtures then result is passed as parameters
)
def test_person_is_eligable(sample_person_with_param, sample_output):
    assert is_eligable(sample_person_with_param) == sample_output