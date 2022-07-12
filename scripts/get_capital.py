import os
from selenium import webdriver
from bs4 import BeautifulSoup
import sqlite3

path = "C:/Users/Tiago/Documents/Python/Jogo Bandeiras/chromedriver.exe"
pathdb = 'C:/Users/Tiago/Documents/Python/Jogo Bandeiras/Bandeiras/'

filedb = 'bandeiras.db'
conn = sqlite3.connect(os.path.join(pathdb,filedb))
curseur = conn.cursor()

cmd = "SELECT Pais FROM Bandeiras"
curseur.execute(cmd)

lt_paises = []

for element in curseur.fetchall():
    lt_paises.append(element[0])

lt_capitais = []

for pais in lt_paises:         
    try:    
        driver = webdriver.Chrome(executable_path = path)
        url = "https://www.google.com.br/search?q="+str(pais)+"%20capital&lr=lang_pt"
        
        driver.get(url)
                
        html = driver.page_source
        html_soup = BeautifulSoup(html, 'html.parser')
        capital = html_soup.find("a", class_ = 'FLP8od').get_text()
        driver.close()
    
    except AttributeError:
        capital = None
    
    print(capital)
    lt_capitais.append(capital)

for i in range(len(lt_paises)):
    
    pais = lt_paises[i]
    capital = lt_capitais[i]
    
    cmd = "UPDATE Bandeiras SET Capital='{}' WHERE Pais='{}'".format(capital,pais)
    curseur.execute(cmd)
    conn.commit()