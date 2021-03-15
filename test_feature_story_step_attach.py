import pytest
import allure


@allure.severity(allure.severity_level.MINOR)
@allure.feature("搜索模块")
class TestSearch():
    @allure.title("case1")
    def test_case1(self):
        print("测试用例-搜索模块-case1")

    @allure.title("case2")
    def test_case2(self):
        print("测试用例-搜索模块-case2")


@allure.severity(allure.severity_level.TRIVIAL)
@allure.feature("登录模块")
class TestLogin():
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("登录成功")
    @allure.title("登录成功")
    def test_login_success(self):
        print("测试用例-登录模块-登录成功")
        pass

    TEST_CASE_LINK = 'http://www.baidu.com'

    @allure.testcase(TEST_CASE_LINK, 'Test case title: 登录失败')
    @allure.severity(allure.severity_level.MINOR)
    @allure.story("登录失败")
    @allure.title("登录失败")
    def test_login_failure(self):
        print("测试用例-登录模块-登录失败")
        with allure.step("步骤1：点击用户名"):
            print("输入用户名")
        with allure.step("步骤2：点击密码"):
            print("输入密码")
        print("点击登录")
        with allure.step("步骤3：点击登陆之后登录失败"):
            assert 1 == 1
            print("登录失败")
            allure.attach('显示登录失败', name='信息', attachment_type=allure.attachment_type.TEXT)
            allure.attach.file("./files/login_fail.jpg", name='screen_shot', attachment_type=allure.attachment_type.JPG)
            allure.attach.file("./files/error.log", name='log', attachment_type=allure.attachment_type.TEXT)


if __name__ == '__main__':
    pytest.main(['test_feature_story_step_attach.py'], '-vs')

"""
pytest test_feature_story_step_attach.py -vs --alluredir=./results --clean-alluredir
pytest test_feature_story_step_attach.py -vs --allure-features="登录模块" --allure-stories="登录失败" --alluredir=./results --clean-alluredir
allure serve ./results
"""
