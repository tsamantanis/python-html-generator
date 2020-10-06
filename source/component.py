class Component():
    def __init__(self, tag, class_name, id, content):
        """Initialize instance of Component class with class_name, id, and content properties"""
        self.tag = tag
        self.class_name = class_name
        self.id = id
        self._content = content

    def get_html(self):
        """Recursively produces and returns html code for component and its content"""
        res = ""
        if type(self._content).__name__ == 'str':
            return "<" + self.tag + " class=\"" + self.class_name + "\" id=\"" + self.id + "\"> \n" + self._content + "\n</" + self.tag + ">"
        else:
            for content in self._content:
                res += content.get_html() + "\n"
            return "<" + self.tag + " class=\"" + self.class_name + "\" id=\"" + self.id + "\"> \n" + res + "\n</" + self.tag + ">"

    def get_content(self):
        """Returns contents of the component"""
        return self._content
        
    def update_content(self, content):
        """Update component content"""
        self._content = content

    def to_file(self, filename):
        """Create html file and print get_html content in it"""
        print("\n\nCreating HTML file...\n\n")
        file = open(filename,"w+")
        print("Writing HTML to file...\n\n")
        file.write(self.get_html())
        file.close()
        print("File creation complete!\n\n")
