from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/home/daniel/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com/")
search = driver.find_element_by_css_selector(".gLFyf")
time.sleep(1)
search.send_keys("Meu doce de leite")
search.send_keys(Keys.RETURN)
time.sleep(5)
print("voce acabou de acessar " + driver.title)
driver.quit()




"""
driver.close() fecha a aba atual
driver.quit()  fecha a janela inteira
"""


