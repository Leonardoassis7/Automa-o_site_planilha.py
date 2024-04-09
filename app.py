from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

driver = webdriver.Chrome()
driver.get('https://www.kabum.com.br/computadores/pc')


titulos = driver.find_elements(By.XPATH,"//a[@class='sc-61cda13b-14 jaEYHK']")

titulos = driver.find_elements(By.XPATH,"//strong[@class='sc-b1f5eb03-2 iaiQNF']")


workbook =  openpyxl.Workbook()
workbook.create_sheet('produtos')
sheet_produtos = workbook['produtos']
sheet_produtos['A1'].value = 'Produto'
sheet_produtos['B1'].value = 'Preço'



for titulo, preco in zip(titulos, precos):  #ele so prenchedados dados que estão ativo no site
    sheet_produtos.append([titulo,text,preco.text])
    pass   

workbook.save('produtos.xlsx')