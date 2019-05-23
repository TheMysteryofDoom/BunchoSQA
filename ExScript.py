from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://jaikun12.github.io/simple-task-app/")

tasks = ["Rage at Python Script","Switch Code Editor","Improve Script","Rage at script again","Think why I failed...","Fail to do this and get angry again","Relearn Python","Optimize Code","Finish Task","Have task checked"]

elem = driver.find_element_by_id("task-input")
i = 0
name = ""
for task in tasks:
    i += 1
    name = "enput-" +str(i)+ ".png"
    elem.clear()
    elem.send_keys(task)
    driver.save_screenshot(name)
    elem.send_keys(Keys.RETURN)

driver.save_screenshot('finaloutput.png')
items = driver.find_elements_by_tag_name("li")
print(len(items), " tasks")

assert "No results found." not in driver.page_source
