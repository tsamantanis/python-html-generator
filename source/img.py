from component import Component
class Img(Component):
    def __init__(self, tag, class_name, id, src, alt, width, height):
        """Initialize instance of Img class with charset, name, and content properties"""
        super().__init__(tag, class_name, id, content="")
        self.src = src
        self.alt = alt
        self.width = width
        self.height = height


    def get_html(self):
        """Override component get_html method to include unique properties"""
        return "<" + self.tag + " class=\"" + self.class_name + "\" id=\"" + self.id + "\"" + " src=\""  + self.src + "\"" +  " alt=\"" + self.alt + "\"" + " width=\"" + self.width + "\"" + " height=\"" + self.height + "\"" + " />" + "\n"
