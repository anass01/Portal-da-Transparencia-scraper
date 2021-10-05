import time

from selenium import webdriver

list=[]

driver = webdriver.Firefox()
driver.get("https://transparencia.registrocivil.org.br/registros")
time.sleep(2)
driver.find_element_by_xpath('//div[@id="__BVID__70"]/div').click()
time.sleep(3)
for element in driver.find_elements_by_xpath('//div[@id="__BVID__70"]/div//ul/li/span/span'):
     print(element.text)
     list.append(element.text)

print("states = [")
for line in list:
    print('"'+line+'",')
print(']')