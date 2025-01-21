from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chrome_service
from selenium.webdriver.firefox.service import Service as FF_service
from selenium.webdriver.edge.service import Service as Edge_service

class tester():
    def test_chrome(self):
        #Set location of the chromedriver
        service_var=Chrome_service(executable_path="C:\\Users\\nisha\\workspace_python\\SeleniumWD_Tutorial\\drivers\\chromedriver.exe")

        #Instantiates browser
        driver = webdriver.Chrome(service=service_var)

        #Open the URL
        driver.get("https://www.google.com")

    def test_firefox(self):
        service_var=FF_service(executable_path="C:\\Users\\nisha\\workspace_python\\SeleniumWD_Tutorial\\drivers\\geckodriver.exe")
        driver=webdriver.Firefox(service=service_var)
        driver.get("https://www.google.com")

    def test_edge(self):
        service_var=Edge_service(executable_path="C:\\Users\\nisha\\workspace_python\\SeleniumWD_Tutorial\\drivers\\msedgedriver.exe")
        driver=webdriver.Edge(service=service_var)
        driver.get("https://www.google.com")


a= tester()
a.test_firefox()
a.test_chrome()
a.test_edge()