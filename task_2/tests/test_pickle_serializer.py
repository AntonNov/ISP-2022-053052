import pickle

from ..factory import Factory


class TestPickleSerializer:
    def test_pickle_serializer(self):
        dict1 = {"a": 1, "b": 2, "c": 3}
        assert pickle.dumps(dict1) == Factory.create_serializer("json").dumps(dict1)
