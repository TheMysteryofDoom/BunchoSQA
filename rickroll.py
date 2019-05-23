from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.youtube.com")
search = driver.find_element_by_name("search_query")
search.clear()
search.send_keys("Rick Astley")
search.send_keys(Keys.RETURN)
video = driver.find_element_by_partial_link_text("never gonna give you up")
video.click()