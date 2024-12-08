import pytest
from src.pergolaprojecttools.config_util import ConfigUtilBase
from src.pergolaprojecttools.exceptions import ConfigException

class NoFileConfigUtil(ConfigUtilBase):
    pass

class TestConfigUtil(ConfigUtilBase):

    config_path = 'tests/config/config.json'

    def get_batman(cls):
        return cls.get_config_value('batman')

    def get_batmans_car(cls):
        return cls.get_inner_value(cls.get_config_value('batmandetails'), 'preferredVehicle')


def test_no_config_file():
    config_util = NoFileConfigUtil()
    with pytest.raises(ConfigException) as excinfo:
        config_util.get_config_value('something')

    assert "ConfigUtilBase.config_path" in str(excinfo.value)

def test_get_config_inner():
    config_util = TestConfigUtil()

    batman = config_util.get_batmans_car()
    assert batman == "bat mobile"

def test_get_config():
    config_util = TestConfigUtil()

    batman = config_util.get_batman()
    assert batman == "Bruce Wayne"