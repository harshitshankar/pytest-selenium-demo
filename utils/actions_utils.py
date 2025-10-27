# utils/actions_utils.py
from selenium.webdriver import ActionChains

def hover_and_click(driver, element_to_hover, element_to_click):
    actions = ActionChains(driver)
    actions.move_to_element(element_to_hover).click(element_to_click).perform()
