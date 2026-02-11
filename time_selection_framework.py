import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TimeKeeperPage:

    URL = "https://mike-borges.github.io/TimeKeeper/"

    # Locators
    TIMER_OPTIONS = (By.CSS_SELECTOR, "button")
    START_BUTTON = (By.XPATH, "//button[contains(text(),'Start')]")
    ACTIVE_TIMER = (By.CSS_SELECTOR, ".active")
    TIMER_DISPLAY = (By.CSS_SELECTOR, "h1")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def get_timer_buttons(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(self.TIMER_OPTIONS)
        )

    def get_timer_texts(self):
        buttons = self.get_timer_buttons()
        return [btn.text for btn in buttons if ":" in btn.text]

    def is_timer_visible_and_clickable(self, time_value):
        locator = (By.XPATH, f"//button[contains(text(),'{time_value}')]")
        button = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        return button.is_displayed()

    def select_timer(self, time_value):
        locator = (By.XPATH, f"//button[contains(text(),'{time_value}')]")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_active_timer(self):
        active = self.wait.until(
            EC.presence_of_element_located(self.ACTIVE_TIMER)
        )
        return active.text

    def click_start(self):
        self.wait.until(
            EC.element_to_be_clickable(self.START_BUTTON)
        ).click()

    def get_current_url(self):
        return self.driver.current_url

    def get_displayed_time(self):
        return self.wait.until(
            EC.presence_of_element_located(self.TIMER_DISPLAY)
        ).text
