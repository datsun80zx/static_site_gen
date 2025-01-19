from __future__ import annotations


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