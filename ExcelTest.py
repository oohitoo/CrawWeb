import openpyxl
from selenium import webdriver

driver = webdriver.Chrome('D:\chromedriver')

# 확인하기 위한 print문
print('드라이버 확인')

#크롤링 할 주소 (url)
# get함수 사용
link = driver.get('https://docs.google.com/spreadsheets/d/15_wzTM3IZM3v42gQJ-byIEhieTwn71zE56Jeo4VE9XU/edit?usp=sharing')

wb = openpyxl.load_workbook()


