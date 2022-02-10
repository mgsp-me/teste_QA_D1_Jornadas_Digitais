from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from tkinter import Tk
import helper
import os
import platform

def selecionarVideo(driver, videoPath, allVideosPath, n):
    """Sua função é ir até 'vídeos' e selecionar um vídeo.
    driver, str, str, int
    """

    WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.CSS_SELECTOR, videoPath)))
    helper.breaker()
    for element in driver.find_elements(By.CSS_SELECTOR, videoPath):
        if "Videos" in str(element.get_attribute("textContent")):
            element.click()

    helper.breaker()
    videoLink = (driver.find_elements(By.CSS_SELECTOR, allVideosPath))[n]
    videoLink.click()

def compartilhar(driver, sharePath, copyPath, whatsappPath, nomePlataforma):
    """Função que coleta o link de um vídeo e valida se o nome 'whatsapp' está entre as opções de compartilhar.
    driver, str, str, int
    """

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, sharePath)))
    helper.breaker()

    driver.find_element(By.CSS_SELECTOR, sharePath).click()
    helper.breaker()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, copyPath)))
    str(driver.find_element(By.CSS_SELECTOR, copyPath).click())
    link = Tk().clipboard_get()

    for element in driver.find_elements(By.CSS_SELECTOR, whatsappPath):
        elementName = element.get_attribute("textContent")
        if nomePlataforma == elementName:
            print(f"Validado, é o {nomePlataforma}")
    
    return link


if "Linux" in platform.platform():
    driver = helper.searcher('src/chromedriver')

else:
    path_windows = os.path.dirname(os.path.abspath(file)) + '\ChromedriverW\chromedriver.exe'
    driver = helper.searcher(path_windows)


# Fase 1, navegação (já daria para fazer a extração dos dados aqui)
helper.pesquisaYouTube(driver, "http://www.youtube.com", "search_query",
"D1 - Jornadas Digitais","search-icon-legacy")


# Fase 2, Validação
helper.entrandoCanal(driver, "D1 - Jornadas Digitais", "div#text-container > yt-formatted-string#text",
"div#avatar-section.style-scope.ytd-channel-renderer > a")


# Fase 3, Selecionando vídeo
selecionarVideo(driver, "tp-yt-paper-tab.style-scope.ytd-c4-tabbed-header-renderer > div.tab-content.style-scope.tp-yt-paper-tab",
"div#details.style-scope.ytd-grid-video-renderer", 2)


# Fase 4, Pegar link
link = compartilhar(driver, "ytd-button-renderer.style-scope.ytd-menu-renderer.force-icon-button.style-default.size-default",
"yt-button-renderer#copy-button.style-scope.yt-copy-link-renderer.style-text.size-default",
"div#title.style-scope.yt-share-target-renderer" , "WhatsApp")


# Fase 5, Printar link
print(link)
