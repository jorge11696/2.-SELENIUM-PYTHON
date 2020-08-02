import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import  By


class AssertionsTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window()

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, "q"))

    def test_language_option(self): #Barra seleccionar lenguaje
        self.assertTrue(self.is_element_present(By.ID, "select-language"))


    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, how, what): #identificar  donde esta el elemento
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True

if __name__ == '__main__':
    unittest.main(verbosity = 2)
