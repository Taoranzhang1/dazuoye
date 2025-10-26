import os
import pytest

def test_environment_variables():
    os.environ["APP_NAME"] = "Python程序"
    os.environ["GREETING"] = "欢迎"
    
    app_name = os.getenv("APP_NAME")
    greeting = os.getenv("GREETING")
    
    assert app_name == "Python程序"
    assert greeting == "欢迎"

def test_default_values():
    default_app_name = os.getenv("NON_EXISTENT_VAR", "默认应用")
    assert default_app_name == "默认应用"

def test_string_operations():
    name = "测试用户"
    assert len(name) == 4
    assert name + "!" == "测试用户!"