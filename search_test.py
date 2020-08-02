import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class EcomerceHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver #Para no repetir el codigo
        driver.get("http://demo-store.seleniumacademy.com") #Para ir a nuestro sitio web donde vamos a estar practicando
        driver.maximize_window() #Indicamos al navegador que maximize ventana
        driver.implicitly_wait(10) #Va a esperar max 15 seg para que ocurra este cambio antes de ejectar la prueba

    def test_search_text_field(self): #Barra de busqueda
        search_field = self.driver.find_element_by_id("search") #Va a encontrar ese elemento por su id, sabemos su id gracias a la pag web, inspeccionar

    def test_search_text_field_by_name(self):#Barra de busqueda
        search_field = self.driver.find_element_by_name("q")

    def test_search_text_field_by_class(self):#Barra de busqueda
        search_field = self.driver.find_element_by_class_name("input-text")

    def test_search_button_enabled(self):#Boton barra busqueda(lupa)
        button = self.driver.find_element_by_class_name("input-text")

    def test_count_of_promo_bar(self):#imagenes de promocion
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name('img')#Almacenamos la busqueda de esos banners y busca los elemntos por tag name
        self.assertEqual(3,len(banners))#Para contar las img, son 3 imagenes.

    def test_vip_promo(self): #imagen principal
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')

    def test_shopping_cart(self): #icono del carrito de compra
        shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")

    def tearDown(self):
        self.driver.quit()#Cierra ventana y cualquier sesion iniciada

if __name__ == '__main__':
    unittest.main(verbosity = 2)
