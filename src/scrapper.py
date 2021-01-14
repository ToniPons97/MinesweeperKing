import os, pyperclip
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.action_chains import ActionChains

from process_game_data import decode_game_state

def command_c():
    action = ActionChains(browser)
    action.key_down(Keys.COMMAND)
    action.send_keys('c')
    action.key_up(Keys.COMMAND).perform()

def rightClick(elem):
    action = ActionChains(browser)
    action.context_click(elem).perform()
 
load_dotenv()

cap = webdriver.DesiredCapabilities().CHROME
cap["marionette"] = False

browser = webdriver.Chrome(desired_capabilities=cap, executable_path=os.getenv("DRIVER"))
browser.get("http://minesweeperonline.com/")
browser.find_element_by_id("export-link").click()

command_c()
state_data = pyperclip.paste()

browser.find_element_by_id("export-close").click()
mine_coords = decode_game_state(state_data)

for i, j in enumerate(mine_coords):
    square = browser.find_element_by_id(f"{j[0]}_{j[1]}")
    rightClick(square)