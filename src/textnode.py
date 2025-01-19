from enum import Enum, auto

class TextType(Enum):
    TEXT = auto()
    BOLD = auto()
    ITALIC = auto()
    CODE = auto()
    LINK = auto()
    IMAGE = auto()



class TextNode:
    def __init__ (self, TEXT: str, TEXT_TYPE: TextType, URL: str=None):
        self.text = TEXT 
        self.text_type = TEXT_TYPE
        self.url = URL

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        
        # text_equal = self.text == other.text
        # type_equal = self.text_type == other.text_type
        # url_equal = self.url == other.url
        
        # print(f"Text comparison: {text_equal} ({self.text} == {other.text})")
        # print(f"Type comparison: {type_equal} ({self.text_type} == {other.text_type})")
        # print(f"URL comparison: {url_equal} ({self.url} == {other.url})")
        
        # return text_equal and type_equal and url_equal            
        return(
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )
    
    def __repr__ (self):
        url_str = str(self.url) if self.url is not None else "None"
        return f'TextNode("{self.text}", {self.text_type.name}, {url_str})'
