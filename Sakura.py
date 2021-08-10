from appium import webdriver

desired_cap = {
"platformName": "Android",
"antomationName": "Appium",
"deviceName": "miike",
"platfromVersion": "7.1.2",
"appPackage": "com.pitayagames.sakura.stg6.dgs",#使用adb命令adb shell dumpsys window | findstr mCurrentFocus 查看当前app的包名和package
"appActivity": "com.pitayagames.sakura.AppActivity",
"noReset": True,
"unicodeKeyboard":True,
"resetKeyboard":True
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_cap)

driver.implicitly_wait(10)#隐式等待10秒