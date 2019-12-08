from selenium import webdriver
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

        # She is invited to add her salary straight away
        self.fail("Finish the functional tests!")
        # Testing out her desired salary of $100,000, she types it in to the
        # text field and presses ENTER.

        # Bonnie notices that the page now lists her Salary
        # alongside the amount of Tax that Bonnie can expect to pay

        # Shocked by the amount of Tax on that Salary, Bonnie enters a lower 
        # salary of $80,000 and presses ENTER.

        # Bonnie notices that both the Salary and Tax displayed have updated
        # to reflect her lower salary.