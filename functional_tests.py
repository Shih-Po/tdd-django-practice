from selenium import webdriver
# for firefox 47.0
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest

from selenium.webdriver.common.keys import Keys

# here we start to build a user story

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        caps = DesiredCapabilities.FIREFOX
        caps["marionette"] = True
        self.browser = webdriver.Firefox(capabilities=caps)

        # set a easy wait
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Emily heard an cool todo app
        # She checks her web
        self.browser.get('http://localhost:8000')

        # She founds "To-Do" in tile of the website
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She creates one thing that she has todo by the invitation
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She inputs 'Buy a basketball'
        input_box.send_keys('Buy a basketball')

        # While she presses enter, website renews and lists out:
        # 1. Buy a basketball
        input_box.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy a basketball')

        # Now there still has an text bar to let her add other todos
        # She inputs 'Call friends to play basketball'
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Call friends to play basketball')
        input_box.send_keys(Keys.ENTER)

        # Website renews again, now she has 2 todo lists
        self.check_for_row_in_list_table('1: Buy a basketball')
        self.check_for_row_in_list_table('2: Call friends to play basketball')

        # Emily dosen't know if this website can remember her todos
        # She sees this website send an unique URL to her
        # Website give some description for this feature

        # She goes to this URL - Her todos still there.

        # She quits happily
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')