from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

start_url = 'https://google.com'

driver = webdriver.Chrome()
driver.get(start_url)
driver.maximize_window()
banner = input('Нажми для продолжения...')

with open('list_domain.txt', 'r') as file:
	domains = file.readlines()
	for domain in domains:
		print(f'\n{domain}')
		driver.get(start_url)
		enter_search = driver.find_element(By.TAG_NAME, 'textarea')
		enter_search.send_keys(f'site:linkedin.com/in intext:{domain}')
		#enter_search.send_keys(Keys.ENTER)
		time.sleep(2)

		num=0
		while num < 5:
			num+=1
			time.sleep(1)
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			# print(f'Проскроллил {num} раз')

		links = driver.find_elements(By.TAG_NAME, 'h3')
		for link in links:
			name_company = (link.text)
			print(name_company)
			with open('result_1.txt', 'a+') as file:
				if name_company != 'Ещё результаты':
					file.write(f'{name_company}\n')



		time.sleep(3)
