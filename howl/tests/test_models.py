import pytest

from .factories.observers import AlertFactory, ObserverFactory


@pytest.mark.django_db
class TestObserverModel:

    def test_repr(self):
        obj = ObserverFactory.create(name='test observer')

        assert str(obj) == 'test observer'

    @pytest.mark.parametrize('value, compare_value, return_value', [
        (49, 50, False),
        (50, 50, True),
        (51, 50, False),
    ])
    def test_is_exceeded(self, value, compare_value, return_value):
        obj = ObserverFactory.create(value=compare_value)
        obj.is_exceeded(value) is return_value


@pytest.mark.django_db
class TestAlertModel:

    def test_repr(self, activate_en):
        observer = ObserverFactory.create(name='my observer')
        obj = AlertFactory.create(id=23, observer=observer)

        assert str(obj) == 'Alert (ID: 23) for my observer'