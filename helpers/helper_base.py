from playwright.sync_api import sync_playwright, BrowserType, expect, Dialog, Download


class Helperbase:
    def __init__(self):
        self.all_pages = None
        self.new_page = None
        self.we_selectopt = None
        self.we_slider = None
        self.we_has = None
        self.css_hastext = None
        self.xpath = None
        self.cssattr = None
        self.we_id = None
        self.we_css_hastext = None
        self.we_cssattr = None
        self.we_xpath = None
        # self._dialog = Dialog(sync_playwright)
        self._p = sync_playwright().start()
        self._browser = self._p.chromium.launch(headless=False, slow_mo=5000)
        self._browsercontext = self._browser.new_context()
        self._page = self._browsercontext.new_page()

    def gotourl(self, url):
        self._page.goto(url)

    def closebrowser(self):
        self._browser.close()

    def stopplaywright(self):
        self._p.stop()

    # selector section

    def findxpath(self, xpath):
        self.we_xpath = xpath
        return self.we_xpath

    def findcssattr(self, attr: str):
        self.we_cssattr = '[{0}={1}]'.format(attr.split("=")[0], attr.split("=")[1])
        return self.we_cssattr

    def findcss_hastext(self, tag: str, txt: str):
        self.we_css_hastext = '{0}, has_text={1}'.format(tag, txt)
        return self.css_hastext

    def findid(self, val):
        self.we_id = 'id={0}'.format(val)
        return self.we_id

    def findcss_has(self, attr):
        self.we_has = '{0}:has({1})'.format(attr.split(":")[0], attr.split(":")[1])
        return self.we_has

    # Input section

    def btnclick_id(self, id):
        self.we_id = self._page.locator('id={0}'.format(id))
        return self.we_id.click()

    def btnclick_cssattr(self, attr):
        self.we_cssattr = self._page.locator('[{0}={1}]'.format(attr.split("=")[0], attr.split("=")[1]))
        return self.we_cssattr.click()

    def presskeyboard(self, key):
        return self._page.keyboard.press(key)

    def btnclick_xpath(self, xpath):
        self.we_xpath = self._page.locator(xpath)
        return self.we_xpath.click()

    def filltext_id(self, id: str, txt):
        self.we_id = self._page.locator('id={0}'.format(id))
        return self.we_id.fill(txt)

    def filltext_xpath(self, xpath: str, txt: str):
        self.we_xpath = self._page.locator(xpath)
        return self.we_xpath.fill(txt)

    def filltext_cssattr(self, attr, txt):
        self.we_cssattr = self._page.locator('[{0}={1}]'.format(attr.split("=")[0], attr.split("=")[1]))
        return self.we_cssattr.fill(txt)

    def upload_files(self, selector, filepath):
        self._page.set_input_files(selector, filepath)

    def upload_files_windows(self, element, filepath):
        with self._page.expect_file_chooser() as fc_info:
            self._page.click(element)
        file_chooser = fc_info.value
        file_chooser.set_files(filepath)

    def dargslider(self, attr, boxsize, amt):
        x = boxsize["x"]
        y = boxsize["y"]
        self.mousemove(x + boxsize["width"] / 2, y + boxsize["height"] / 2)
        self.mousedown()
        self.mousemove(x + 15, y + boxsize["height"] / 2)
        self.mouseup()

    def selectopts_value(self, selector, val):
        self.we_selectopt = self._page.locator(selector).select_option(value='In stock')
        # self.we_selectopt.click()
        # return self.we_selectopt

    def selectopts_label(self, selector, value):
        self.we_selectopt = self._page.locator(selector).select_option(label=value)
        # return self.we_selectopt

    def selectopts_index(self, selector, ind):
        self.we_selectopt = self._page.locator(selector).select_option(index=ind)

    def selectopts_multi(self, selector, value: list):
        self.we_selectopt = self._page.locator(selector).select_option(value)
        return self.we_selectopt

    def checkbox_xpath(self, xpath):
        self._page.check(self.findxpath(xpath))

    def checkbox_id(self, i_d):
        self._page.check(i_d)

    def uncheckbox_xpath(self, xpath):
        self._page.uncheck(self.findxpath(xpath))

    def mouseclick(self, x: float, y: float, **kwargs):
        self._page.mouse.click(x, y, **kwargs)

    def mousedblclick(self, x: float, y: float, **kwargs):
        self._page.mouse.dblclick(x, y, **kwargs)

    def mousewheel(self, x, y):
        self._page.mouse.wheel(x, y)

    def mousemove(self, x, y, **kwargs):
        self._page.mouse.move(x, y, **kwargs)

    def mouseup(self, **kwargs):
        self._page.mouse.up(**kwargs)

    def mousedown(self, **kwargs):
        self._page.mouse.down(**kwargs)

    # WebElements interaction

    def gettext_xpath(self, xpath):
        self.we_xpath = self._page.locator(xpath)
        return self.we_xpath.text_content()

    def locatorhover(self, xpath, **kwargs):
        self._page.locator(xpath).hover(**kwargs)

    def getboundingbox(self, element):
        return self._page.locator(element).bounding_box()

    def getframes(self, selector):
        return self._page.frame_locator(selector)

    def get_element_into_view(self, selector):
        self._page.locator(selector).scroll_into_view_if_needed()

    # Frame interactions

    def frame_getelement(self, frame, selector):
        ele = self.getframes(frame).locator(selector)
        return ele

    def frame_selectopts_index(self, frame, selector, ind):
        self.frame_getelement(frame, selector).select_option(index=ind)

    def frame_btnclick_xpath(self, frame, selector):
        self.getframes(frame).locator(selector).click()

    # Navigation

    def visturl(self, url):
        self._page.goto(url)

    def handlenewpages(self, selector):
        with self._browsercontext.expect_page() as new_page_info:
            self._page.click(selector)
        self.new_page = new_page_info.value
        self.new_page.wait_for_load_state()
        self.new_page.bring_to_front()

    def handlemultiplepages(self):
        self.all_pages = self._browsercontext.pages
        return self.all_pages

    # Handling chrome extensions
    def handle_extensions(self, playwright, path_to_extensions, user_data):
        context = playwright.chromium.launch_persistent_context(
            user_data_dir=user_data,
            headless=False,
            args=[
                f"--disable-extensions-expect={path_to_extensions}",
                f"--load-extension={path_to_extensions}"
            ]
        )
        background_page = context.background_pages[0]
        context.close()

    # BrowserType
    def connect_to_existing_browser(self, ws_endpoint, **kwargs):
        with sync_playwright() as p:
            p.chromium.connect(ws_endpoint)

    def connect_cdp(self, endpoint_url, **kwargs):
        with sync_playwright() as p:
            p.chromium.connect_over_cdp(endpoint_url, **kwargs)

    # Browser Context
    # event emitted when background page loaded
    def waitfor_backgroundpage(self):
        background_page = self._browsercontext.wait_for_event("backgroundpage")
        return background_page

    # event emitted when browser context is closed
    def waitfor_browserclose(self):
        self._browsercontext.wait_for_event("close")

    # event emitted when new page is created in browser context
    def onevent_NewPage(self, selector):
        with self._browsercontext.expect_page() as page_info:
            self._page.click(selector)
        newpage = page_info.value
        return newpage

    # event emitted when request made in browser context
    def onevent_Request(self, fun):
        self._browsercontext.on("request", fun)

    # event emitted when request failed in browser context
    def onevent_RequestFailed(self, fun):
        self._browsercontext.on("requestfailed", fun)

    # event emitted when request finished in browser context
    def onevent_RequestFinished(self, fun):
        self._browsercontext.on("requestfinished", fun)

    # event emitted when response status and headers are recevied
    def onevent_response(self, fun):
        self._browsercontext.on("response", fun)

    # Handle Assertions
    def assert_By_expect(self, *args):
        self.assertionargs = list(args)
        return expect(self.assertionargs[0])

    # Handle Dialog
    def acceptdialog(self, **kwargs):
        self._dialog.accept()

    def dismissdialog(self, **kwargs):
        self._dialog.dismiss()

    def getdialogmessage(self):
        return self._dialog.message

    def getdialogtype(self):
        return self._dialog.type

    # Handle Downloads
    def cancel_download(self, element):
        with self._page.expect_download() as download_info:
            self._page.click(element)
        download = download_info.value
        download.cancel()

    def delete_download(self, element):
        with self._page.expect_download() as download_info:
            self._page.click(element)
        download = download_info.value
        download.delete()

    def failure_download(self, element):
        with self._page.expect_download() as download_info:
            self._page.click(element)
        download = download_info.value
        download.failure()

    def getpage_download(self, element):
        with self._page.expect_download() as download_info:
            self._page.click(element)
        download = download_info.value
        return download.page

    def getpath_download(self, element):
        with self._page.expect_download() as download_info:
            self._page.click(element)
        download = download_info.value
        return download.path()

    def saveas_download(self, element, path):
        with self._page.expect_download() as download_info:
            self._page.click(element)
        download = download_info.value
        download.save_as(path)

    def geturl_download(self, element):
        with self._page.expect_download() as download_info:
            self._page.click(element)
        download = download_info.value
        return download.url
