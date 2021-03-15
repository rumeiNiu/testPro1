import pytest
import yaml


# 参数化:string
@pytest.mark.parametrize("a,b", [(10, 20), (100, 200)])
def test_data1(a, b):
    assert a * 2 == b


# 参数化:turple
@pytest.mark.parametrize(("a", "b"), [(10, 20), (100, 200)])
def test_data2(a, b):
    assert a * 2 == b


# 参数化:list
@pytest.mark.parametrize(["a", "b"], [(10, 20), (100, 200)])
def test_data3(a, b):
    assert a * 2 == b


# 参数化:yaml
@pytest.mark.parametrize(("a", "b"), yaml.safe_load(open('data.yml')))
def test_data4(a, b):
    assert a * 2 == b


class TestDemo:

    @pytest.mark.parametrize("env", yaml.safe_load(open('env.yml')))
    def test_env(self, env):
        if "test" in env:
            assert "test" in env
            print("测试环境IP：", env['test'])
        elif "dev" in env:
            assert "dev" in env
            print("开发环境IP：", env['dev'])


if __name__ == '__main__':
    pytest.main(['test_para_yaml.py'], '-vs')
