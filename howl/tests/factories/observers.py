import factory
from factory.fuzzy import FuzzyChoice

from howl.models import Alert, Observer
from howl.operators import get_operator_types


class ObserverFactory(factory.DjangoModelFactory):
    name = factory.Sequence(lambda i: 'observer {0}'.format(i))
    operator = get_operator_types()[0][0]
    value = 50
    waiting_period = 0

    class Meta:
        model = Observer


class AlertFactory(factory.DjangoModelFactory):
    observer = factory.SubFactory(ObserverFactory)
    value = FuzzyChoice(range(1, 10))

    class Meta:
        model = Alert
