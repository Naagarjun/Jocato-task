import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.failory.com/blog/top-indian-startups')

data = url.content
soup = BeautifulSoup(data, "lxml")
names = soup.find(
    'div', attrs={"class": "blog-rich-text w-richtext"}).find_all('h3')
comapny_name = []
about = []
founded = []
office_loc = []
total_found = []
for i in range(len(names)):
    comapny_name.append(names[i].text)
    nxt_about_p = names[i].find_next("p")
    about.append(nxt_about_p.text)
    found_p = nxt_about_p.find_next("p")
    founded.append(found_p.text)
    office_p = found_p.find_next('p')
    office_loc.append(office_p.text)
    total_funds_p = office_p.find_next("p")
    total_found.append(total_funds_p.text)
print(comapny_name)