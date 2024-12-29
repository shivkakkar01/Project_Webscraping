import threading
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from config import BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY, BROWSERSTACK_CONFIG


def run_test(config):
    """Run the test on a given BrowserStack configuration."""
    capabilities = config.copy()
    capabilities["browserstack.user"] = BROWSERSTACK_USERNAME
    capabilities["browserstack.key"] = BROWSERSTACK_ACCESS_KEY
    capabilities["name"] = "Web Scraping Test"

    driver = webdriver.Remote(
        command_executor="http://hub-cloud.browserstack.com/wd/hub",
        desired_capabilities=capabilities
    )

    try:
        # Example test: Visit El País and print the title
        driver.get("https://elpais.com")
        print(f"Title of the page on {capabilities.get('browser', capabilities.get('device'))}: {driver.title}")
    except Exception as e:
        print(f"Error in test with config {capabilities}: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    threads = []

    for config in BROWSERSTACK_CONFIG:
        thread = threading.Thread(target=run_test, args=(config,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All tests completed.")
