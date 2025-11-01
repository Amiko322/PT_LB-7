from appium import webdriver
from appium.options.android import UiAutomator2Options

class AppiumDriver:
    '''
    Appium Driver
    '''
    @staticmethod
    def get(
        app=r"C:\Users\Amiko\Desktop\Тестирование\ЛБ7\PT_LB-7\apk\notes.apk",
        device_name="emulator-5556"
    ):
        '''
        Get Appium Driver
        '''
        options = UiAutomator2Options().load_capabilities({
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "udid": device_name,
            "deviceName": device_name,
            "app": app,
            "noReset": True,
            "newCommandTimeout": 120
        })

        return webdriver.Remote(
            "http://127.0.0.1:4723", 
            options=options
        )