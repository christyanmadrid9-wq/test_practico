import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pytest_html import extras

CI = bool(os.getenv("CI"))  # GitHub Actions define CI=true


@pytest.fixture
def driver():
    options = Options()
    if CI:
        for arg in ("--headless=new", "--no-sandbox", "--disable-dev-shm-usage", "--window-size=1920,1080"):
            options.add_argument(arg)
    d = webdriver.Chrome(options=options)
    if not CI:
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