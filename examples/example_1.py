import sys
sys.path.insert(1, '../source')
from a import A
from component import Component
from html import HTML
from link import Link
from meta import Meta
from style import Style

# Create Meta instance
meta = Meta(
    tag="meta",
    class_name="",
    id="meta",
    charset='utf-8',
    name="description",
    content="Python HTML generator"
)

# Create Link instances for styles and fonts
link_styles = Link(
    tag="link",
    class_name="",
    id="link_styles",
    href="",
    rel="stylesheet",
    referrerpolicy="noreferrer",
    type="text/css"
)
link_comfortaa = Link(
    tag="link",
    class_name="",
    id="link_comfortaa",
    href="https://fonts.googleapis.com/css2?family=Comfortaa&display=swap",
    rel="stylesheet",
    referrerpolicy="noreferrer",
    type=""
)
link_montserrat = Link(
    tag="link",
    class_name="",
    id="link_montserrat",
    href="https://fonts.googleapis.com/css2?family=Montserrat+Alternates:wght@500&display=swap",
    rel="stylesheet",
    referrerpolicy="noreferrer",
    type=""
)
link_raleway = Link(
    tag="link",
    class_name="",
    id="link_raleway",
    href="https://fonts.googleapis.com/css2?family=Raleway&display=swap",
    rel="stylesheet",
    referrerpolicy="noreferrer",
    type=""
)

# Create Head instance
head = Component(
    tag="head",
    class_name="",
    id="head",
    content=[meta, link_styles, link_comfortaa, link_montserrat, link_raleway]
)

# Create Nav instance
nav = Component(
    tag="nav",
    class_name="nav_styles",
    id="nav",
    content=""
)

# Create P instances
p = Component(
    tag="p",
    class_name="p_styles",
    id="text",
    content="Hello World"
)

p1 = Component(
    tag="p",
    class_name="p_styles",
    id="text",
    content="I am somehow found in this html code"
)

p2 = Component(
    tag="p",
    class_name="p_styles",
    id="text",
    content="even though I was initially created in Python"
)

p_style_properties = {
    "font-size": "18",
    "font-weight": "600",
    "color": "blue"
}
p_styles = Style(p.tag, p_style_properties)

p.update_content("Hello, my name is Ducky!")
p1.update_content("I am somehow found in this html code,")
p2.update_content("even though I was initially created in Python!")

# Create Div instance
div = Component(
    tag="div",
    class_name="",
    id="div_styles",
    content=[p, p1, p2]
)

# Create Body instance
body = Component(
    tag="body",
    class_name="",
    id="body_styles",
    content=[nav, div]
)

# Create HTML instance
html = HTML(
    tag="html",
    class_name="",
    id="html_styles",
    content=[head, body],
    lang="en",
    xmlns="http://www.w3.org/1999/xhtml"
)

link_styles.set_href("styles.css")

html.to_file("example_1.html")
p_styles.to_file("styles.css")
