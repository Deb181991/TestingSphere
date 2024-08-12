# from Testing6 import *
import time

from selenium import webdriver
# from selenium.webdriver import EdgeOptions
from selenium.webdriver.chrome.options import Options

from Logs import log_file

log = log_file.get_logs()

options1 = Options()
prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False,
         "download.default_directory": "F:\SphereWMS\CevaVision - Copy\CevaVision\Download"}
options1.add_experimental_option("excludeSwitches", ["enable-automation"])
options1.add_experimental_option("prefs", prefs)
options1.add_experimental_option("detach", True)


# # options2 = EdgeOptions()
# prefs = {"credentials_enable_service": False,
#          "profile.password_manager_enabled": False}
# options2.add_experimental_option("excludeSwitches", ["enable-automation"])
# options2.add_experimental_option("prefs", prefs)
# options2.add_experimental_option("detach", True)


def before_all(context):
    # *****************************************************************************************************#
    # global browserName
    # browserName = input("Enter the Browser")
    # if browserName == 'chrome':
    #
    #     # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options1)
    #     driver = webdriver.Chrome(executable_path="D:\Bestinet\Driver\chromedriver.exe", options=options1)
    #
    # elif browserName == 'firefox':
    #     driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # elif browserName == 'edge':
    #     driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    # else:
    #     # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options1)
    driver = webdriver.Chrome(executable_path='D:\Bestinet\Driver\chromedriver.exe', options=options1)
    time.sleep(5)

    log.info("Browser Name Entered")
    context.driver = driver
    log.info("Driver Initialized")
    context.driver.maximize_window()


# def before_scenario(context, scenario):
#     # height = GetSystemMetrics(1)
#     # width = GetSystemMetrics(0)
#     # time_stamp = datetime.datetime.now().strftime(
#     #     '%Y-%m-%d %H-%M-%S')
#     # file_name = f'{time_stamp}.mp4'
#     # fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
#     # final_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))
#     # while True:
#     #     img = ImageGrab.grab(bbox=(0, 0, width, height))
#     #     img_ny = ny.array(img)
#     #     img_final = cv2.cvtColor(img_ny, cv2.COLOR_BGR2RGB)
#     #     final_video.write(img_final)
#     time.sleep(1)
#
#
def after_step(context, step):
    if step.status == "failed":
        context.driver.delete_all_cookies()
        # context.driver.refresh()
    #  context.driver.quit()
#         allure.attach(context.driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
#         context.driver.get_screenshot_as_file(".\Fail-ScreenShots\Capture1.png")
#         fromaddr = "monalisab@esspl.com "
#         # toaddr = ["debadatta@esspl.com", "subratsahoo@esspl.com"]
#         toaddr = "monalisab@esspl.com "
#         msg = MIMEMultipart()
#         msg['From'] = fromaddr
#         # Multiple email send
#         # msg['To'] = ",".join(toaddr)
#         # Single email send
#         msg['To'] = toaddr
#         msg['Subject'] = "Error meassage"
#         body = """\
#                 Subject: Error Message
#
#                 Dear Team,
#
#                      Kindly find the attached screenshot for the Error.
#
#                 Thanks & Regards,
#                 Debadatta Pattanaik
#                 Senior Tester."""
#         msg.attach(MIMEText(body, 'plain'))
#         filename = "Capture1.png"
#         attachment = open("E:\\Phoenix_20High\\Fail-ScreenShots\\Capture1.png", "rb")
#         p = MIMEBase('application', 'octet-stream')
#         p.set_payload((attachment).read())
#         encoders.encode_base64(p)
#         p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
#         msg.attach(p)
#         s = smtplib.SMTP('smtp.gmail.com', 587)
#         s.starttls()
#         s.login(fromaddr, "Password")
#         text = msg.as_string()
#         s.sendmail(fromaddr, toaddr, text)
#         s.quit()
# # from Testing9 import *
# # import time
# #
# # from selenium import webdriver
# # from webdriver_manager.chrome import ChromeDriverManager
# # from webdriver_manager.firefox import GeckoDriverManager
# # from webdriver_manager.microsoft import EdgeChromiumDriverManager
# #
# # from Pages.LoginPage import myLogger
# #
# #
# # # from webdrivermanager import GeckoDriverManager, EdgeChromiumDriverManager, ChromeDriverManager
# #
# #
# # from hooks import browserName
#
#
# # global browserName
#
#
# def before_all(context):
#     # parser = argparse.ArgumentParser()
#     # parser.add_argument('browserName', help="enter the browser")
#     #
#     # args = parser.parse_args()
#     # print(args)
#
#     global browserName
#
#     browserName = input("Enter the Browsername")
#
#     if browserName == 'chrome':
#         # driver = webdriver.Chrome(executable_path="D:\pythonProject1\Driver\chromedriver_win32\chromedriver.exe")
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#     elif browserName == 'firefox':
#         driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#     elif browserName == 'edge':
#         driver = webdriver.Edge(EdgeChromiumDriverManager().install())
#     elif browserName == '':
#         # driver = webdriver.Chrome(executable_path="D:\pythonProject1\Driver\chromedriver_win32\chromedriver.exe")
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#     else:
#         print('Enter correct browser here')
#         time.sleep(5)
#     context.driver = driver
#     myLogger.info("****** Driver Initialized ******")
#     context.driver.maximize_window()
