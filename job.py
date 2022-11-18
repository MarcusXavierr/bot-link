from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Job:
    def __init__(self, id, driver: WebDriver):
        self.id = id
        self.driver = driver
        self.page = 'section.scaffold-layout__detail'

    def get_info(self) -> dict:
        info = {
            'id': self.id,
            'title': self._get_title(),
            'description': self._get_job_description(),
        }
        info.update(self._get_metadata())
        return info

    def _get_title(self) -> str:
        return self._search('h2.jobs-unified-top-card__job-title').text

    def _get_metadata(self) -> dict:
        metadata = '.jobs-unified-top-card__primary-description'
        company = self._search(f'{metadata} span.jobs-unified-top-card__company-name>a')
        location = self._search(f'{metadata} .jobs-unified-top-card__bullet')
        workplace = self._search(f'{metadata} .jobs-unified-top-card__workplace-type')
        appliants = self._get_appliants(metadata)
        other_info = self._get_other_info()
        return {
            'company_name': company.text,
            'company_url': company.get_attribute('href'),
            'location': location.text,
            'workplace': workplace.text,
            'appliants': appliants,
            'other_info': other_info,
        }

    def _get_appliants(self, metadata: str) -> str:
        try:
            return self._search(f'{metadata} .jobs-unified-top-card__applicant-count').text
        except Exception:
            return '0, pois deu errado'

    def _get_other_info(self) -> list:
        try:
            info = self.driver.find_elements(By.CSS_SELECTOR, f'{self.page} ul>li.jobs-unified-top-card__job-insight')
            return list(map(lambda x: x.text, info))
        except Exception:
            return []

    def _get_job_description(self) -> str:
        return self._search('.jobs-description-content__text').text

    def _search(self, selector: str) -> WebElement:
        return self.driver.find_element(By.CSS_SELECTOR, f'{self.page} {selector}')
