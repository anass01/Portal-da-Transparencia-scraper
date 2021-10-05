import time
import csv
from selenium import webdriver



driver = webdriver.Firefox()
driver.get("https://transparencia.registrocivil.org.br/registros")

types=["birth","marriage","death"]
years=[2019,2018,2017,2016,2015]
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

for type in types:
    for year in years:
        for month in months:
            for state in states:
                driver.find_element_by_xpath('//div[input[@value="'+type+'"]]').click()
                driver.find_element_by_xpath('//fieldset[@id="datePickrGroup"]/div').click()
                driver.find_element_by_xpath('//span[text()="'+str(year)+'"]').click()
                driver.find_element_by_xpath('//fieldset[@id="__BVID__62"]/div').click()
                monthlist = driver.find_elements_by_xpath('//fieldset[@id="__BVID__62"]/div//ul/li/span/span')
                monthlist[month].click()
                driver.find_element_by_xpath('//div[@id="__BVID__70"]/div').click()
                driver.find_element_by_xpath('//div[@id="__BVID__70"]/div//ul/li/span/span[text()="'+state+'"]').click()
                time.sleep(0.250)
                driver.find_element_by_xpath('//button[@class="btn btn-success"]').click()
                time.sleep(0.250)
                next = True
                while next:
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


