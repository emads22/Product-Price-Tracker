from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from app_utils import get_random_user_agent
from constants import CHROMEDRIVER_PATH


def chrome_web_driver(url, proxy=None):
    """
    Initialize a Chrome WebDriver instance and navigate to the specified URL.

    Args:
        url (str): The URL to navigate to.
        proxy (str, optional): The proxy address and port to use, if any. Defaults to None.

    Returns:
        webdriver.Chrome: An instance of Chrome WebDriver.

    Raises:
        WebDriverException: If an error occurs while initializing the WebDriver.
    """
    # Create a service object to manage the ChromeDriver server
    service = Service(executable_path=CHROMEDRIVER_PATH)

    # Configure ChromeOptions to customize Chrome WebDriver behavior
    options = webdriver.ChromeOptions()

    # # Disables infobars, such as "Chrome is being controlled by automated test software"
    # options.add_argument("disable-infobars")
    # # Maximizes the browser window on startup
    # options.add_argument("start-maximized")
    # # Disables the use of /dev/shm, which can cause Chrome to crash in some Linux environments
    # options.add_argument("disable-dev-shm-usage")
    # # Disables the sandbox mode, which can cause issues in some environments
    # # The sandbox in a web browser is an isolated environment that restricts the actions of web pages and their scripts to enhance security and prevent potential harm to the system.
    # options.add_argument("no-sandbox")
    # # Disables browser automation detection, preventing sites from detecting that WebDriver is being used
    # options.add_argument("disable-blink-features=AutomationControlled")
    # # Excludes the "enable-automation" switch, further preventing sites from detecting WebDriver
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # Altenatively, if we prefer Selenium not to open a browser window during execution we can remove all the arguments above and only apply this
    options.add_argument("--headless")

    # Set the user agent for the browser instance to a randomly chosen user agent string
    options.add_argument(f'user-agent={get_random_user_agent()}')

    # Check if a proxy is provided to be added
    if proxy:
        # Add the proxy server option to the browser options
        options.add_argument(f'--proxy-server={proxy}')

    try:
        # Initialize Chrome WebDriver with the configured service and options
        web_driver = webdriver.Chrome(service=service, options=options)
        # Navigate to the specified URL
        web_driver.get(url)

        return web_driver

    except WebDriverException as e:
        # If an error occurs during WebDriver initialization, raise an exception
        raise WebDriverException(
            f"\n--- Failed to initialize WebDriver: ---\n{e}\n\n")
