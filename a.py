from component import Component
from ref import Ref
class A(Component, Ref):
    def __init__(self, tag, class_name, id, href, rel, referrerpolicy, target):
        """Initialize instance of A class with tag, class_name, id, href, rel, referrerpolicy, and target properties"""
        Component.__init__(tag, class_name, id)
        Ref.__init__(href, rel, referrerpolicy)
        self.target = target

    def get_html(self):
        """Override component get_html method to include unique properties"""
        return "<" + self.tag + " class=\"" + self.class_name + "\" id=\"" + self.id + "\"" + " href=\"" + self.href + "\"" +  " rel=\"" + self.rel + "\"" + " referrerpolicy=\"" + self.referrerpolicy + "\"" + " target=\"" + self.target + "\"" + " />"
