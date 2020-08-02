import unittest
from selenium import webdriver

class CompareProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.get("http://google.com")
        driver.maximize_window()

    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('youtube')
        search_field.submit()

        driver.back() #Retrocede pag anterior
        driver.forward()#pag siguiente
        driver.refresh() #Refresca la pagina


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)
