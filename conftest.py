import os
import pytest
from selenium import webdriver
from pytest_html import extras


@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.maximize_window()
    yield d
    d.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    rep = (yield).get_result()
    if rep.when == "call" and rep.failed and "driver" in item.funcargs:
        drv = item.funcargs["driver"]
        os.makedirs("screenshots", exist_ok=True)
        drv.save_screenshot(f"screenshots/{item.name}.png")
        rep.extras = getattr(rep, "extras", []) + [extras.png(drv.get_screenshot_as_base64())]
