from abc import ABC
class Ref(ABC):
    def __init__(self, href, rel, referrerpolicy):
        """Initialize Text abstract class"""
        # Reference proprerties should be protected so they can be changed in subclasses but not publicly
        self._href = href
        self._rel = rel
        self._referrerpolicy = referrerpolicy

    def get_href(self):
        """Returns href attribute value"""
        return self._href

    def get_rel(self):
        """Returns rel attribute value"""
        return self._rel

    def get_referrerpolicy(self):
        """Returns referrerpolicy attribute value"""
        return self._referrerpolicy
