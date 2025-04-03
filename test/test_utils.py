import json
from unittest.mock import Mock
from src.extract_utils import get_weather_data, get_aq_data

with open("test/weather_sample.json", "r") as file:
    weather_data = json.load(file)

with open("test/aq_sample.json", "r") as file:
    aq_data = json.load(file)

class TestExtractUtils:
    def test_get_weather_data_outputs_data_on_correct_type(self):
            weather_response = Mock()
            weather_response.json.return_value = weather_data
            result = get_weather_data(weather_response)
            assert type(result) == dict

    def test_get_weather_data_outputs_expected_values(self):
            weather_response = Mock()
            weather_response.json.return_value = weather_data
            result = get_weather_data(weather_response)
            assert '2025-04-03' in result

    def test_get_weather_data_contains_nested_values(self):
            weather_response = Mock()
            weather_response.json.return_value = weather_data
            result = get_weather_data(weather_response)
            assert type(result['2025-04-03']) == list