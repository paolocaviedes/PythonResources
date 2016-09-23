from lxml import html
from bs4 import BeautifulSoup
import requests
from urllib2 import urlopen



def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")


def EscribirHTML(objetohtml):
	archivo=open("pagina.html","w")
	archivo.write(objetohtml)
	archivo.close()

#link=str(raw_input("ingrese URL: "))
soup = make_soup("http://consulta.servel.cl")
EscribirHTML(str(soup))

