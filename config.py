# Configuration file for settings

# URLs
BASE_URL = "https://elpais.com/"
OPINION_SECTION_URL = f"{BASE_URL}/opinion"

# BrowserStack credentials
BROWSERSTACK_USERNAME = "shiv_PptY4j"
BROWSERSTACK_ACCESS_KEY = "Mv3yyvYZojvobjdzVewH"
BROWSERSTACK_CONFIG = [
    {
        "browser": "Chrome",
        "browser_version": "latest",
        "os": "Windows",
        "os_version": "10",
    },
    {
        "browser": "Firefox",
        "browser_version": "latest",
        "os": "Windows",
        "os_version": "10",
    },
    {
        "browser": "Safari",
        "browser_version": "latest",
        "os": "OS X",
        "os_version": "Ventura",
    },
    {
        "device": "iPhone 14",
        "os_version": "16",
        "real_mobile": "true",
    },
    {
        "device": "Samsung Galaxy S22",
        "os_version": "12.0",
        "real_mobile": "true",
    }
]
GOOGLE_TRANSLATE_API_KEY = None

# File paths
DOWNLOADS_FOLDER = "downloads/"
