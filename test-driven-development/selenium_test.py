import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()


class InputTesting(TestCase):
    BLOG_URL = "https://login.pwr.edu.pl/auth/realms/pwr.edu.pl/protocol/cas/login?service=https%3A%2F%2Fweb.usos.pwr.edu.pl%2Fkontroler.php%3F_action%3Dlogowaniecas%2Findex%26callback%3DK7YyNrdS0s%252FOzyspys9JLdIryCiwj09MLsnMz7PNTixJzMlPN9LPzEtJrVCyBgA%253D4a359a7facdbed51a7082a46269dcd560c5dd739&locale=pl"
    INPUT_NAME = "username"
    INPUT_NAME_PASSWORD = "password"
    BUTTON_NAME = "clear"

    def test_clear_button(self):
        self.driver.get(self.BLOG_URL)
        try:
            login_box = self.driver.find_element(by=By.NAME, value=self.INPUT_NAME)
            password_box = self.driver.find_element(by=By.NAME, value=self.INPUT_NAME_PASSWORD)
            clear_button = self.driver.find_element(by=By.NAME, value=self.BUTTON_NAME)
        except Exception:
            self.fail("Login input not found")

        login_box.send_keys("your_username")
        password_box.send_keys("your_password")
        clear_button.click()

        input_value = login_box.get_attribute("value")
        self.assertEqual("", input_value)


if __name__ == '__main__':
    unittest.main()
