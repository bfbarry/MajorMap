import os
import urllib
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

def replace_all(unwanted, in_str):
    """
    Removes all instances of an unwanted string inside in_str
    """
    for i in unwanted:
        in_str = in_str.replace(i, '')
    return in_str

def extract_course_catalog(dept): #where dept is a string
    """
    Extracts course names and descriptions (including prerequisites) from downloaded
    course catalog page given department ID (string) using beautifulsoup
    """
    f = open('utils/sites/' + dept + '_courses.html') #dept is all caps
    soup = BeautifulSoup(f, 'html.parser')
    names = soup.find_all("p", {"class": "course-name"})
    descriptions = soup.find_all("p", {"class": "course-descriptions"}) #includes prereqs
    return names, descriptions
