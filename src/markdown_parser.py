import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    if not isinstance(old_nodes, list):
        old_nodes = [old_nodes]

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        delimiter_count = node.text.count(delimiter)

        if delimiter_count == 0:
            new_nodes.append(node)
            continue

        if delimiter_count % 2 != 0:
            raise Exception('Cannot Process: Invalid markdown syntax')

        parts = node.text.split(delimiter)
        for i in range(len(parts)):
            if parts[i] == '':
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(parts[i], text_type))

    return new_nodes

def split_nodes_images(old_nodes):
    new_nodes = []
    
    if not isinstance(old_nodes, list):
        old_nodes = [old_nodes]
    
    for node in old_nodes:
        # if the TextType is something besides text just add the node to the new list. 
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        #create a list of tuples where the first and 
        # second index of the tuple are the alt text and url for the image.
        images = extract_markdown_images(node.text) 
        
        # confirm valid images in the node
        if not images: 
            new_nodes.append(node)
            continue

        # keep track of where we are in the current nodes text. 
        current_text = node.text

        # iterate over the list of tuples and split the text node for each one
        for image in images: 
            image_alt = image[0]
            image_url = image[1]

            # this is a list where the first item is text before the current image
            # the second item is the remaining text which could also contain another image. 
            section = current_text.split(f'![{image_alt}]({image_url})', 1)
            
            # if the first list item is an empty string then the image was the starting point 
            # therefore should be added as a node and then the second item is the remaining text. 
            if section[0] == '':
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
                current_text = section[1]
                continue
            else:
                new_nodes.extend(
                    [
                        TextNode(section[0], TextType.TEXT), 
                        TextNode(image_alt,TextType.IMAGE, image_url),
                    ]
                )
                current_text = section[1]
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    
    if not isinstance(old_nodes, list):
        old_nodes = [old_nodes]

    for node in old_nodes:
        # if the TextType is something besides text just add the node to the new list. 
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        #create a list of tuples where the first and 
        # second index of the tuple are the alt text and url for the image.
        links = extract_markdown_links(node.text) 
        
        # confirm valid images in the node
        if not links: 
            new_nodes.append(node)
            continue

        # keep track of where we are in the current nodes text. 
        current_text = node.text

        # iterate over the list of tuples and split the text node for each one
        for link in links: 
            anchor_text = link[0]
            url = link[1]

            # this is a list where the first item is text before the current image
            # the second item is the remaining text which could also contain another image. 
            section = current_text.split(f'[{anchor_text}]({url})', 1)
            
            # if the first list item is an empty string then the image was the starting point 
            # therefore should be added as a node and then the second item is the remaining text. 
            if section[0] == '':
                new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
                current_text = section[1]
                continue
            else:
                new_nodes.extend(
                    [
                        TextNode(section[0], TextType.TEXT), 
                        TextNode(anchor_text,TextType.LINK, url),
                    ]
                )
                current_text = section[1]
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes

def extract_markdown_images(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    good_images = []
    bad_images = []
    for tuple in images:
        if tuple[0] != '' and tuple[1] != '':
            good_images.append(tuple)
        elif tuple[0] == '' or tuple[1] == '':
            bad_images.append(tuple)
    
    return good_images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    good_links = []
    for tuple in links:
        if tuple[1] != '':
            good_links.append(tuple)
    return good_links

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)

    nodes = split_nodes_delimiter(node, '**', TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, '*', TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)
    nodes = split_nodes_images(nodes)
    nodes = split_nodes_links(nodes)

    return nodes

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    final = []
    for block in blocks:
        tmp = block.strip()
        if tmp != '':
            final.append(tmp)
            continue
    return final

def block_to_block_type(block):
    block_types = {
        '# ': 'Heading 1',
        '## ': 'Heading 2',
        '### ': 'Heading 3',
        '#### ': 'Heading 4',
        '##### ': 'Heading 5',
        '###### ': 'Heading 6',
        '>': 'quote',
        '* ': 'unordered list',
        '- ': 'unordered list',
    }
    for type in block_types:
        if block.startswith(type):
            return block_types[type]
        
    if block.startswith('```') and block.endswith('```'):
        return 'code'
    elif block.startswith('1. '):
        return 'ordered list'
    else:
        return 'paragraph'   

