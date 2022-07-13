import os
from selenium import webdriver
from bs4 import BeautifulSoup
import sqlite3

def replace_especial(string):     
    for i in range(len(string)):
        if not string[i].isdigit() and string[i] != ".":
            return string.replace("\xa0",".")
        if not string[i].isdigit() and string[i] == ".":
            return string.replace("\xa0"," ")

path = "C:/Users/Tiago/Documents/Python/Jogo das Bandeiras/chromedriver.exe"
pathdb = 'C:/Users/Tiago/Documents/Python/Jogo das Bandeiras/Bandeiras/'

filedb = 'bandeiras.db'
conn = sqlite3.connect(os.path.join(pathdb,filedb))
curseur = conn.cursor()

cmd = "SELECT Pais FROM Bandeiras"
curseur.execute(cmd)

lt_paises = []

for element in curseur.fetchall():
    lt_paises.append(element[0])

lt_pop = []
 

for pais in lt_paises:         
    try:    
     
      options = webdriver.ChromeOptions()
      options.add_argument('headless')
      driver = webdriver.Chrome(executable_path = path,options=options)
      
      url = "https://www.google.com.br/search?q="+str(pais)+"%20população&lr=lang_pt"

      driver.get(url)
          
      html = driver.page_source
      html_soup = BeautifulSoup(html, 'html.parser')
      pop_string = html_soup.find("div", class_ = 'ayqGOc kno-fb-ctx KBXm4e').get_text()

      pop = replace_especial(pop_string.split("(")[0].replace(",","."))
      censo = pop_string.split("(")[1].split(")")[0]
      
      pop_tuple = (pop,censo)      
      driver.close()
      
    except AttributeError:
        pop_tuple = (None,None)
    
    print(pop_tuple)
    lt_pop.append(pop_tuple)

for i in range(len(lt_paises)):
    
    pais = lt_paises[i]
    pop_tuple = lt_pop[i]
    
    cmd = "UPDATE Bandeiras SET Populacao='{}',Censo='{}' WHERE Pais='{}'".format(pop_tuple[0],pop_tuple[1],pais)
    curseur.execute(cmd)
    conn.commit()




