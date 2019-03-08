from selenium import webdriver
import datetime


f = open('D:\학교자료/가격정보.txt', 'a')

# 드라이버 = D드라이브, 크롬드라이브잡아주기
driver = webdriver.Chrome('D:\chromedriver')

# 확인하기 위한 print문
print('드라이버 확인 ')

#크롤링 할 주소 (url)
# get함수 사용
driver.get('http://search.danawa.com/dsearch.php?k1=gtx1660ti')

driver.implicitly_wait(5)


now = datetime.datetime.now()
datatime = now.strftime('%Y-%m-%d %H:%M:%S')

print("==========",datatime,"==========")

f.write(datatime)
f.write("\n")
data = ""
for i in range(1,15):
  search = driver.find_element_by_xpath('//*[@id="productListArea"]/div[3]/ul/li[%d]' % i).text.split('\n')

  if len(search)-1 == 9:
      data = search[0], "\t",search[9].replace("가격정보 더보기",""), "\n"
      w =(''.join(data))
      f.write(w)
  elif len(search)-1 == 8:
      data = search[0], "\t",search[8].replace("가격정보 더보기",""),"\n"
      w =(''.join(data))
      f.write(w)
  elif len(search)-1 == 7:
      data = search[0], "\t",search[7].replace("가격정보 더보기",""),"\n"
      w =(''.join(data))
      f.write(w)
  elif len(search)-1 == 6:
      data = search[0], "\t",search[6].replace("가격정보 더보기",""),"\n"
      w =(''.join(data))
      f.write(w)
  elif len(search)-1 == 5:
      data = search[0], "\t",search[5].replace("가격정보 더보기",""),"\n"
      w =(''.join(data))
      f.write(w)
  elif len(search)-1 == 4:
      printdata = search[0], "\t",search[4].replace("가격정보 더보기",""),"\n"
      w =(''.join(data))
      f.write(w)
  elif len(search)-1 == 3:
      printdata = search[0], "\t",search[3].replace("가격정보 더보기",""),"\n"
      w =(''.join(data))
      f.write(w)
  elif len(search)-1 == 2:
      data = search[0], "\t",search[2].replace("가격정보 더보기",""),"\n"
      w =(''.join(data))
      f.write(w)
f.write('================================\n')
f.close()
print("==============================")

