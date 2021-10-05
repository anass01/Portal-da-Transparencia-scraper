import csv

csvfile = open('records.csv', 'w', encoding='utf8', newline='')
fnames = ['Tipo_Registro', 'Ano','Mes','Estado','Cidade','Qnt_Registros']
writer = csv.DictWriter(csvfile, fieldnames=fnames)
writer.writeheader()
csvfile.flush()
years=[2020,2019,2018,2017,2016,2015]
for year in years:
    for line in open("records"+str(year)+".csv","r",encoding='utf8'):
        csvfile.write(line)
        csvfile.flush()
