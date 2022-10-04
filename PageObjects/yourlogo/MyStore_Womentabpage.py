from helpers.helper_base import Helperbase


class Womenpage:

    def __init__(self, hb: Helperbase):
        self.driver = hb
        # checkboxes
        self.topscb = self.driver.findxpath("//input[@id='layered_category_4']")
        self.sortbydropdown = self.driver.findxpath("//select[@id='selectProductSort']")
        self.priceslider = self.driver.findxpath("//div[@class='layered_slider_container']/div[1]/div[1]")
        self.rangelow = self.driver.findxpath("//div[@class='layered_slider_container']/div/child::a[1]")
        self.rangehigh = self.driver.findxpath("//div[@class='layered_slider_container']/div/child::a[2]")
        self.productimg = self.driver.findxpath("//a[@class='product_img_link']/img[@title='Blouse']")
        self.quickview = self.driver.findxpath("//a[@class='quick-view']/span")
        self.productframe = self.driver.findxpath("//html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/iframe[1]")
        self.sizedropdown = self.driver.findxpath("//select[@id='group_1']")
        self.addtocarft = self.driver.findxpath("//button[@name='Submit']")
        self.proceedtocheckout = self.driver.findxpath("//a[@title='Proceed to checkout']/span")
        self.pricerange = self.driver.findxpath("//span[@id='layered_price_range']")
        self.sliderbox = None
        self.range = None

    def topscheckbox(self):
        self.driver.get_element_into_view(self.topscb)
        self.driver.checkbox_xpath(self.topscb)

    def sort_by(self, value):
        self.driver.get_element_into_view(self.sortbydropdown)
        self.driver.selectopts_label(self.sortbydropdown, value)

    def price_slider(self):
        self.sliderbox = self.driver.getboundingbox(self.priceslider)
        return self.sliderbox

    def getpricerange(self):
        self.range = self.driver.gettext_xpath(self.pricerange)

    def sliderlow(self, amt):
        self.driver.get_element_into_view(self.rangelow)
        self.getpricerange()
        while float(str(self.range).split("-")[0].removeprefix('$')) < float(amt):
            self.sliderbox = self.driver.getboundingbox(self.rangelow)
            self.driver.dargslider(self.rangelow, self.sliderbox, float(amt))
            self.getpricerange()

    def sliderhigh(self, amt):
        self.sliderbox = self.driver.getboundingbox(self.rangehigh)
        self.driver.dargslider(self.rangehigh, self.sliderbox, float(amt))

    def hoverover(self):
        self.driver.locatorhover(self.productimg, force=True)

    def clickquickview(self):
        self.driver.btnclick_xpath(self.quickview)

    def selectsize(self, val):
        self.driver.frame_selectopts_index(self.productframe, self.sizedropdown, val)

    def clickaddtocart(self):
        self.driver.frame_btnclick_xpath(self.productframe, self.addtocarft)

    def clickcheckout(self):
        self.driver.btnclick_xpath(self.proceedtocheckout)
