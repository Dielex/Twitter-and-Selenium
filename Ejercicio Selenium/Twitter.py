from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://twitter.com/")

driver.find_element_by_css_selector(".StreamsHero-buttonContainer .Button.StreamsLogin").click()

usuario = driver.find_element_by_name("session[username_or_email]")
usuario.send_keys("dielex_117@hotmail.com")

clave = driver.find_element_by_name("session[password]")
clave.send_keys("dielex117")

driver.find_element_by_css_selector(".submit").click()

#driver.find_element_by_css_selector(".tweet-btn").click()

tweet = driver.find_element_by_id('tweet-box-home-timeline')
tweet.send_keys("Im using Selenium!!")

driver.find_element_by_css_selector("button.tweet-action").click()



