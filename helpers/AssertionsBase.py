from helpers.helper_base import Helperbase

"""
    
"""


class Assertion(Helperbase):
    def should_not_be_checked(self, locator, **kwargs):
        self.assert_By_expect(locator).not_to_be_checked(**kwargs)

    def should_not_be_disabled(self, locator, **kwargs):
        self.assert_By_expect(locator).not_to_be_disabled(**kwargs)

    def should_not_be_editable(self, locator, **kwargs):
        self.assert_By_expect(locator).not_to_be_editable(**kwargs)

    def should_not_be_enabled(self, locator, **kwargs):
        self.assert_By_expect(locator).not_to_be_enabled(**kwargs)

    def should_not_be_empty(self, locator, **kwargs):
        self.assert_By_expect(locator).not_to_be_empty(**kwargs)

    def should_not_be_focused(self, locator, **kwargs):
        self.assert_By_expect(locator).not_to_be_focused(**kwargs)

    def should_not_be_hidden(self, locator, **kwargs):
        self.assert_By_expect(locator).not_to_be_hidden(**kwargs)

    def should_not_be_visible(self,locator, **kwargs):
        self.assert_By_expect(locator).not_to_be_visible()

    def should_not_contain_text(self,locator, expected,**kwargs):
        self.assert_By_expect(locator).not_to_contain_text(expected,**kwargs)

