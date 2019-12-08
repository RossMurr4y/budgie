from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_budget_and_calculate_tax(self):

        # Bonnie the Budgerigar has heard about an awesome new budgeting app.
        # She goes online to check out it's homepage.
        self.browser.get('http://localhost:8000')

        # She notices the page title and header indicate that she is on the
        # Budgie Budget Site.
        self.assertIn('Budgie Budget', self.browser.title)

        # She notices that there is a header for the top of the Budget
        header_text = self.browser.find_element_by_id('h1').text
        self.assertIn('Salary:', header_text)

        # She is invited to add her salary straight away
        inputbox = self.browser.find_element_by_id('id_salary')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'What is your current Annual Salary?'
        )

        # Testing out her desired salary of $100,000, she types it in to the
        # text field and presses ENTER.
        salary_amount = 100000
        inputbox.send_keys(salary_amount)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Bonnie notices that the page now lists her Salary
        # alongside the amount of Tax that Bonnie can expect to pay
        displayed_salary = self.browser.find_element_by_id('id_salary_amount')
        displayed_tax = self.browser.find_element_by_id('id_tax_displayed')
        self.assertEqual(displayed_salary, salary_amount)
        self.assertEqual(displayed_tax, "24497")

        # Shocked by the amount of Tax on that Salary, Bonnie enters a lower 
        # salary of $80,000 and presses ENTER.
        new_salary_amount = 80000
        inputbox.send_keys(new_salary_amount)
        inputbox.send_keys(Keys.ENTER)
        time.slee(1)

        # Bonnie notices that both the Salary and Tax displayed have updated
        # to reflect her lower salary.
        new_displayed_salary = self.browser.find_element_by_id('id_salary_amount')
        new_displayed_tax = self.browser.find_element_by_id('id_tax_displayed')
        self.assertEqual(new_displayed_salary, new_salary_amount)
        self.assertEqual(new_displayed_tax, "17547")

        self.fail("Finish the functional tests!")