import requests
from bs4 import BeautifulSoup

URL = 'https://www.jobindex.dk/jobsoegning/storkoebenhavn?q=software'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='results')

job_elems = results.find_all('div', class_='PaidJob')
print(' ')


for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('b')
    location_elem = job_elem.find('p')
    description_elem = job_elem.find('i')
    furtherdescription_elem = job_elem.find('p')

    #Finding the link
    link = job_elem.findAll('a')
    link = str(link)
    #placement = link.find('href', link.find('href')+1)+6
    #placement = placement+6
    link = link[link.find('href', link.find('href')+1)+6:]
#    print(placement)
#    print(link.find('rel', link.find('rel')))
    placement2 = link.find('rel', link.find('rel'))



    if title_elem is not None:
        print('Titel: '+title_elem.text.strip())
    if location_elem is not None:
        print('Lokation: '+location_elem.text.strip())
    if description_elem is not None:
        print('Beskrivelse: '+description_elem.text.strip())
    print(link[:placement2 - 2])
    print('')