import os
import urllib
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

def replace_all(unwanted, in_str):
    for i in unwanted:
        in_str = in_str.replace(i, '')
    return in_str

 #this beautifulsoups those catalogs from the folder
def extract_course_catalog(dept): #where dept is a string
    f = open('utils/sites/' + dept + '_courses.html') #dept is all caps     
    soup = BeautifulSoup(f, 'html.parser')
    names = soup.find_all("p", {"class": "course-name"})
    descriptions = soup.find_all("p", {"class": "course-descriptions"}) #includes prereqs
    return names, descriptions