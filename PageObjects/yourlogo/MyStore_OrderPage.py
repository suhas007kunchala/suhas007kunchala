from helpers.helper_base import Helperbase


class Orderpage:

    def __init__(self, hb: Helperbase):
        self.driver = hb
        self.proceedtocheckout_summary = self.driver.findxpath("//p/a[@title='Proceed to checkout']")
        self.proceedtocheckout_address = self.driver.findxpath("//span[text()='Proceed to checkout']")
        self.proceedtocheckout_shipping = self.driver.findxpath("//button[@name='processCarrier']")
        self.agreecheckbox = self.driver.findid("cgv")
        self.paybywire = self.driver.findxpath("//a[@class='bankwire']")
        self.confirmorder = self.driver.findxpath("//span[text()='I confirm my order']")
        self.verifysuccess = self.driver.findxpath("//strong[contains(text(),'Your order on My Store is complete.')]")

    def clickproceedtocheckout(self, stage):
        match stage:
            case "summary":
                self.driver.mousedown()
                return self.driver.btnclick_xpath(self.proceedtocheckout_summary)
            case "address":
                self.driver.mousedown()
                return self.driver.btnclick_xpath(self.proceedtocheckout_address)
            case "shipping":
                self.driver.mousedown()
                return self.driver.btnclick_xpath(self.proceedtocheckout_shipping)

    def checktermsandconditions(self):
        self.driver.mousedown()
        self.driver.checkbox_id(self.agreecheckbox)

    def clickpaybywire(self):
        self.driver.btnclick_xpath(self.paybywire)

    def clickconfirmord(self):
        self.driver.btnclick_xpath(self.confirmorder)

    def validateorder(self):
        assert self.driver.gettext_xpath(self.verifysuccess).__eq__("Your order on My Store is complete.")
