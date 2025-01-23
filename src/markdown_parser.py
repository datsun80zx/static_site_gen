import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

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
