from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from tkinter import Tk
import time


def breaker():
    """Função básica para dar tempo pro Selenium achar os dados"""
    time.sleep(0.5)


def searcher(path):
    """Define o caminho do chromedriver, retornando o browser.
    str -> driver"""

    return webdriver.Chrome(path)


def goUrl(driver, url):
    """Leva o chrome para uma determinada URL.
    driver, str"""

    driver.get(url)
   

def pesquisaYouTube(driver, url, nameBarPath, key, btnPath):
    """Fase 1, onde vai para o youtube e pesquisa um canal.
    driver, str, str, str, str"""

    goUrl(driver, url)
    searchBar = driver.find_element(By.NAME, nameBarPath)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, nameBarPath)))
    searchBar.send_keys(key)
    breaker()
    button = driver.find_element(By.ID, btnPath)
    button.click()


def entrandoCanal(driver, nomeDoCanal, namePath, canalPath):
    """Essa função faz um check se o canal que apareceu é o certo, e entra nele caso for.
    driver, str, str, str -> str"""

    driver.refresh()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, namePath)))
    breaker()
    channelName = driver.find_element(By.CSS_SELECTOR, namePath).get_attribute("textContent")
    if nomeDoCanal == channelName:
        link = driver.find_element(By.CSS_SELECTOR, canalPath).get_attribute("href")
        goUrl(driver, link)
    
    else:
        print("Canal diferente do pré-definido")

    return channelName