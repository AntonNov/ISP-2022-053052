import pickle
from task_2.abstract_serializer import AbstractSerializer


class TestPickleSerializer:
    def test_pickle_serializer(self):
        dict1 = {'a': 1, 'b': 2, 'c': 3}
        serializer = AbstractSerializer("pickle")
        assert pickle.dumps(dict1) == serializer.serialize(dict1)