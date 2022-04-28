import json

from ..factory import Factory


class TestJsonSerializer:
    def test_json_serializer(self):
        dict1 = {"a": 1, "b": 2, "c": 3}
        assert json.dumps(dict1) == Factory.create_serializer("json").dumps(dict1)
