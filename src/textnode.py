from enum import Enum, auto

class TextType(Enum):
    TEXT = auto()
    BOLD = auto()
    ITALIC = auto()
    CODE = auto()
    LINK = auto()
    IMAGE = auto()
    QUOTE = auto()



class TextNode:
    def __init__ (self, TEXT: str, TEXT_TYPE: TextType, URL: str=None):
        self.text = TEXT 
        self.text_type = TEXT_TYPE
        self.url = URL

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
           
        return(
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )
    
    def __repr__ (self):
        url_str = str(self.url) if self.url is not None else "None"
        return f'TextNode("{self.text}", {self.text_type.name}, {url_str})'
