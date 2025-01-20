import unittest
from main import text_node_to_html_node
from leafnode import LeafNode
from textnode import TextNode, TextType

class TestTextToLeafnode(unittest.TestCase):
    def test_text_text_type(self):
        plain_text = TextNode("Hello World", TextType.TEXT)
        test = text_node_to_html_node(plain_text)

        self.assertIsInstance(test, LeafNode)
        self.assertEqual(
            test.to_html(),
            'Hello World',
            'this test shows that .TEXT is handled correctly'
        )

    def test_bold_text_type(self):
        bold_text = TextNode("Important message", TextType.BOLD)
        test1 = text_node_to_html_node(bold_text)

        self.assertIsInstance(test1, LeafNode)
        self.assertEqual(
            test1.to_html(),
            '<b>Important message</b>',
            'this should show that bold and other tags should work'
        )

    def test_link_text_type(self):
        link_text = TextNode("Click me", TextType.LINK, "https://www.example.com")
        test2 = text_node_to_html_node(link_text)

        self.assertIsInstance(test2, LeafNode)
        self.assertEqual(
            test2.to_html(),
            '<a href="https://www.example.com">Click me</a>',
            'this test should pass if links are handled correctly'
        )

    def test_img_text_type(self):
        image = TextNode("this is an image", TextType.IMAGE,'www.exampleurl.com')
        test3 = text_node_to_html_node(image)

        self.assertIsInstance(test3, LeafNode)
        self.assertEqual(
            test3.to_html(),
            '<img src="www.exampleurl.com" alt="this is an image">',
            'this should pass to show proper handling of images',
        )

    def test_invalid_text_type(self):
        self.assertRaises(Exception, text_node_to_html_node, None)
