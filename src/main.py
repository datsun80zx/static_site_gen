from textnode import TextNode, TextType
from htmlnode import LeafNode
from markdown_parser import markdown_to_blocks

def main ():

    raw_markdown = '# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item'

    markdown_to_blocks(raw_markdown)

if __name__ == "__main__":
    main()