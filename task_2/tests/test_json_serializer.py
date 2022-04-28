import json
from ..serializers.json_serializer import JsonSerializer


class TestJsonSerializer:
    def test_json_serializer(self):
        serializer = JsonSerializer()
        dict1 = {'a': 1, 'b': 2, 'c': 3}
        assert json.dumps(dict1) == JsonSerializer.dumps(dict1)
