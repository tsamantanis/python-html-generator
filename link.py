from component import Component
from ref import Ref
class Link(Component, Ref):
    def __init__(self, tag, class_name, id, href, rel, referrerpolicy, crossorigin):
        """Initialize instance of Link class with tag, class_name, id, href, rel, referrerpolicy, and crossorigin properties"""
        Component.__init__(self, tag, class_name, id, content="")
        Ref.__init__(self, href, rel, referrerpolicy)
        self.crossorigin = crossorigin

    def get_html(self):
        """Override component get_html method to include unique properties"""
        return "<" + self.tag + " class=\"" + self.class_name + "\" id=\"" + self.id + "\"" + " href=\"" + self._href + "\"" +  " rel=\"" + self._rel + "\"" + " referrerpolicy=\"" + self._referrerpolicy + "\"" + " crossorigin=\"" + self.crossorigin + "\"" + " />"
