from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Funcionalidades do webdriver e definições iniciais
PATH = "/home/daniel/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://onepiece.fandom.com/pt/wiki/Arco_Romance_Dawn")
linkAtual = driver.current_url
numeroDeArcos = 4

# O XPATH da primeira página é diferente do restante
XPath1 = '/html/body/div[3]/section/div[2]/article/div/div[1]/div[2]/aside/section[2]/table/tbody/tr/td/a'
XPath2 = '/html/body/div[3]/section/div[2]/article/div/div[1]/div[2]/aside/section[2]/table/tbody/tr/td[2]/a'

# Funcionalidades de cada página

def encontrarSinopsedoArco(linkAtual):
    textoDaPagina = requests.get(linkAtual).text
    soup = BeautifulSoup(textoDaPagina,'lxml')
    sinopseDoArco = soup.p

    if len(sinopseDoArco.text) < 30:
        sinopseDoArco = sinopseDoArco.find_next('p').text
    else:
        sinopseDoArco = soup.p.text

    return sinopseDoArco

def escreverConteudoDoArco(linkAtual):
    print(driver.title)
    arquivo = open("onepiece.txt", "a")
    arquivo.write("\n" + driver.title + "\n" + encontrarSinopsedoArco(driver.current_url) + "\n")

def acharProximoArco (arcoAtual):

    if (arcoAtual == 0):
        proximoArco = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, XPath1))
        )
    else:
        proximoArco = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, XPath2))
        )
    return proximoArco

def clicarNoProximoArco(arcoAtual):
    try:
        driver.execute_script("window.scrollTo(0, 800)")
        acharProximoArco(arcoAtual).click()
    except:
        driver.execute_script("window.scrollTo(0, 300)")
        acharProximoArco(arcoAtual).click()

for arco in range(numeroDeArcos):

    try:
        print("Este é o arco " + str(arco + 1))
        escreverConteudoDoArco(linkAtual)
        if (arco < numeroDeArcos - 1):
            acharProximoArco(arco)
            clicarNoProximoArco(arco)
        time.sleep(2)
    except:
        print("Ocorreu um erro")
        driver.quit()

driver.quit()
