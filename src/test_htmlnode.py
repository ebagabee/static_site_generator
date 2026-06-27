import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        html_node = HTMLNode("p", "testing p", None, None)
        
        self.assertRaises(NotImplementedError, html_node.to_html)

    def test_props_to_html_with_props_none(self):
        node = HTMLNode("p", "testing p", None, None)

        self.assertEqual("", node.props_to_html())

    def test_props_to_html_with_props(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        
        node = HTMLNode("a", "Teste de link", None, props=props)

        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())

if __name__ == "__main__":
    unittest.main()