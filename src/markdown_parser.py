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


    
    
    
    
    
    
    
    # new_nodes = []
    # delimiters = {
    #     '**': TextType.BOLD,
    #     '*': TextType.ITALIC,
    #     '`': TextType.CODE,
    # }
    # if text_type == TextType.TEXT:
    #     for delimiter in delimiters:
    #         if delimiter in old_nodes:
    #             text_list = old_nodes.text.split(delimiter)
    #         if len(text_list) == 3:
    #             new_nodes.extend(
    #                 [
    #                     TextNode(text_list[0], TextType.TEXT),
    #                     TextNode(text_list[1], delimiters[delimiter]),
    #                     TextNode(text_list[2], TextType.TEXT),
    #                 ]
    #             )
