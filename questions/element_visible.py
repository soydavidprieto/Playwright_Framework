# questions/element_visible.py
from abilities.browser import BrowseTheWeb

class ElementVisible:
    def __init__(self, selector: str):
        self.selector = selector

    def answered_by(self, actor):
        page = actor.ability_to(BrowseTheWeb).page
        try:
            page.wait_for_selector(self.selector, timeout=10000)
            return page.is_visible(self.selector)
        except Exception:
            page.screenshot(path=f"reports/failure_{self.selector}.png")
            return False