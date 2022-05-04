from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Iniciando robô...\n")

driver = webdriver.Chrome('C:/Users/maiury.nascimento/Desktop/Robos/chromedriver')
driver.get("https://registro.br/")

dominios = ["roboscompython.com.br", "udemy.com","uol.com.br","pythoncursos.com"] # Domínio a ser pesquisado

for dominio in dominios:
    pesquisa = driver.find_element_by_id("is-avail-field") #Encontrar barra de pesquisa
    pesquisa.clear() # Limpar barra de pesquisa
    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.RETURN) # Enter
    time.sleep(2) #Dormindo
    resultados = driver.find_elements_by_tag_name("strong")

    #import pdb; pdb.set_trace() #Para o programa no meio da execução para interagir com o mesmo
    print("Domínio %s está %s" % (dominio, resultados[4].text)) # Dizer exatamente o domínio disponível.

#time.sleep(8) 
driver.close()