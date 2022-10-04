from helpers.helper_base import Helperbase


class twitterpage:
    def __init__(self, hb: Helperbase):
        self.driver = hb
        self.followbtn = self.driver.findxpath("//div[@class='css-1dbjc4n r-6gpygo']/div/div/span/span")

    def clickfollowbtn(self):
        self.driver.new_page.locator(self.followbtn).click()