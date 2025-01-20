from __future__ import annotations
from htmlnode import HTMLNode
from leafnode import LeafNode
from typing import Union


class ParentNode(HTMLNode):
    def __init__(self, tag, children: list[Union[LeafNode, ParentNode]], props = None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError('Invalid HTML: no tag')
        if not self.children:
            raise ValueError('Invalid HTML: no children')

        result = ''
        
        for child in self.children:

            if isinstance(child, LeafNode):
                result = result + child.to_html()

            elif isinstance(child, ParentNode):
                result = result + child.to_html()

        return f'<{self.tag}{self.props_to_html()}>{result}</{self.tag}>'

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
        