from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.select import Select
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.thesparksfoundationsingapore.org/")

    def test_page1_logo(self):
        self.driver.find_element_by_xpath('//*[@id="home"]/div/div[1]/h1/a')
        assert True

    def test_page1_nav_bar(self):
        self.driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul')
        assert True

    def test_page1_know_more_button(self):
        a=self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/a')
        a.click()
        time.sleep(2)
        assert True

    def test_page1_learn_more_button(self):
        a=self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/a')
        a.click()
        time.sleep(2)
        assert True

    def test_page2_about(self):
        a=self.driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[1]/a')
        a.click()
        time.sleep(2)
        b=self.driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[1]/ul/li[1]/a')
        b.click()
        time.sleep(2)
        assert True

    def test_page3_policies(self):
        a=self.driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[2]/a')
        a.click()
        time.sleep(2)
        b=self.driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[2]/ul/li[1]/a')
        b.click()
        time.sleep(2)
        assert True

    def test_page4_programs(self):
        a=self.driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[3]/a')
        a.click()
        time.sleep(2)
        b=self.driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[3]/ul/li[1]/a')
        b.click()
        time.sleep(2)
        assert True

    def test_page5_links(self):
        a=self.driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[4]/a')
        a.click()
        time.sleep(2)
        b=self.driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[4]/ul/li[1]/a')
        b.click()
        time.sleep(2)
        assert True

    def test_page6_joinUs(self):
        a=self.driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[5]/a')
        a.click()
        time.sleep(2)
        b=self.driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[5]/ul/li[1]/a')
        b.click()
        time.sleep(2)
        assert True

    def test_page5_contact(self):
        a=self.driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[6]/a')
        a.click()
        time.sleep(2)
        assert True

    def test_page5_facebook(self):
        a=self.driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[1]/a')
        a.click()
        time.sleep(5)
        assert True

    def test_page5_linkedin(self):
        a=self.driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[2]/a')
        a.click()
        time.sleep(5)
        assert True

    def test_page5_medium(self):
        a=self.driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[3]/a')
        a.click()
        time.sleep(5)
        assert True

    def test_page5_twitter(self):
        a=self.driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[4]/a')
        a.click()
        time.sleep(5)
        assert True

    def test_page5_insta(self):
        a=self.driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[6]/a')
        a.click()
        time.sleep(5)
        assert True

    def test_page_and_send_info(self):
            a = self.driver.find_element_by_xpath("/html/body/div[6]/div/div[1]/div[2]/ul/li[5]/a")
            a.click()
            time.sleep(2)
            name = self.driver.find_element_by_xpath('//input[@name="Name"]')
            time.sleep(2)
            name.send_keys('Vikas')
            time.sleep(2)
            email = self.driver.find_element_by_name("Email")
            time.sleep(2)
            email.send_keys('testingMailID@mail.com')
            time.sleep(2)
            select = Select(self.driver.find_element_by_class_name("form-control"))
            time.sleep(2)
            select.select_by_visible_text('Student')
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@value='Submit']").click()
            time.sleep(2)
            assert True

    def tearDown(self):
        self.driver.close()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Programming/Programming fundamentals/python projects/Sparks internship testing/Web Testing/reports'))
