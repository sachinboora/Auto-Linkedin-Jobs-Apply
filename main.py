from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/sachin/PycharmProjects/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url="https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

email = driver.find_element(By.ID, "username")
email.send_keys("sboora765@gmail.com")

password = driver.find_element(By.ID, "password")
password.send_keys("tD:Cgqp.8yz7,N2")
password.submit()

save_jobs = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
save_jobs.click()

