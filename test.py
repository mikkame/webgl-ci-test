import unittest
import os
import chromedriver_binary
from selenium import webdriver


FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screen.png")

driver = webdriver.Chrome()
driver.get("https://webglsamples.org/aquarium/aquarium.html")

driver.save_screenshot(FILENAME)

driver.quit()
