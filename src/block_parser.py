from htmlnode import (
    ParentNode,
    text_node_to_html_node,
)
from markdown_parser import (
    block_to_block_type,
    markdown_to_blocks,
    text_to_textnodes,
)

def markdown_to_html_node(markdown):
    # Create a copy of the data to manipulate. 
    document = markdown

    # split the document into blocks. 
    document_blocks = markdown_to_blocks(document)


    # iterate through the list of blocks to find the type and then store as tag/text tuple. 
    # I want to refactor this portion to where i have the tag stored and then I call a function to process the text. 
    tag_text_tuple_list = []
    for block in document_blocks:
        # create the variable to hold the tag value &
        #identify the block_type of the current block:
        tag = block_to_block_type(block)
        # create a tuple with tag and text: 
        tag_text_tuple = (tag, block)
        tag_text_tuple_list.append(tag_text_tuple)


    # strip markdown block formatting from text. 
    tag_stripped_text_tuple_list = []
    for tuple in tag_text_tuple_list:
        if tuple[0] == "ul" or tuple[0] == "ol" or tuple[0] == "blockquote":
            tag_stripped_text_tuple_list.append(tuple)
        elif tuple[0] != "p":
            format_stripped_block = markdown_format_stripper(tuple[1])
            tmp_tuple = (tuple[0], format_stripped_block)
            tag_stripped_text_tuple_list.append(tmp_tuple)
        else:
            tag_stripped_text_tuple_list.append(tuple)


    # At this point I have a list of text and the appropriate tags they should have. Now I need to convert the text into a text node.
    # So I need to do two steps. First I need to create a list of textnodes, Then I need to process that list into a list of HTML LeafNodes. 
    # once i have the html node list aka the children I need to combine them with the overall tag into a parent node. 

    # tag_and_textnode_list = []
    parents = []
    for tuple in tag_stripped_text_tuple_list: 
        if tuple[0] == "ol":
            parent = olist_parser(tuple[1])
            parents.append(parent)
        elif tuple[0] == "ul":
            parent = ulist_parser(tuple[1])
            parents.append(parent)
        elif tuple[0] == "p":
            parent = paragraph_to_html_node(tuple[1])
            parents.append(parent)
        elif tuple[0] == "blockquote":
            parent = quote_to_html_node(tuple[1])
            parents.append(parent)
        else:
            text = tuple[1]
            parents.append(ParentNode(tuple[0], text_to_html_children(text)))
    
    final_parent_node = ParentNode("div", parents)

    html = final_parent_node.to_html()

    return html
    
def markdown_format_stripper(block): # this function really only handles headers and code blocks however I didn't want to change the name everywhere it was used. 
    headings = {
        '# ': 'h1',
        '## ': 'h2',
        '### ': 'h3',
        '#### ': 'h4',
        '##### ': 'h5',
        '###### ': 'h6',
    }
    for heading in headings:
        if block.startswith(heading):
            return block.strip(heading)
        
    if block.startswith('```') and block.endswith('```'):
        return block.strip('```')

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.strip("# ").strip()
    raise Exception("No Header")

def olist_parser(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_html_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def ulist_parser(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_html_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_html_children(paragraph)
    return ParentNode("p", children)

def text_to_html_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_html_children(content)
    return ParentNode("blockquote", children)
