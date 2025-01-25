from textnode import TextNode, TextType
from leafnode import LeafNode
from markdown_parser import split_nodes_images, extract_markdown_images

def main ():


    node = [
        TextNode(
                    "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
                    TextType.TEXT,
                )
    ]        

    new_nodes = split_nodes_images(node)
    print(new_nodes)


    # plain_text = TextNode("Hello World", TextType.TEXT)
    # print("Plain text node:")
    # print(plain_text)

    # bold_text = TextNode("Important message", TextType.BOLD)
    # print("\nBold text node:")
    # print(bold_text)

    # link_text = TextNode("Click me", TextType.LINK, "https://www.example.com")
    # print("\nLink text node:")
    # print(link_text)

    # italic_text = TextNode("or don't", TextType.ITALIC,)
    # print("\nItalic text node:")
    # print(italic_text)

    # code_text = TextNode("a bit of code", TextType.CODE,)
    # print("\nCode text Node:")
    # print(code_text)

    # image = TextNode("this is an image", TextType.IMAGE,'www.exampleurl.com')
    # print("\nImages:")
    # print(image)

    # duplicate_plain = TextNode("Hello World", TextType.TEXT)
    # print("\nTesting equality...")
    # print(f"Are the plain text nodes equal? {plain_text == duplicate_plain}")
    # print(f"Are different nodes equal? {plain_text == bold_text}")

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
            


if __name__ == "__main__":
    main()