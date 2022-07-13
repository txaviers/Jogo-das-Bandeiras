import os
from bs4 import BeautifulSoup as bs
import requests
import sqlite3

path = 'C:/Users/Tiago/Documents/Python/Jogo das Bandeiras/Bandeiras/'

filedb = 'bandeiras.db'
conn = sqlite3.connect(os.path.join(path,filedb))
curseur = conn.cursor()

cmd = "SELECT Pais FROM Bandeiras"
curseur.execute(cmd)

lt_paises = []

for element in curseur.fetchall():
    lt_paises.append(element[0])

# lt_moeda = []

# for pais in lt_paises:
        
#     try:        
#         wikiurl="https://pt.wikipedia.org/wiki/" + str(pais)
        
#         response = requests.get(wikiurl)
            
#         soup = bs(response.text, 'html.parser')
#         a_string = soup.find(string="Moeda")
#         capital = a_string.find_next("td")
        
#         moeda_tag = capital.findChildren('a')
        
#         moeda = moeda_tag[0].get_text()+" e "+moeda_tag[2].get_text() if len(moeda_tag)>2 else moeda_tag[0].get_text()
           
#     except AttributeError:
#         moeda = None
#     except IndexError:
#         moeda = None
        
#     print(moeda)
#     lt_moeda.append(moeda)

for i in range(len(lt_paises)):
    
    pais = lt_paises[i]
    moeda = lt_moeda[i]
    
    cmd = "UPDATE Bandeiras SET Moeda='{}' WHERE Pais='{}'".format(moeda,pais)
    curseur.execute(cmd)
    conn.commit()