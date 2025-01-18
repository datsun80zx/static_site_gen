import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_notequal(self):
        node3 = TextNode("This is a text", TextType.CODE)
        node4 = TextNode("this is a test", TextType.ITALIC)
        self.assertNotEqual(node3, node4)

    def test_urlfield(self):
        node5 = TextNode("some website", TextType.LINK)
        node6 = TextNode("another website", TextType.LINK, "https://www.google.com") 
        self.assertIsNone(node5.url, "URL should be None when not provided")
        self.assertEqual(node6.url,"https://www.google.com", "URL should match the provided value")

        self.assertIsInstance(node5, TextNode, "Node without URL should be a TextNode")
        self.assertIsInstance(node6, TextNode, "Node with URL should be a TextNode")


if __name__ == "__main__":
    unittest.main()