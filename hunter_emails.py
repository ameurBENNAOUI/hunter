from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import pymongo
import numpy as np
import pandas as pd
def find_by_xpath(locator):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, locator))
    )

    return element
def find_by_id(locator):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, locator))
    )

    return element
def find_by_css(locator):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, locator))
    )

    return element
def find_by_class(locator):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, locator))
    )

    return element
def parse_results(results,result_number):
    for result in results: 
        try:
            name=result.find_element_by_css_selector('span.name').text
        except:
            name=None
        try:
            position=result.find_element_by_css_selector('span.position').text
        except:
            position=None            
        try:
           linkedin=result.find_element_by_css_selector('a.fab.fa-linkedin').get_attribute('href')
        except:
            linkedin=None
            
        try:
            department=result.find_element_by_css_selector('span.department').text
        except:
            department=None
        try:
            phone=result.find_element_by_css_selector('span.phone').text
        except:
            phone=None
        try:
            email=result.find_element_by_css_selector('div.email').text
        except:
            email=None
        try:    
            score_high_score=result.find_element_by_css_selector('div.score.high-score').get_attribute('data-original-title').replace('Confidence score: ','')
        except:
            score_high_score=None
        try:
            last_checked_date=result.find_element_by_css_selector('div.sources-list > div > span.source-date').get_attribute('innerHTML').replace('\n','')
        except:
            last_checked_date=None
            
        data={"company":company,
                        "name":name,
                        "department":department,
                        "linkedin":linkedin,
                        "position":position,
                        "phone":phone,
                        "email":email,
                        "score_high_score":score_high_score,
                        "last_checked_date":last_checked_date,
                        "result_number":result_number,
                        "st":"new"
                        }
        print(data['email'])
        mystatus.insert_one(data)
    return driver.find_element_by_css_selector('div.account-detail').get_attribute('innerHTML').split('span')[1].split('pull-right">')[1].replace('</','')

    
def get_driver(user):
    try:
        driver.close()

    except:
        print('no driver sutdown')
        
        
    opera_profile = r'%appdata%\\opera software\\Opera stable' 
    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir=' + opera_profile)
    options._binary_location = r'C:\\Users\\amb\\AppData\Local\\Programs\Opera\\63.0.3368.71_0\\opera.exe'
    url='https://hunter.io/users/sign_in'
    
    driver = webdriver.Opera(executable_path='operadriver.exe',options=options)
    time.sleep(5)
    driver.delete_all_cookies()


    driver.get(url)
    time.sleep(5)
    driver.find_element_by_id('email-field').send_keys(user)
    driver.find_element_by_id('password-field').send_keys('Mohamed@2004')
    driver.find_element_by_css_selector('button.btn-lg.btn-orange').click()


    
    return driver
def process_pre(k):
    k=k+1
    print('processing....: {}'.format(k))
    driver.find_element_by_id('domain-field').clear()
    driver.find_element_by_id('domain-field').send_keys(list_company[k])
    driver.find_element_by_id('search-btn').click()
#    time.sleep(3)
    return k
def process_pre_company(company_domain):
    k=k+1
    print('processing....: {}'.format(k))
    driver.find_element_by_id('domain-field').clear()
    driver.find_element_by_id('domain-field').send_keys(company_domain)
    driver.find_element_by_id('search-btn').click()
#    time.sleep(3)
    return k
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mystatus = myclient["company"]["contacts"]

user='ameur313@outlook.com'
driver=get_driver(user)
#find_by_id('email-field').send_keys(user)
#find_by_id('password-field').send_keys('Mohamed@2004')
#find_by_css('button.btn-lg.btn-orange').click()

list_company=np.loadtxt('domain_company.txt',dty9pe="str")

company=list_company[43]
#for company in list_company:
k=47
##3104 position adde
for k in range(43,55):

    k=process_pre(k)
    
    result_number=find_by_css('div.results-count').text
    print(result_number)
    
    results=driver.find_elements_by_css_selector('div.result')
    print(parse_results(results,result_number))
    
    
    
k=61  
    
