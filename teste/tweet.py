from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Acessa o chromedriver e abre o twitter
PATH = "/home/daniel/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://twitter.com/home")
time.sleep(3)

# Encontra as caixas de login e senha e os envia
login = driver.find_element_by_name("session[username_or_email]")
login.send_keys("Insira seu e-mail")
password = driver.find_element_by_name("session[password]")
password.send_keys("Insira sua senha")
password.send_keys(Keys.RETURN)

# Encontra a caixa e escreve um tweet
tweet = driver.find_element_by_css_selector(".public-DraftStyleDefault-block")
tweet.send_keys("Agora sim deu certo o tweet automatizado")
time.sleep(2)

# Tenta encontrar o botão de tweetar
try:
    button = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-1qd0xha r-a023e6 r-vw2c0b r-1777fci r-eljoum r-dnmrzs r-bcqeeo r-q4m81j r-qvutc0'))
    )
    button.click()
except:
    time.sleep(2)
    print("Não foi possível encontrar o botão")



