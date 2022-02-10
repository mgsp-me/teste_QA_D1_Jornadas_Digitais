from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import helper
import os
import platform

def recolhendoDados(driver, aboutPath, subsPath):
    """recolhendoDados é a responsável por coletar os dados.
    driver, str, str -> str
    """

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, aboutPath)))
    for element in driver.find_elements(By.CSS_SELECTOR, aboutPath):
        if "About" in str(element.get_attribute("textContent")):
            element.click()

    nSubscribers = driver.find_element(By.CSS_SELECTOR, subsPath).get_attribute("textContent")

    return nSubscribers


if "Linux" in platform.platform():
    driver = helper.searcher('src/chromedriver')

else:
    path_windows = os.path.dirname(os.path.abspath(__file__)) + '\ChromedriverW\chromedriver.exe'
    driver = helper.searcher(path_windows)


# Fase 1, navegação (já daria para fazer a extração dos dados aqui)
helper.pesquisaYouTube(driver, "http://www.youtube.com", "search_query",
"D1 - Jornadas Digitais", "search-icon-legacy")


# Fase 2, Validação
nomeCanal = helper.entrandoCanal(driver, "D1 - Jornadas Digitais", "div#text-container > yt-formatted-string#text",
"div#avatar-section.style-scope.ytd-channel-renderer > a")


# Fase 3, coletando dados
nInscritos = recolhendoDados(driver, "tp-yt-paper-tab.style-scope.ytd-c4-tabbed-header-renderer > div.tab-content.style-scope.tp-yt-paper-tab",
"yt-formatted-string#subscriber-count")


# Fazendo o print e fechando o driver
print(f"O nome do canal é {nomeCanal} e ele têm {nInscritos}")
driver.quit()