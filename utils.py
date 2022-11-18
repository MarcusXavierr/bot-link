from random import randint
import re
from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def scrape_jobs(driver: WebDriver) -> list[WebElement]:
    sleep(randint(5, 10))
    scroll_until_end(driver)
    return get_jobs(driver)


def scroll_until_end(driver: WebDriver):
    scroll_page(driver, 4)
    scroll_page(driver, 3)
    scroll_page(driver, 2)
    scroll_page(driver, 1)


def get_jobs(driver: WebDriver):
    return driver.find_elements(By.CSS_SELECTOR, '.scaffold-layout__list-container>li>div>div.job-card-container')


def scroll_page(driver: WebDriver, part_of_page: int):
    if part_of_page != 0:
        driver.execute_script(f"document.querySelector('.jobs-search-results-list').scroll(0, document.querySelector('.jobs-search-results-list').scrollHeight / {part_of_page})")
        sleep(randint(2, 5))


def create_url(url: str, next_page: int) -> str:
    if next_page < 1:
        return url + f'&start={next_page * 25}'
    return re.sub('start=[0-9][0-9]?[0-9]?', f'start={next_page * 25 + 1}', url)
