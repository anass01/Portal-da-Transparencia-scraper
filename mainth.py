import time
import csv
from selenium import webdriver
import threading
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

types=["birth","marriage","death"]
try:
    years = []

    while True:
        years.append(int(input("enter a year:")))
        print("enter empty line to start the program")
except:
    print(years)
months=[1,2,3,4,5,6,7,8,9,10,11,12]
states = [
"Acre",
"Alagoas",
"Amazonas",
"Amapá",
"Bahia",
"Ceará",
"Distrito Federal",
"Espírito Santo",
"Goiás",
"Maranhão",
"Minas Gerais",
"Mato Grosso do Sul",
"Mato Grosso",
"Pará",
"Paraíba",
"Pernambuco",
"Piauí",
"Paraná",
"Rio de Janeiro",
"Rio Grande do Norte",
"Rondônia",
"Roraima",
"Rio Grande do Sul",
"Santa Catarina",
"Sergipe",
"São Paulo",
"Tocantins",
]
csvfile = open('records.csv', 'w', encoding='utf8', newline='')
fnames = ['Tipo_Registro', 'Ano','Mes','Estado','Cidade','Qnt_Registros']
writer = csv.DictWriter(csvfile, fieldnames=fnames)
print("this will take time please wait...")
def work(year):
    csvfile = open('records'+str(year)+'.csv', 'w', encoding='utf8', newline='')
    fnames = ['Tipo_Registro', 'Ano', 'Mes', 'Estado', 'Cidade', 'Qnt_Registros']
    writer = csv.DictWriter(csvfile, fieldnames=fnames)
    driver = webdriver.Firefox()
    driver.get("https://transparencia.registrocivil.org.br/registros")
    for type in types:
        for month in months:
            for state in states:
                driver.find_element_by_xpath('//div[input[@value="'+type+'"]]').click()
                driver.find_element_by_xpath('//fieldset[@id="datePickrGroup"]/div').click()
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '//span[text()="'+str(year)+'"]')))
                driver.find_element_by_xpath('//span[text()="'+str(year)+'"]').click()
                driver.find_element_by_xpath('//fieldset[@id="__BVID__62"]/div').click()
                monthlist = driver.find_elements_by_xpath('//fieldset[@id="__BVID__62"]/div//ul/li/span/span')
                monthlist[month].click()

                driver.find_element_by_xpath('//div[@id="__BVID__70"]/div').click()
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//div[@id="__BVID__70"]/div//ul/li/span/span[text()="'+state+'"]')))

                driver.find_element_by_xpath('//div[@id="__BVID__70"]/div//ul/li/span/span[text()="'+state+'"]').click()

                try:
                    WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-success"]')))
                    driver.find_element_by_xpath('//button[@class="btn btn-success"]').click()
                except:
                    driver.find_element_by_xpath('//button[@class="btn btn-success"]').click()
                next = True
                while next:
                    WebDriverWait(driver, 60).until(EC.presence_of_element_located(
                        (By.XPATH, '//tbody/tr')))
                    rows = driver.find_elements_by_xpath('//tbody/tr')
                    for row in rows:
                        if type == "birth":
                            tipo = "Nascimentos"
                        if type == "marriage":
                            tipo = "Casamentos"
                        if type == "death":
                            tipo = "Óbitos"
                        city = row.find_elements_by_tag_name("td")[0].text
                        number =row.find_elements_by_tag_name("td")[1].text
                        writer.writerow({'Tipo_Registro': tipo, 'Ano': str(year),'Mes':str(month),'Estado':state,'Cidade':city,'Qnt_Registros':str(number)})
                    try:
                        driver.find_element_by_xpath('//ul[@role="menubar"]/li[last()-1]/button').click()
                    except:
                        next=False
    print(str(year)+" finish" )
threads=[]
for year in years:
    x = threading.Thread(target=work, args=(year,))
    threads.append(x)
for x in threads:
    x.start()

for x in threads:
    x.join()
print("finish")










#driver.find_element_by_xpath('//div[input[@value="birth"]]').click()

#driver.find_element_by_xpath('//fieldset[@id="datePickrGroup"]/div').click()
#//span[text()="2018"]

#driver.find_element_by_xpath('//fieldset[@id="__BVID__62"]/div').click()
#months = driver.find_elements_by_xpath('//fieldset[@id="__BVID__62"]/div//ul/li/span/span')
#months[5].click()

#driver.find_element_by_xpath('//div[@id="__BVID__70"]/div').click()
#//div[@id="__BVID__70"]/div//ul/li/span/span[text()="Rio de Janeiro"]

#//tbody/tr

#//button[@class="btn btn-success"]

#driver.find_element_by_xpath('//ul[@role="menubar"]/li[last()-1]/button').click()


