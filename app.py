from time import sleep
from random import randint
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from file import File
from utils import scrape_jobs, create_url

from job import Job

driver = Chrome()


def main():
    driver.get('https://www.linkedin.com/')
    scrappe_name = input('Digite o nome do seu scrappe meu parça: ')
    driver.get('https://www.linkedin.com/jobs/')
    input('Primeiro monte a sua busca meu patrão')
    file = File(f'./data_{scrappe_name}')
    print('arquivo montando, bora lá')
    for page in range(40):
        print(f'indo scrappar a pagina {page + 1}')
        go_to_page(page)
        write_file(file)


def write_file(file: File):
    file.append_item(work())


def go_to_page(page):
    current_url = driver.current_url
    new_url = create_url(current_url, page)
    driver.get(new_url)
    sleep(randint(3, 6))


def work():
    info = []
    jobs = scrape_jobs(driver)
    for job in jobs:
        try:
            info.append(scrape_data(job))
            print('job scrapado com sucesso')
        except Exception:
            print('deu ruim meu patrão')
            continue
    return info


def scrape_data(job: WebElement) -> dict:
    job.click()
    sleep(randint(4, 7))
    jobPost = Job(job.get_attribute('data-job-id'), driver)
    return jobPost.get_info()


main()