www.gea.com 












    
    
    while True:
        try:
            driver.find_element_by_css_selector('button.show-more.btn-white').click()
            time.sleep(1)
        except:
            break
    
    try:
        results=find_by_css('div.result')

        results=driver.find_elements_by_css_selector('div.result')
    except:
        print("no results1!")
    if len(results)<1:
        print("no results2!")
    print(parse_results(results))
#    k=k+1


results=driver.find_elements_by_css_selector('div.result')
print(parse_results(results))


driver_linked = webdriver.Opera(executable_path='operadriver.exe',options=options)
driver_hunter = webdriver.Opera(executable_path='operadriver.exe',options=options)

company_name=np.loadtxt('company_name.txt',delimiter=';',dtype="str")
domain_name=np.loadtxt('domain_name.txt',delimiter=';',dtype="str")

k=24
name=company_name[k]
company=domain_name[k]
company_name_=company.split('.')[-2]

#data=mystatus.find( { "position": { "$exists": True}, "position": { "$ne": None}})
data=mystatus.find( { "position": { "$exists": True},"email":{"$regex" : ".*"+company_name_+".*"}})
#data=mystatus.find( { "position": { "$exists": True},"position": { "$ne": None}}),"position":{"$regex" : "*ressources*"}})
#data=mystatus.find( { "position": { "$exists": True},"position": { "$ne": None},"position":{"$eq" : "Operations Vp"}})
data.count()
dd=data[0]

data=mystatus.find( { "position": { "$exists": True}})
data_=[]
for dd in data:
    del dd['_id']
    data_.append(dd)
df = pd.DataFrame(data_)    

df.to_csv("dta.csv", sep='\t', encoding='utf-8')


position=data.distinct('position')
lis=[]
for dd in data:
                print(dd['name'],"  :  ",dd['position'],"  :  ",dd['email'])

    try:
#        if dname.split(" ")[1] in dd['name']:
        if (dd['email'] not in lis):
            dd['position']
            lis.append(dd['email'])
            print(dd['name'],"  :  ",dd['position'],"  :  ",dd['email'])


    except:    
        continue



linked_company=[]
linked_company.append('linked_company')
for k  in range(1,len(company_name)):
    try:
        url=''
        name=company_name[k]
        company=domain_name[k]
        company_name=company.split('.')[-2]
    
        driver_linked.get('https://www.google.com')
        driver_linked.find_element_by_css_selector("input.gLFyf.gsfi").send_keys(company+" linkedin")
        driver_linked.find_element_by_css_selector("input.gLFyf.gsfi").send_keys(Keys.RETURN)
        time.sleep(1)
        url=find_by_css('#rso > div > div > div:nth-child(1) > div > div > div.r > a',driver_linked).get_attribute("href")
        linked_company.append(url)
    except:
        
        list_domains
domain_names=np.loadtxt('list_domains.txt',delimiter=';',dtype="str")
elem={}
dd=domain_names[1]
dmain_list=[]
for dd in domain_names:
    elem={}
    elem["Domain"]=dd
    data=[]
    try:
        company_name_=dd.split('.')[-2]
        data=mystatus.find( { "position": { "$exists": True},"email":{"$regex" : ".*"+company_name_+".*"}}).sort([("score_high_score", pymongo.DESCENDING), ("position", pymongo.DESCENDING)])
    except:
        data.append('NAN')
    try:
        elem["email"]=data[0]['email']
    except:
        elem["email"]="NAN"
        pass
    try:
        elem["email1"]=data[1]['email']
    except:
        elem["email1"]="NAN"
        pass
    try:
        elem["email2"]=data[2]['email']
    except:
        elem["email2"]="NAN"
        pass
    try:
        elem["email3"]=data[3]['email']
    except:
        elem["email3"]="NAN"
        pass
    try:
        elem["email4"]=data[4]['email']
    except:
        elem["email4"]="NAN"
        pass
    try:
        elem["email5"]=data[5]['email']
    except:
        elem["email5"]="NAN"
        pass
    dmain_list.append(elem)

    
    
df = pd.DataFrame(dmain_list)    

df.to_csv("domain_list.csv", sep='\t', encoding='utf-8') 