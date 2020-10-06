import sys
sys.path.insert(1, '../source')
from a import A
from component import Component
from html import HTML
from img import Img
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
    content=[
        Component(
            tag="div",
            class_name="flex",
            id="nav_div",
            content=[
                A(
                    tag="a",
                    class_name="logo text-white",
                    id="nav_home",
                    content="Home",
                    href="/",
                    rel="",
                    referrerpolicy="",
                    target=""
                ),
                A(
                    tag="a",
                    class_name="",
                    id="nav_about",
                    content="About",
                    href="/about",
                    rel="",
                    referrerpolicy="",
                    target=""
                )
            ]
        ),
        Component(
            tag="button",
            class_name="button bg-green bg-green-hover mr-1 button-header",
            id="nav_button",
            content="Action"
        )
    ]
)

# Create P instances
heading_1 = Component(
    tag="h1",
    class_name="heading_1",
    id="text",
    content="Hello World"
)

p1 = Component(
    tag="p",
    class_name="p_styles",
    id="text",
    content="This code was translated from Python"
)


p_style_properties = {
    "font-size": "18",
    "font-weight": "600",
}
p_styles = Style(p1.tag, p_style_properties)

# Create Sections

section_1 = Component(
    tag="section",
    class_name="",
    id="section_1",
    content=[
        Component(
            tag="div",
            class_name="",
            id="div_styles",
            content=[heading_1, p1]
        )
    ]
)

section_2 = Component(
    tag="section",
    class_name="section_2",
    id="section_2",
    content=[
        Component(
            tag="div",
            class_name="",
            id="section_2_div_styles",
            content=[
                Component(
                    tag="h2",
                    class_name="",
                    id="heading_section_2",
                    content="This is a section"
                ),
                Component(
                    tag="p",
                    class_name="p_styles",
                    id="text_section_2",
                    content="It happens to be super cool"
                ),
                Img(
                    tag="img",
                    class_name="img_styles",
                    id="img",
                    src="https://images.theconversation.com/files/337593/original/file-20200526-106811-ql6d51.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1356&h=668&fit=crop",
                    alt="Llama Face",
                    width="600",
                    height="300"
                ),
                Component(
                    tag="p",
                    class_name="p_styles",
                    id="text_section_2",
                    content="Here's a llama ^ for no particular reason"
                ),
            ]
        )
    ]
)

# Create Body instance
body = Component(
    tag="body",
    class_name="",
    id="body_styles",
    content=[nav, section_1, section_2]
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

html.to_file("example_2.html")
p_styles.to_file("styles.css")

body_styles = Style(body.tag, {
    "color": "#222",
    "font-family": "\"Raleway\", sans-serif",
    "margin": "0",
    "padding": "0",
    "position": "relative",
    "padding-bottom": "100px",
    "width": "1100px",
    "display": "flex",
    "flex-direction": "column",
    "justify-content": "flex-start",
    "align-items": "center",
    "margin": "auto",
    "margin-top": "20px",
    "min-height": "100vh",
})

nav_styles = Style(nav.tag, {
    "width": "100%",
    "padding": "0",
    "margin": "0",
    "min-height": "60px",
    "display": "flex",
    "align-items": "center",
    "justify-content": "space-between",
    "background-color": "#229954",
    "top": "0",
    "left": "0",
    "box-shadow": "0 4px 8px 0 rgba(0,0,0,0.2)",
    "position": "sticky",
    "border-radius": "10px"
})

nav_a_styles = Style(nav.tag + "  a", {
    "margin": "auto 0",
    "padding": "0 25px",
    "background-color": "#229954",
    "color": "white",
    "text-decoration": "none",
    "line-height": "1.65",
    "display": "block",
})

logo = Style(".logo", {
    "font-family": "\"Comfortaa\", sans-serif"
})

flex = Style(".flex", {
    "display": "flex"
})

button_styles = Style(".button", {
    "border": "none",
    "border-radius": "0.75rem",
    "padding": "0.75rem 1rem",
    "line-height": "1.5rem",
    "color": "white",
    "text-decoration": "none",
    "font-size": "1rem",
    "cursor": "pointer",
    "font-weight": "bold",
    "margin-right": "10px"
})

bg_green_hover = Style(".bg-green-hover:hover", {
    "background-color": "#55a175",
    "color": "white",
    "transition": "0.2s ease"
})

button_header = Style(".button-header", {
    "background-color": "white",
    "color": "#229954",
    "transition": "0.3s ease",
})

section_styles = Style("section", {
    "padding": "2rem",
    "width": "90%"
})

section_2_styles = Style(".section_2", {
    "background-color": "#F79E1B",
    "border-radius": "10px"
})

img_styles = Style(".img_styles", {
    "border-radius": "10px",
    "box-shadow": "0 4px 8px 0 rgba(0,0,0,0.2)",
})

body_styles.add_to_file("styles.css")
nav_styles.add_to_file("styles.css")
nav_a_styles.add_to_file("styles.css")
logo.add_to_file("styles.css")
flex.add_to_file("styles.css")
button_styles.add_to_file("styles.css")
bg_green_hover.add_to_file("styles.css")
button_header.add_to_file("styles.css")
section_styles.add_to_file("styles.css")
section_2_styles.add_to_file("styles.css")
img_styles.add_to_file("styles.css")
