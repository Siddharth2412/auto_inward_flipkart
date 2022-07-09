from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import selenium
import time


class Inward:
    def __init__(self,id,pwd):
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.maximize_window()
        self.driver.get('https://seller.flipkart.com/sell-online/')
        time.sleep(8)

        login_button = '//*[@id="app"]/div[1]/div[2]/div/span'
        '//*[@id="app"]/div[1]/div[2]'

        # Old Code data
        # login_text = '/html/body/div[6]/div/div/div[2]/div[1]/form/div[1]/div/input'
        # password_text = '/html/body/div[6]/div/div/div[2]/div[1]/form/div[2]/div/input'
        # login = '/html/body/div[6]/div/div/div[2]/div[2]/button'
        # login_text_class = 'user-input'

        button_css = 'dCpPQE'

        self.driver.find_element_by_xpath(login_button).click()
        time.sleep(1)

        # Old Code
        # self.driver.find_element_by_xpath(login_text).send_keys(id)
        # self.driver.find_element_by_class_name(login_text_class).send_keys(id)

        self.driver.find_element_by_name('username').send_keys(id)
        try:
            self.driver.find_element_by_class_name(button_css).click()
        except:
            pass
        time.sleep(1)
        self.driver.find_element_by_name('password').send_keys(pwd)
        self.driver.find_element_by_class_name(button_css).click()
        time.sleep(5)

        self.driver.get('https://seller.flipkart.com/index.html#dashboard/fbflite-fa/LOC4c0b59045c9840c8ad360aef146fdbe1/nav-fa/inwarding')
        time.sleep(5)


    def inward_data(self,lid,qty,bin):
        qty_textbox = '//*[@id="quantity0"]'
        bin_textbox = '//*[@id="binId0"]'
        submit = '//*[@id="save-to-bin"]'
        inward_yes = '//*[@id="qc-pass"]'
        cancel_save = '//*[@id="cancel-save"]'
        lid_textbox = 'productId-input'

        try:
            self.driver.find_element_by_class_name(lid_textbox).send_keys(lid)
            self.driver.find_element_by_class_name(lid_textbox).send_keys(Keys.ENTER)
        except:
            return lid

        time.sleep(2)

        try:
            self.driver.find_element_by_class_name('confirm-button').click()
        except:
            pass

        time.sleep(2)

        try:
            self.driver.find_element_by_xpath(inward_yes).click()
        except:
            return lid

        self.driver.find_element_by_xpath(qty_textbox).send_keys(qty)
        self.driver.find_element_by_xpath(bin_textbox).send_keys(bin)
        self.driver.find_element_by_xpath(submit).click()
        time.sleep(3)

        try:
            self.driver.find_element_by_xpath(cancel_save).click()
            time.sleep(2)
            return lid
        except:
            pass

    def shut_down(self):
        self.driver.close()
        self.driver.quit()