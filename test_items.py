import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket_button(browser):
    browser.get(link)
    time.sleep(10)
    basket_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(basket_button) != 0, "Button missing!"