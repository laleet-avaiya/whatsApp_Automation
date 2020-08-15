from selenium import webdriver
import pandas as pd
# import pickle
import time

df = pd.read_csv('number.csv')

chrome_path = "chromedriver"

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome(chrome_path, options=options)

message = "https://rapidbox.in/s/R222642D2"

url = 'https://web.whatsapp.com'
driver.get(url)

time.sleep(20)
for i in range(0, len(df['Contacts'])):
    send_to = str(df['Contacts'][i])
    execu = '''
    var link = document.createElement('a');
    link.href = 'https://web.whatsapp.com/send?phone={}&text={}';
    document.body.appendChild(link);
    link.click();  
    '''.format(send_to, message)

    driver.execute_script(execu)
    # message_box = driver.find_elements_by_css_selector("div._2S1VP.copyable-text.selectable-text")
    # message_box[-1].send_keys(message)
    time.sleep(1)
    send_button = driver.find_elements_by_css_selector("div._1JNuk")[-1]
    send_button.click()
    time.sleep(4)

driver.close()