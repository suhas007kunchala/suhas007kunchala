from helpers.helper_base import Helperbase


class Homepage:

    def __init__(self, hb: Helperbase):

        self.driver = hb
        self.homebth = self.driver.findxpath("//header/div[3]/div[1]/div[1]/div[1]/a[1]/img[1]")
        self.womentab = self.driver.findxpath("//a[@title='Women']")
        self.dressestab = self.driver.findcss_has("li:has(ul.submenu-container clearfix first-in-line-xs)")
        self.tshirtstab = self.driver.findxpath("//ul/li[3]/a[@title='T-shirts']")
        self.searchbox = self.driver.findxpath("//form[@id='searchbox']/child::input[4]")
        self.searchbtn = self.driver.findxpath("//button[@name='submit_search']")
        self.yourlogotwitter = self.driver.findxpath("//body/div[@id='page']/div[3]/footer[1]/div[1]/section[1]/ul["
                                                     "1]/li[2]/a[1]")

    def searchproducts(self, txt: str):
        self.driver.filltext_xpath(self.searchbox, txt)
        self.driver.btnclick_xpath(self.searchbtn)

    def clickwomentab(self, tab: str):
        match tab:
            case "women":
                return self.driver.btnclick_xpath(self.womentab)

            case "dresses":
                return self.driver.btnclick_xpath(self.dressestab)

            case "tshirt":
                return self.driver.btnclick_xpath(self.tshirtstab)

    def clickhomebtn(self):
        self.driver.btnclick_xpath(self.homebth)

    def clicktwitter(self):
        box = self.driver.getboundingbox(self.yourlogotwitter)
        self.driver.mousewheel(box["x"], box["y"])
        self.driver.handlenewpages(self.yourlogotwitter)

    def yourlogowindow(self):
        tabs = self.driver.handlemultiplepages()
        tabs[0].bring_to_front()
        self.clickhomebtn()
