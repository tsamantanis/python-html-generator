from component import Component
class HTML(Component):
    def __init__(self, tag, class_name, id, content, lang, xmlns):
        """Initialize HTML class instance with head and body properties"""
        super().__init__(tag, class_name, id, content)
        self.lang = lang
        self.xmlns = xmlns

    def get_html(self):
        """Override component get_html method to include unique properties"""
        content_html = ""
        for content_item in self._content:
            content_html += content_item.get_html() + "\n"
        return "<" + self.tag + " class=\"" + self.class_name + "\" id=\"" + self.id + "\"" + " lang=\"" + self.lang + "\"" +  " xmlns=\"" + self.xmlns + "\"" + ">\n" + content_html + "\n</html>"
