from textnode import TextNode, TextType
from htmlnode import LeafNode
from markdown_parser import markdown_to_blocks, block_to_block_type

def main ():

    code = """```
        Here is some text that is supposed to be read as code
        ```"""

    test = block_to_block_type(code)

    print(test)
    

if __name__ == "__main__":
    main()