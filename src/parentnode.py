from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError()
        
        if self.children is None:
            raise ValueError("Children is missing")
        
        result = ""
        
        for children in self.children:
            result += children.to_html()

        return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"
        
