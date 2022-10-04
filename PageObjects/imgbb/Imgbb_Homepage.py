from helpers.helper_base import Helperbase
from helpers.autoit import runautoit


class homepage:
    def __init__(self, hb: Helperbase):
        self.driver = hb
        self.startuploadbtn = self.driver.findxpath("//a[contains(text(),'Start uploading')]")
        self.submitbtn = self.driver.findxpath(
            "//body/div[@id='anywhere-upload']/div[1]/div[1]/div[2]/div[1]/button[1]")
        self.uploadstatus = self.driver.findxpath("//div[contains(text(),'Upload complete')]")

    def clickstartuploadbtn(self):
        self.driver.btnclick_xpath(self.startuploadbtn)

    def fileupload(self, filepath):
        runautoit(filepath)

    def submitfilebtn(self):
        self.driver._page.pause()
        self.driver.btnclick_xpath(self.submitbtn)

    def validateuploadstatus(self):
        self.driver.gettext_xpath(self.uploadstatus).__eq__("Upload complete")

    def imgbbsite(self, url):
        self.driver.visturl(url)
