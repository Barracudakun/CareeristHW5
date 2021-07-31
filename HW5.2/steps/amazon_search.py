from behave import *
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


@given('Open Amazon product page')
def open_amazon_product_page(context):
    context.driver = webdriver.Chrome('/Users/seashore/Dropbox/My Mac (MacBook-Air.lan)/Downloads/chromedriver')
    context.driver.get('https://www.amazon.com/dp/B081YS2F7N')
    context.driver.implicitly_wait(10)


@then('Verify user can click through colors')
def verify_user_click_product_color(context):
    expected_colors = ['Black', 'Blue', 'Burgundy', 'Caramel', 'Gray', 'Green', 'Khaki',
                       'Pink', 'White', 'Yellow', 'Light Green']
    color_selections = context.driver.find_elements(By.CSS_SELECTOR, '#variation_color_name li')
    sleep(5)

    for i in range(len(color_selections)):
        color_selections[i].click()
        actual_text = context.driver.find_element(By.CSS_SELECTOR, '#variation_color_name span').text
        sleep(5)
        assert actual_text == expected_colors[i], f'Error, color is {actual_text}, but expected{expected_colors[i]}'



