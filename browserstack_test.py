from selenium import webdriver
from config import BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY


def run_browserstack_tests():
    """Run tests on BrowserStack."""
    desired_capabilities = {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "os": "Windows",
        "osVersion": "10",
        "name": "Web Scraping Test"
    }

    driver = webdriver.Remote(
        command_executor=f"http://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
        desired_capabilities=desired_capabilities
    )

    # Test logic (e.g., visiting URLs, asserting content)
    driver.get("https://elpais.com")
    print("Title of the page is:", driver.title)

    driver.quit()
