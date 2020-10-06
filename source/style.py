class Style():
    def __init__(self, selector, properties):
        """Initialize instance of Style class with properties and id properties."""
        self.selector = selector
        self.properties = properties

    def get_css(self):
        """Returns CSS code for style"""
        css = ""
        for key in self.properties:
            css += "\t" + key + ": " + self.properties[key] + ";\n"
        body = " {\n" + css + "}"
        return "\n" + self.selector + body

    def to_file(self, filename):
        """Create css file and print get_css content in it"""
        print("\n\nOpening CSS file...\n\n")
        file = open(filename,"w+")
        print("Updating CSS file...\n\n")
        file.write(self.get_css())
        file.close()
        print("File update complete!\n\n")

    def add_to_file(self, filename):
        """Add content to existing to css file"""
        print("\n\nCreating CSS file...\n\n")
        file = open(filename,"a")
        print("Writing CSS to file...\n\n")
        file.write(self.get_css())
        file.close()
        print("File creation complete!\n\n")
