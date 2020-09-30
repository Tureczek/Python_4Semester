from markdownify import markdownify
import requests
from bs4 import BeautifulSoup

#url = 'https://clbokea.github.io/exam/assignment_2.html'
#page = requests.get(url)
#soup = BeautifulSoup(page.content, 'html.parser')
#html = markdownify(page)
req = requests.get('https://clbokea.github.io/exam/assignment_2.html', allow_redirects=True)

print(req)