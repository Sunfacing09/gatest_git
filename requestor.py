# import requests
import random
import time

# response = requests.get('https://sunfacing09.github.io/gatest/')


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://sunfacing09.github.io/gatest/") # 更改網址以前往不同網頁

for i in range(20):
    driver.get("https://sunfacing09.github.io/gatest/") # 更改網址以前往不同網頁

    interval = random.randint(1, 6)
    print('===== Pause for %s =====' % (interval,))
    time.sleep(interval)



