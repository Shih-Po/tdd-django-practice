from django.test import LiveServerTestCase
from selenium import webdriver
# for firefox 47.0
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

# here we start to build a user story

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        caps = DesiredCapabilities.FIREFOX
        caps["marionette"] = True
        self.browser = webdriver.Firefox(capabilities=caps)

        # set an easy wait
        self.browser.implicitly_wait(6)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Emily heard an cool todo app
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices "To-Do" in title of the website
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She inputs 'Buy a basketball'
        inputbox.send_keys('Buy a basketball')

        # When she hits enter, she is taken to a new URL:
        # 1. Buy a basketball
        inputbox.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(6)

        emily_list_url = self.browser.current_url
        self.assertRegex(emily_list_url, '/lists/.+')

        self.check_for_row_in_list_table('1: Buy a basketball')

        # Now there still has an text bar to let her add other todos
        # She inputs 'Call friends to play basketball'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Call friends to play basketball')
        inputbox.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(6)

        # The page updates again, and now show both items on her list
        self.check_for_row_in_list_table('1: Buy a basketball')
        self.check_for_row_in_list_table('2: Call friends to play basketball')

        # Now a new user Francis comes

        ## We use an new browser process to confirm
        ## Any information about Emily will not present by cookies or other ways
        self.browser.quit()
        caps = DesiredCapabilities.FIREFOX
        caps["marionette"] = True
        self.browser = webdriver.Firefox(capabilities=caps)

        # Francis go to the homepage
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy a basketball', page_text)
        self.assertNotIn('Call friends to play basketball', page_text)

        # Francis input an new item, make a new list
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(6)

        # Francis get his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotIn(francis_list_url, emily_list_url)

        # There still no emily's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Call friends to play basketball', page_text)
        self.assertIn('Buy milk')

        # He quits happily
        self.fail('Finish the test!')


