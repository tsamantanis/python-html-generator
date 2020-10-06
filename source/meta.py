from component import Component
class Meta(Component):
    def __init__(self, tag, class_name, id, charset, name, content):
        """Initialize instance of Meta class with charset, name, and content properties"""
        super().__init__(tag, class_name, id, content="")
        self.charset = charset
        self.name = name
        self.content = content

    def get_html(self):
        """Override component get_html method to include unique properties"""
        return "<" + self.tag + " class=\"" + self.class_name + "\" id=\"" + self.id + "\"" + " charset=\""  + self.charset + "\"" +  " name=\"" + self.name + "\"" + " content=\"" + self.content + "\""+ " />" + "\n"
