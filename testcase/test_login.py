from page.main import Main


class TestLogin:
    def setup(self):
        self.main = Main()

    def test_login(self):
        assert True == self.main.into_login().into_register().register()
        # assert  True == self.main.into_login().scan()
