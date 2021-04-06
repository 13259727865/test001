#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:Gemini
import pytest as pytest


@pytest.fixture(params=[(1,2),(3,4)],ids=["a","b"])
def login(request):
	print(f"登录{request.param[0]}")
	yield request.param
	print(f"注销{request.param[1]}")

@pytest.mark.usefixtures("login")
class TestFixture:

	@pytest.mark.usefixtures("login")
	def test_demo1(self,login):
		print(f"demo1--{login[0]}")

	def test_demo2(self):
		print("demo2")

	@pytest.mark.usefixtures("login")
	def test_demo3(self):
		print("demo3")

	def test_demo4(self):
		print("demo4")
		pytest.assume(100==200)
		pytest.assume(1==1)
		pytest.assume(True == False)

if __name__ == '__main__':
	pytest.main("test_fixture.py")