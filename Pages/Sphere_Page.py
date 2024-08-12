import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from Utilities.Assertion import assertion
from Utilities.GenericMethod import genericmethod
from Utilities.customLogger import LogGen
from Utilities.readproperty import ReadConfig
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

myLogger = LogGen.loggeen()
DateTime = time.ctime()

baseURL = ReadConfig.getURL()

# myScreenshot = pyautogui.screenshot()
# keyboard = pynput.keyboard.Controller()
# Driver.get(baseURL)

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.genericMethod = genericmethod(driver)
        self.assertion = assertion(driver)
        self.act = ActionChains(driver)


    ##*************************************************************************##
    #############################"""""""""XPATH""""""""##########################
    #############################"""""""""Login Page""""""""##########################

    def UserID(self):
        return self.driver.find_element(By.XPATH, "//*[@id='username']")

    def Password(self):
        return self.driver.find_element(By.XPATH, "//*[@name='password']")

    def Button_Login(self):
        return self.driver.find_element(By.XPATH, "//*[@type='submit']")
    
    def Dashboard(self):
        return self.driver.find_element(By.XPATH, "//*[@title='Dashboard']")

    def TargetPortal(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Target Portal']")
    
    def Close(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Close']")
    def IdentifyItems(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Identify Items to Bin ']")

    def TruckInformation(self):
        return self.driver.find_element(By.XPATH, "//div[@class='boxImage col-12']//img[1]")
    def TruckSchedule(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Truck Schedule ']")
    def NewRequest(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' New Request ']")
    def EnterRequest(self):
        return self.driver.find_element(By.XPATH, "//*[@name='request']")
    def selecteCarrier(self):
        return self.driver.find_element(By.XPATH, "//*[@name='selectedCarrier']")
    def InStoreDate(self):
        return self.driver.find_element(By.XPATH, "//*[@name='strD']")
    def Date(self):
        return self.driver.find_element(By.XPATH, "//*[@class='btn-light']/..//*[text()='"+date+"']")
    
    def Origins(self):
        return self.driver.find_element(By.XPATH, "//*[@name='origins']") 
    def locations(self):
        return self.driver.find_element(By.XPATH, "//*[@name='locations']")
    def showPickUpTime(self):
        return self.driver.find_element(By.XPATH, "//*[@name='showPickUpTime']/../../..//*[@class='fa fa-calendar']")
    def PickUpTime(self):
        return self.driver.find_element(By.XPATH, "//*[@name='showPickUpTime']")
    def showDeliveryTime(self):
        return self.driver.find_element(By.XPATH, "//*[@name='showDeliveryTime']/../../..//*[@class='fa fa-calendar']")
    def DeliveryTime(self):
        return self.driver.find_element(By.XPATH, "//*[@name='showDeliveryTime']")
    def SubmitButton(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Submit']") 
    def OkButton(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Ok']")

    def CloseBūtton(self):
        return self.driver.find_element(By.XPATH, '//*[text()="Close"]')
    
    def PickDate(self):
        return self.driver.find_element(By.XPATH, "(//div[text()='"+datepick+"'])[1]")
    def DeliveryDate(self):
        return self.driver.find_element(By.XPATH, "(//div[text()='"+dateDelivery+"'])[1]")
    
    def DragtoConfirmdetails(self):
        return self.driver.find_element(By.XPATH, "//table[contains(@class,'table table-striped')]/tbody[1]/tr[1]/td[3]")
    
    def source_element(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Origin ']")
    
    # def target_element(self):
    #     return self.driver.find_element(By.XPATH, "//*[text()=' Next Available Delivery ']")
        
    def Action(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Actions ']")       
    def More(self):
        return self.driver.find_element(By.XPATH, "//*[@class='confirm-detail-truck']")
    def truckmodal(self):
        return self.driver.find_element(By.XPATH, "//*[@class='truck-modal-image']")
    
        
    # ************************************** Gamil LOGIN **************************************************#
    def LaunchBrowser(self, Sphere_Url):
        self.genericMethod.navigateTo(Sphere_Url)
        time.sleep(2)
        # frame_element = self.driver.find_element(By.XPATH, "//iframe[@id='chatbotIframe']")
        # self.driver.switch_to.frame(frame_element)
        # print("Login page")

    def enterUserName(self, username):
        self.genericMethod.type(LoginPage.UserID(self), username)

    def enterPassword(self, password):
        self.genericMethod.type(LoginPage.Password(self), password)
        time.sleep(1)

    def clickOnLogin(self):
        self.genericMethod.click(LoginPage.Button_Login(self))
        time.sleep(5)

#**************************************** Truck Request Creation ***************************************
    def Dashboard_Menu(self):
        self.genericMethod.click(LoginPage.Dashboard(self))
        time.sleep(2)

    def Target_Portal(self):
        self.genericMethod.click(LoginPage.TargetPortal(self))
        time.sleep(2)
        self.genericMethod.switchToTab(1)
        # time.sleep(15)
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Close']")))
        time.sleep(2)
        self.genericMethod.click(LoginPage.CloseBūtton(self))
        time.sleep(2)


    def Truck_Information(self):
        self.genericMethod.click(LoginPage.TruckInformation(self))
        time.sleep(2)
 
    def Truck_Schedule(self):
        self.genericMethod.click(LoginPage.TruckSchedule(self))
        time.sleep(8)
        # self.genericMethod.click(LoginPage.NewRequest(self))

    def New_Request(self):
        # self.genericMethod.clickUsingJS(LoginPage.Close(self))
        # time.sleep(1)
        self.genericMethod.click(LoginPage.NewRequest(self))
        time.sleep(10)
        
    def Enter_Request(self,SelectType):
        select = Select(LoginPage.EnterRequest(self))
        select.select_by_visible_text(SelectType)
        
    def Service_Provider(self,ServiceProvider):
        select = Select(LoginPage.selecteCarrier(self))
        select.select_by_visible_text(ServiceProvider)
     
    def InStore_Date(self):
        self.genericMethod.click(LoginPage.InStoreDate(self))
        today = datetime.today()
        days_ahead = 0 - today.weekday() + 7
        next_monday_date = today + timedelta(days=days_ahead)
        global date
        date = str(next_monday_date.day)
        myLogger.info(date)
        # time.sleep(2)
        self.genericMethod.click(LoginPage.Date(self))

    def TargetOrigin(self,TargetOrigin):
        select = Select(LoginPage.Origins(self))
        select.select_by_visible_text(TargetOrigin)

    def TargetDestination(self,Destination):
        select = Select(LoginPage.locations(self))
        select.select_by_visible_text(Destination)
    
    def RequestedPickUpDate(self):
        self.genericMethod.click(LoginPage.showPickUpTime(self))
        today = datetime.today()
        global datepick
        datepick = str(today.day)
        myLogger.info(datepick)
        # time.sleep(2)
        self.genericMethod.click(LoginPage.PickDate(self))
    
    def RequestedDeliveryDate(self):
        self.genericMethod.click(LoginPage.showDeliveryTime(self))
        today = datetime.today()
        global dateDelivery
        dateDelivery = str(today.day)
        myLogger.info(dateDelivery)
        # time.sleep(2)
        self.genericMethod.click(LoginPage.DeliveryDate(self))

    def PickUptime(self,time):
        self.genericMethod.type(LoginPage.PickUpTime(self),time)

    def Deliverytime(self,time):
        self.genericMethod.type(LoginPage.DeliveryTime(self),time)
    
    def submit(self):
        self.genericMethod.click(LoginPage.SubmitButton(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.OkButton(self)) 
        time.sleep(5)
    def ConfirmDetails(self):
        # self.genericMethod.click(LoginPage.SubmitButton(self))
        # self.act.drag_and_drop(LoginPage.source_element, LoginPage.target_element).perform()
        self.genericMethod.click(LoginPage.Action(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.More(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.truckmodal(self))
        time.sleep(1)
        Hawb = self.genericMethod.ReadData(".//TestData//HawbPipo.json", "PIPO")
        myLogger.info(Hawb)



#****************************************  PICK  ********************************************
    def allocation_Pick(self):
        return self.driver.find_element(By.XPATH, '//*[@class="pointer allocation"]')
    def Pick(self):
        return self.driver.find_element(By.XPATH, '//*[@id="menu-pick"]')
    def Locationchoose(self):
        return self.driver.find_element(By.XPATH, '//*[@id="Location"]')
    def GetNextPick(self):
        return self.driver.find_element(By.XPATH, '//*[text()="Get Next Pick"]')
    def ScanLP(self):
        return self.driver.find_element(By.XPATH, '//*[text()="Scan License Plate"]/..//*[@class="form-control text "]')
    def ScanLPOKButton(self):
        return self.driver.find_element(By.XPATH, '//*[text()="OK"]')

###############################################################################################
    def Aloction(self):
            self.genericMethod.click(LoginPage.allocation_Pick(self))
            time.sleep(1)

    def PickButton(self):
            self.genericMethod.click(LoginPage.Pick(self))
            time.sleep(4)

    def locationDropDown(self,location):
            # self.genericMethod.click(LoginPage.Locationchoose(self))
            time.sleep(1)
            select = Select(LoginPage.Locationchoose(self))
            select.select_by_visible_text(location)
            time.sleep(1)
            self.act.send_keys(Keys.ENTER).perform()
            time.sleep(1)

    def getNextPickButton(self):
            self.genericMethod.click(LoginPage.GetNextPick(self))
            time.sleep(4)
    def EnterLP(self,Lp):
            
            self.genericMethod.type(LoginPage.ScanLP(self),Lp)
            time.sleep(1)
            self.act.send_keys(Keys.ENTER).perform()
            time.sleep(1)
            self.genericMethod.click(LoginPage.ScanLPOKButton(self))