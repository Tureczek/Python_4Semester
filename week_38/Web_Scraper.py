import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='SearchResults')

job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before
    python_jobs = results.find_all('h2', string=lambda text: 'develop' in text.lower())
    for p_job in python_jobs:
        link = p_job.find('a')['href']
        print(p_job.text.strip())
        print(f'Apply here: {link}\n')
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if title_elem is not None:
        print("Title : ", title_elem.text.strip())
    if company_elem is not None:
        print("Company : ", company_elem.text.strip())
    if location_elem is not None:
        print("Location : ", location_elem.text.strip())
    print('\n')
    print(len(python_jobs))
