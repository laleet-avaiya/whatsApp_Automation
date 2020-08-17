from selenium import webdriver
import pandas as pd
# import pickle
import time

df = pd.read_csv('number.csv')

chrome_path = "chromedriver"

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome(chrome_path, options=options)

message = "\
If you Download and Register on this App we will get Rupee 10. \
We use this amount to help needy people. \
Thanks. \
This message is sent by bot  \
App Link : https://rapidbox.in/s/R222642D2 \
"

url = 'https://web.whatsapp.com'
driver.get(url)

time.sleep(20)
working = open("working.csv", "a")

for i in range(0, len(df['Contacts'])):
    send_to = str(df['Contacts'][i])
    execu = '''
    var link = document.createElement('a');
    link.href = 'https://web.whatsapp.com/send?phone={}&text={}';
    document.body.appendChild(link);
    link.click();  
    '''.format(send_to, message)

    driver.execute_script(execu)
    try:
        time.sleep(1)
        send_button = driver.find_elements_by_css_selector("div._1JNuk")[-1]
        time.sleep(1)
        send_button.click()
        working.write(send_to + "\n")
    except:
        time.sleep(1)
        ok_button = driver.find_elements_by_css_selector("div.S7_rT.FV2Qy")[-1]
        time.sleep(1)
        ok_button.click()
    time.sleep(3)
working.close()
driver.close()