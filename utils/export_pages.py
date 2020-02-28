import os
import urllib
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

#From https://stackoverflow.com/questions/13332192/inherent-way-to-save-web-page-source
# This puts all the course catalog webpages into a folder 'sites'



depts = ['ANTH','BIOI','BIOL','CHEM','CHIN','CLAS','CCS','COGS','COMM','CGS','CAT','DSC','DSGN','DOC','ECON','EDS','ENG','BENG','CSE','ECE','MAE','NANO','SE','ENVR','ESYS','ETHN','FMPH','FILM','GLBH','HIST','HDS','HR','HUM','INTL','JAPN','JWSP','LATI','LAWS','LING','LIT','MGT','MATH','MUS','PHIL','PHYS','POLI','PSYC','RELI','SCIS','SIO','SOC','THEA','TWS','USP','VIS']


dirName = 'sites'
if not os.path.exists(dirName):
	os.mkdir(dirName)

for dept in depts:
    url =  'https://www.ucsd.edu/catalog/courses/' + dept + '.html'
    page = urllib.request.urlopen(url)
    page_content = page.read()
    with open('sites/' + dept + '_courses.html', 'wb') as fid:
        fid.write(page_content)



 #this beautifulsoups those catalogs from the folder
def extract_course_catalog(dept): #where dept is a string
    f = open('/sites' + dept + '_courses.html') #dept is all caps     
    soup = BeautifulSoup(f, 'html.parser')