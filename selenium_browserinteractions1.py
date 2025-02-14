from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select


class Interactions():
    def __init__(self):
        #Opens the link in Chrome
        baseurl = "https://www.letskodeit.com/practice"
        self.driver = webdriver.Chrome()
        self.driver.get(baseurl)
        #Maximizes window
        self.driver.maximize_window()
        #Tells driver to wait for 10s before failing when trying to locate an element
        self.driver.implicitly_wait(10)

    def test1(self):
        #Returns title of the webpage
        print("Title:"+self.driver.title)
        #Returns current url of the webpage
        print("Current url:"+self.driver.current_url)
        #Refreshes the page
        self.driver.refresh()
        #Going one step backward and one step forward in browser history
        self.driver.get("https://www.google.com")
        self.driver.back()
        time.sleep(2)
        self.driver.forward()
        time.sleep(3)
        #Browser Close/Quit
        #self.driver.close() - Closes the current window
        self.driver.quit()

    def test2(self):
        self.__init__()
        #Finds the web element of the Sign in button
        loginbutton=self.driver.find_element(By.XPATH,"//a[@href='/login']")
        #Clicks Sign in button and takes user to Sign in page
        loginbutton.click()
        emailfield=self.driver.find_element(By.ID,"email")
        #Inputs the given text on the text field
        emailfield.send_keys("nishanttest@gmail.com")
        time.sleep(2)
        passwordfield=self.driver.find_element(By.ID,"login-password")
        passwordfield.send_keys("abc123")
        time.sleep(2)
        #Clicks the Submit button
        self.driver.find_element(By.ID,"login").click()
        time.sleep(2)
        self.driver.quit()

    def test3(self):
        self.__init__()
        field1=self.driver.find_element(By.ID,"enabled-example-input")
        #Checks if a web element is enabled or disabled
        print("Enabled? "+str(field1.is_enabled()))
        #Clicking this button disables the input field
        self.driver.find_element(By.ID,"disabled-button").click()
        print("Enabled? "+str(field1.is_enabled()))

        field2=self.driver.find_element(By.ID,"displayed-text")
        #Checks if web element is displayed or hidden
        print("Displayed? "+str(field2.is_displayed()))
        #This button hides the input field
        self.driver.find_element(By.ID,"hide-textbox").click()
        print("Displayed? "+str(field2.is_displayed()))

        #Checks if a radio button/check box is selected
        radiob=self.driver.find_element(By.ID,"bmwradio")
        radiob.click()
        print("BMW Selected?"+str(radiob.is_selected()))

    def test4(self):
        #Finds dropdown menu
        element = self.driver.find_element(By.ID,"carselect")
        sel = Select(element)
        #Selecting from dropdown with index
        sel.select_by_index(1)
        time.sleep(1)
        #Selecting from dropdown with value
        sel.select_by_value("bmw")
        time.sleep(1)
        #Selecting from dropdown with visible text
        sel.select_by_visible_text("Honda")
        time.sleep(1)



a=Interactions()
a.test1()
a.test2()
a.test3()
a.test4()
