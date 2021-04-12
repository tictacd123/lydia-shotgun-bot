from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium import webdriver
import time
# import argparse
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


# print(args.url)
ua = UserAgent()
userAgent = ua.random
print(userAgent)

def selenium_chrome_instance():
  from selenium.webdriver.chrome.options import Options
  options = Options()
  options.add_argument(f'user-agent={userAgent}')
  # options.add_argument("--headless")
  driver = webdriver.Chrome(options=options, executable_path=r"/home/diego/Documents/code/lydia_bot/chromedriver")
  return driver    

def lydia(driver, url, prenom, nom, num,mailzer):

  driver.get(url)

  try:
    email_field= driver.find_element_by_name('customdata[val4]')

    email_field.send_keys(mailzer)
  except:
    # print("An exception occurred with element 4")
    print("")

  try:
    l= driver.find_element_by_name('customdata[val5]')
    l.send_keys(mailzer)
  except:
    print("An exception occurred with element 5")

  # Fill the nom value
  nom_field = driver.find_element_by_name('customdata[val1]')
  nom_field.send_keys(nom)
  prenom_field = driver.find_element_by_name('customdata[val2]')
  prenom_field.send_keys(prenom)

  numero_field = driver.find_element_by_xpath('//*[@id="val3"]')
  numero_field.send_keys(num)

  try:
    option_field = driver.find_element_by_name('customdata[val6]')
    option_field.send_keys(" ...")

  except:
    print("")

  try:
      WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit-phone-form-lydia"]'))).click()
  except:
      print("An exception occurred with pay with cb button")
  try:
      WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[3]/a')))
      element3=driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/a')
      while element3.is_displayed():
            print(f"{bcolors.WARNING}Regarde ton compte le Lydia :) {bcolors.RESET}")
            time.sleep(0.5)
  except:
      print(f"{bcolors.OK}Paiement confirmé{bcolors.RESET}")
  

i=0
print("Combien de places environs tu espères commander: ")
nb = int(input())
print("Prénom:")
prenom = input()
print("Nom:")
nom = input()
print("Email:")
mailzer = input()
print("Ton 06:")
print(f"{bcolors.WARNING}Important renseigne ton num de tel lié au compte Lydia{bcolors.RESET}")
num = int(input())

drivers=[]
while i < nb+1:
  driver =selenium_chrome_instance()
  drivers.append(driver)

  i=i+1

print(f"{bcolors.WARNING}Dernière étape :))){bcolors.RESET}")

print("Url de la cagnotte Lydia: ")
url = input()
for driver in drivers:
  lydia(driver,url,prenom,nom,num,mailzer)

    

    













# try:
#     # cb_field = driver.find_element_by_name('creditCardNumber')
    
#     WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="creditCardNumber"]'))).click()
#     cb_field = driver.find_element_by_xpath('//*[@id="creditCardNumber"]')
#     cb_field.send_keys("6151583838333")
# except:
#     print('Cb form pas encore chargé')
# try:
#     # cb_field = driver.find_element_by_name('creditCardNumber')
#     cb_field = driver.find_element_by_id('creditCardExpiration')
#     cb_field.send_keys("10/22")
# except:
#     print('Cb form pas encore chargé')

# while cb_field is 0:
#     try:
#         cb_field = driver.find_element_by_name('creditCardNumber')
#     except:
#         print('Cb form pas encore chargé')

# try:
#     WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='submit-phone-form-noamount']"))).click()
# except:
#     print("An exception occurred with no-amount button")

# time.sleep(8)

# #Birthday verification
# driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select").click()
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[4]"))).click()

# driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select").click()
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[10]"))).click()

# driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select").click()
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[27]"))).click()

# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[6]/button"))).click()
# time.sleep(3)
# #
# fMail = fake_email[0].split("@")
# mailName = fMail[0]
# domain = fMail[1]
# instCode = verifiCode.getInstVeriCode(mailName, domain, driver)
# driver.find_element_by_name('email_confirmation_code').send_keys(instCode, Keys.ENTER)
# time.sleep(10)
# try:
#     not_valid = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[4]/div')
#     if(not_valid.text == 'That code isn\'t valid. You can request a new one.'):
#       time.sleep(1)
#       driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[1]/div[2]/div/button').click()
#       time.sleep(10)
#       instCodeNew = verifiCode.getInstVeriCodeDouble(mailName, domain, driver, instCode)
#       confInput = driver.find_element_by_name('email_confirmation_code')
#       confInput.send_keys(Keys.CONTROL + "a")
#       confInput.send_keys(Keys.DELETE)
#       confInput.send_keys(instCodeNew, Keys.ENTER)
# except:
#       pass
