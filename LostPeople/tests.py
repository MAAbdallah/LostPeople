from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        time.sleep(5)
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_LogIn_Success(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        #find the form element
        user_name = selenium.find_element_by_id('id_username')
        password = selenium.find_element_by_id('id_password')

        submit = selenium.find_element_by_name('login')

        #Fill the form with data
        user_name.send_keys('hidy')
        time.sleep(5)
        password.send_keys('hidy1234')
        time.sleep(5)

        #submitting the form
        submit.send_keys(Keys.RETURN)
        time.sleep(10)
    def test_LogIn_Fail(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        #find the form element
        user_name = selenium.find_element_by_id('id_username')
        password = selenium.find_element_by_id('id_password')

        submit = selenium.find_element_by_name('login')

        #Fill the form with data
        user_name.send_keys('unary')
        time.sleep(5)
        password.send_keys('123456')
        time.sleep(5)

        #submitting the form
        submit.send_keys(Keys.RETURN)
        time.sleep(10)
    def test_SignUP_Success(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/signup/')
        #find the form element
        user_name = selenium.find_element_by_id('id_username')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')

        submit = selenium.find_element_by_name('signup')

        #Fill the form with data
        user_name.send_keys('bl7')
        time.sleep(5)
        password1.send_keys('hidy1234')
        password2.send_keys('hidy1234')
        time.sleep(5)

        #submitting the form
        submit.send_keys(Keys.RETURN)
        time.sleep(10)
    def test_SignUP_Fail(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/signup/')
        #find the form element
        user_name = selenium.find_element_by_id('id_username')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')

        submit = selenium.find_element_by_name('signup')

        #Fill the form with data
        #user_name.send_keys('hidy')
        user_name.send_keys('bl7')
        time.sleep(5)
        #password.send_keys('123456')
        password1.send_keys('hidy1234')
        password2.send_keys('hidy12355')
        time.sleep(5)

        #submitting the form
        submit.send_keys(Keys.RETURN)
        time.sleep(10)

class MissedTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        time.sleep(5)
        super(MissedTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(MissedTestCase, self).tearDown()

    def test_AddMissed_Success(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/missed/create/')
        #find the form element
        missed_name = selenium.find_element_by_id('nameM')
        location = selenium.find_element_by_id('location')
        Age = selenium.find_element_by_id('Age')
        NameFR = selenium.find_element_by_id('NameFR')
        phone = selenium.find_element_by_id('phone')
        IMG = selenium.find_element_by_id('IMG')

        submit = selenium.find_element_by_name('addMissed')

        #Fill the form with data
        missed_name.send_keys('hady')
        time.sleep(2)
        location.send_keys('13-st')
        time.sleep(2)
        Age.send_keys('15')
        time.sleep(2)
        NameFR.send_keys('mohamed')
        time.sleep(2)
        phone.send_keys('01002426518')
        time.sleep(2)
        IMG.send_keys('G:\coding\Django\GP2\photo\صفحة مفقودين\pictest.jpg')
        time.sleep(2)

        #submitting the form
        submit.send_keys(Keys.RETURN)
        time.sleep(2)
    def test_AddMissed_Fail(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/missed/create/')
        #find the form element
        missed_name = selenium.find_element_by_id('nameM')
        location = selenium.find_element_by_id('location')
        Age = selenium.find_element_by_id('Age')
        NameFR = selenium.find_element_by_id('NameFR')
        phone = selenium.find_element_by_id('phone')
        IMG = selenium.find_element_by_id('IMG')

        submit = selenium.find_element_by_name('addMissed')

        #Fill the form with data
        missed_name.send_keys('hady')
        time.sleep(2)
        location.send_keys('13-st')
        time.sleep(2)
        Age.send_keys('15')
        time.sleep(2)
        NameFR.send_keys('mohamed')
        time.sleep(2)
        phone.send_keys('01002426518')
        time.sleep(2)
        IMG.send_keys('G:\coding\Django\GP2\pics\pic2.jpg')
        time.sleep(2)

        #submitting the form
        submit.send_keys(Keys.RETURN)
        time.sleep(2)

    def test_SeachByImg_Success(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/missed/API')
        #find the form element
        img = selenium.find_element_by_id('IMG')

        submit = selenium.find_element_by_name('submit')

        #Fill the form with data
        img.send_keys('G:\coding\Django\GP2\pics\pic2.jpg')
        time.sleep(2)
        #submitting the form
        submit.send_keys(Keys.RETURN)
        time.sleep(2)
    def test_SeachByImg_Fail(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/missed/API')
        # find the form element
        img = selenium.find_element_by_id('IMG')

        submit = selenium.find_element_by_name('submit')

        # Fill the form with data
        img.send_keys('G:\coding\Django\GP2\pics\pic7.jpg')
        time.sleep(2)
        # submitting the form
        submit.send_keys(Keys.RETURN)
        time.sleep(2)

    def test_Search(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/missed/search')
        # find the form element
        name = selenium.find_element_by_name('SearchedName')
        age =  selenium.find_element_by_name('age')
        #date = selenium.find_element_by_name('bday')
        submit = selenium.find_element_by_id('SearchID')

        name.send_keys('hidy')
        time.sleep(2)
        age.send_keys('ten')
        time.sleep(2)
        #date.send_keys('6/19/2019')
        #time.sleep(2)
        submit.send_keys(Keys.RETURN)
        time.sleep(2)