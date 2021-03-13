import pytest


class TestData:
    @pytest.mark.parametrize("a,b", [(1, 2)])
    def test_data(self, a, b):
        print(a + b)
