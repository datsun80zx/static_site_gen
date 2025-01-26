from __future__ import annotations
from typing import Union
from textnode import TextNode, TextType

class HTMLNode:
    def __init__(self, tag: str=None, value: str=None, children: list[HTMLNode]=None, props: dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props:
            result = ""
            for key, value in self.props.items():
                result = result + f' {key}="{value}"'
            return result
        else:
            return ""
        
    
    def __repr__(self):
        tag_str = str(self.tag) if self.tag is not None else "None"
        value_str = str(self.value) if self.value is not None else "None"
        children_str = str(self.children) if self.children is not None else "None"
        props_str = str(self.props.items) if self.props is not None else "None"
        return f"HTMLNode({tag_str}, {value_str}, {children_str}, {props_str})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value == None: 
            raise ValueError
        elif self.tag == None:
            return self.value
        elif self.tag == 'img':
            return f'<{self.tag}{self.props_to_html()}>'
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

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

def text_node_to_html_node(text_node):
    if isinstance(text_node, TextNode):
        if text_node.text_type == TextType.TEXT:
            return LeafNode(
                None,
                f'{text_node.text}',
                None,
            )
        elif text_node.text_type == TextType.BOLD:
            return LeafNode(
                'b',
                f'{text_node.text}',
                None,
            )
        elif text_node.text_type == TextType.ITALIC:
            return LeafNode(
                'i',
                f'{text_node.text}',
                None,
            )
        elif text_node.text_type == TextType.CODE:
            return LeafNode(
                'code',
                f'{text_node.text}',
                None,
            )
        elif text_node.text_type == TextType.LINK:
            return LeafNode(
                'a',
                f'{text_node.text}',
                {
                    'href': text_node.url,
                },
            )
        elif text_node.text_type == TextType.IMAGE:
            return LeafNode(
                'img',
                '',
                {
                    'src': text_node.url,
                    'alt': text_node.text,
                },
            )
    else:
        raise Exception('Invalid TextType')
