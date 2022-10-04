from helpers.configreader import Configreader
from helpers.helper_base import Helperbase


class loginmodule:
    loginobjs = Configreader("LoginObjects")

    def __init__(self, hb: Helperbase):
        self.driver = hb
        self.signin_btn = self.loginobjs.getData("signin_css")
        self.signout_btn = self.loginobjs.getData("logout_css")
        self.emailaddress = self.loginobjs.getData("email_id")
        self.password = self.loginobjs.getData("password_id")
        self.submit_btn = self.loginobjs.getData("signsubmit_xpath")
        self.loginsuccess = self.loginobjs.getData("loginsuccess_xpath")
        self.loginsuccessmsg = None
        # self.loginsuccess= self.loginobjs.getData("loginsuccess")
        # self.yourlogosite()
        # self.clicklogin()
        # self.enteremail()

    def yourlogosite(self, site):
        self.driver.gotourl(site)

    def clicksingin(self):
        self.driver.btnclick_cssattr(self.signin_btn)

    def enteremail(self, email: str):
        self.driver.filltext_id(self.emailaddress, email)

    def enterpassword(self, password):
        self.driver.filltext_id(self.password, password)

    def clicklogin(self):
        self.driver.get_element_into_view(self.submit_btn)
        self.driver.btnclick_xpath(self.submit_btn)
        self.loginmsg()

    def loginmsg(self):
        self.loginsuccessmsg = self.driver.gettext_xpath(self.loginsuccess)
        return self.loginsuccessmsg

    def logout(self):
        self.driver.btnclick_xpath(self.signout_btn)
