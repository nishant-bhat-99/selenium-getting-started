from selenium import webdriver
from selenium.webdriver.common.by import By

class Findelement():
    #The method testid opens a websites and finds web elements using different techniques.
    def testid(self):
        baseurl = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        elementbyid = driver.find_element(By.ID,"bmwcheck")
        print (elementbyid)
        if elementbyid is not None:
            print("Found element using ID")

        elementbyname = driver.find_element(By.NAME,"viewport")
        print (elementbyname)
        if elementbyname is not None:
            print("Found element using Name")

        elementbyxpath = driver.find_element(By.XPATH,"//input[@value='bmw']")
        print(elementbyxpath)
        if elementbyxpath is not None:
            print("Found element using XPath")

        elementbycss = driver.find_element(By.CSS_SELECTOR, "#bmwcheck")
        print(elementbycss)
        if elementbycss is not None:
            print("Found element using CSS Selector")

        elementbylink = driver.find_element(By.PARTIAL_LINK_TEXT, "ALL")
        if elementbylink is not None:
            print("Found element using Link Text")

        elementbytag = driver.find_element(By.TAG_NAME,"a")
        elementbyclass = driver.find_element(By.CLASS_NAME, "inputs")
        if elementbytag is not None:
            print("Found element using tag")
        if elementbyclass is not None:
            print ("Found element using class")

        elementlist = driver.find_elements(By.TAG_NAME,"td")
        if elementlist is not None:
            print("Found multiple elements of size "+str(len(elementlist)))

a= Findelement()
a.testid()