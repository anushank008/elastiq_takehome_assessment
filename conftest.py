import pytest
from selenium import webdriver

@pytest.fixture(scope='class')
def launchBrowser(request):
    driver = webdriver.Chrome()
    driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
    print("Browser launched")
    request.cls.driver = driver
    yield 
    print("Test completed!")
    driver.quit()