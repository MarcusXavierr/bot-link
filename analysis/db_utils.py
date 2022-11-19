from dataclasses import dataclass
from json import loads
import re


@dataclass
class JobData:
    job_id: str
    title: str
    description: str
    company_name: str
    company_size: str
    company_url: str
    location: str
    workplace: str
    appliants: int
    level: str


def parse_data(data: dict) -> JobData:
    company_size = get_company_size(data.get('other_info', []))
    appliants = int(list(filter(str.isdigit, data.get('appliants', '0'))).pop())

    return JobData(
        data['id'],
        data['title'],
        data['description'],
        company_size,
        data['company_url'],
        data.get('company_name', 'sei lá'),
        data.get('location', 'Brazil'),
        data.get('workplace', 'Remote'),
        appliants,
        data.get('level', 'Não interessa')
    )


def get_company_size(other_info: list) -> str:
    pattern = re.compile(r'[0-9].*-[0-9].*[a-z]')
    test = lambda xs: re.fullmatch(pattern, xs)
    results = list(filter(test, other_info))
    if len(results) > 0:
        return results.pop()
    return '0, deu ruim meu chapa'


def parse_file(name: str) -> list[dict]:
    with open(name) as f:
        line = f.readline()
        return loads(line)


INSERT_QUERY = '''
        INSERT INTO jobs (
        job_id, title, description, company_name, company_size,
        company_url, location, workplace, appliantas, level
        )
        VALUES
        (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
