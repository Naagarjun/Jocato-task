from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

# Create your views here.
#default Home page
def index(request):
    return render(request, 'index.html')

#getting url from website
url = requests.get('https://www.failory.com/blog/top-indian-startups')

def home(request):
    data = url.content
    soup = BeautifulSoup(data, "lxml")
    names_1 = soup.select(
        "body > div.section-article > div:nth-child(4) > div:nth-child(9) > h3")
    names_2 = soup.select(
        "body > div.section-article > div:nth-child(4) > div:nth-child(5) > h3")
    comp_names = soup.select(
        "body > div.section-article > div:nth-child(4) > div:nth-child(1) > h3")
    names_2.extend(names_1)
    comp_names.extend(names_2)

    #Intialising empty list to sum-up the elenments
    company_name = []
    about = []
    founded = []
    office_locations = []
    total_funds = []

    for i in range(53):
        nxt_about_p = comp_names[i].find_next("p")  # About para parsing
        found_p = nxt_about_p.find_next("p")  # found para parsing
        office_p = found_p.find_next('p')  # office locations para parsing
        total_funds_p = office_p.find_next("p")  # total funds para parsing

        #Removing HTML tags and converting to text
        company_name.append(comp_names[i].text)
        about.append(nxt_about_p.text)
        founded.append(found_p.text)
        office_locations.append(office_p.text)
        total_funds.append(total_funds_p.text)

    final_data = zip(company_name, about, founded, office_locations, total_funds)
    return render(request, "home.html", context={'final_data':final_data})   
