from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Iniciando robô...\n")

driver = webdriver.Chrome('C:/Users/maiury.nascimento/Desktop/Robos/chromedriver')
driver.get("https://registro.br/")
time.sleep(2) #Dormir 2 segundos
driver.close()