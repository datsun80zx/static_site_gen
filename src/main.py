from textnode import TextNode, TextType

def main ():

    plain_text = TextNode("Hello World", TextType.TEXT)
    print("Plain text node:")
    print(plain_text)

    bold_text = TextNode("Important message", TextType.BOLD)
    print("\nBold text node:")
    print(bold_text)

    link_text = TextNode("Click me", TextType.LINK, "https://www.example.com")
    print("\nLink text node:")
    print(link_text)

    italic_text = TextNode("or don't", TextType.ITALIC,)
    print("\nItalic text node:")
    print(italic_text)

    code_text = TextNode("a bit of code", TextType.CODE,)
    print("\nCode text Node:")
    print(code_text)

    image = TextNode("this is an image", TextType.IMAGE,)
    print("\nImages:")
    print(image)

    duplicate_plain = TextNode("Hello World", TextType.TEXT)
    print("\nTesting equality...")
    print(f"Are the plain text nodes equal? {plain_text == duplicate_plain}")
    print(f"Are different nodes equal? {plain_text == bold_text}")


if __name__ == "__main__":
    main()