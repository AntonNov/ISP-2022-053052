import pickle

from ..factory import Factory
import unittest


class TestPickleSerializer(unittest.TestCase):
    def test_pickle_serializer(self):
        dict1 = {"a": 1, "b": 2, "c": 3}
        assert pickle.dumps(dict1) != Factory.create_serializer("pickle").dumps(dict1)
