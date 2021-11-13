import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

chrome_driver_path = {DRIVER_PATH}
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=web%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

time.sleep(2)
sign_in = driver.find_element_by_link_text("Sign in")
sign_in.click()

time.sleep(5)
username = driver.find_element_by_id("username")
username.send_keys(USERNAME)

password = driver.find_element_by_id("password")
password.send_keys(PASSWORD)

password.send_keys(Keys.ENTER)

time.sleep(5)
jobs = driver.find_elements_by_class_name("job-card-list__title")
for job in jobs:
    job.click()
    time.sleep(2)

    try:
        apply = driver.find_element_by_class_name("jobs-apply-button--top-card")
        apply.click()
        time.sleep(5)

        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone == "":
            phone.send_keys(MOB.NO.)

        submit_button = driver.find_element_by_css_selector("footer button")

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close.click()
            time.sleep(2)
            discard = driver.find_element_by_css_selector(".artdeco-modal__actionbar .artdeco-button--primary")
            discard.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(4)
        close_button = driver.find_element_by_css_selector("div .artdeco-button--tertiary")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()



