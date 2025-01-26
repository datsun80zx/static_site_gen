import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):
    def test_propstohtml(self):
        node = HTMLNode(
            "<p>",
            "some value",
            None,
            {
                "href": "https://www.google.com", 
                "target": "_blank"
            }
        )

        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"',
            'this should return the string: href="https://www.google.com" target="_blank"'
            )

    def test_nodes_with_various_params_are_nodes(self):
        node = HTMLNode(
            "<p>",
            "some value",
            None,
            {
                "href": "https://www.google.com", 
                "target": "_blank"
            }
        )
        
        node1 = HTMLNode(
            "<h1>"
        )
        
        node2 = HTMLNode(
            "<a>",
            "text in side",
            None,
            {"target": "_notblank"}
        )
        
        self.assertIsInstance(node, HTMLNode, f'node without children should still be a HTMLNode: {node}')
        self.assertIsInstance(node1, HTMLNode, f'\nnode with only a tag should still be a HTMLNode: {node1}')
        self.assertIsInstance(node2, HTMLNode, f'\nnode with only one prop should still be a HTMLNode: {node2}')

    def test_props_is_none(self):
        node1 = HTMLNode(
            "<h1>"
        )
        
        self.assertEqual(
            node1.props_to_html(),
            "",
            'when node has no prop it should return an empty string'
        )

class TestLeafNode(unittest.TestCase):
    def test_reg_tag(self):
        test1 = LeafNode(
            'p',
            'Here is a regular paragraph',
            None,
        )

        self.assertEqual(
            test1.to_html(),
            '<p>Here is a regular paragraph</p>',
            'this test shows that to_html method is creating normal tags correctly'
        )

    def test_link_case_1_property(self):
        test2 = LeafNode(
            'a',
            'click here',
            {
                'href': 'https://www.google.com'
            },
        )

        self.assertEqual(
            test2.to_html(),
            '<a href="https://www.google.com">click here</a>',
            'this test should pass if links are handled correctly'
        )

    def test_multi_props(self):
         test3 = LeafNode(
            'a',
            'click here',
            {
                'href': 'https://www.google.com',
                'target': '_blank'
            },
        )
         self.assertEqual(
            test3.to_html(),
            '<a href="https://www.google.com" target="_blank">click here</a>',
            'this test should pass if multiple link properties are handled correctly'
        )

    def test_no_value(self):
        test4 = LeafNode(
            'p',
            None,
            None,
        )

        self.assertRaises(ValueError, test4.to_html)

    def test_no_tag(self):
        test5 = LeafNode(
            None,
            'some texty text',
            None,
        )
        self.assertEqual(
            test5.to_html(),
            test5.value,
            'this should show that if no tag is provided then it returns raw text'
        )

class TestParentNode(unittest.TestCase):
    def test_single_leafnode(self):
        single_leaf = ParentNode(
            'p',
            [
                LeafNode(
                'b',
                'Bold text',
                None,
                )
            ],
        )

        self.assertEqual(
            single_leaf.to_html(), 
            '<p><b>Bold text</b></p>',
            'this should pass if single children is handled correctly',
        )

    def test_multiple_leafnodes(self):
        multi_leaf = ParentNode(
            'p',
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"), 
            ],
        )

        self.assertEqual(
            multi_leaf.to_html(),
            '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>',
            'this should pass if multiple leaf node children are handled correctly',
        )
    def test_multi_parentnode_children(self):
        multi_parents = ParentNode(
            'div',
            [
                ParentNode(
                    'p',
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                    None,
                ),

                ParentNode(
                    'p',
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                    None,
                ),

                ParentNode(
                    'p',
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                    None,
                ),

            ],
            None,
        )

        self.assertEqual(
            multi_parents.to_html(),
            '<div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div>',
            'should pass if it properly handles when children are also parentnodes',
        )
    def test_no_children(self):
        no_child = ParentNode(
            'p',
            None,
        )

        self.assertRaises(ValueError, no_child.to_html)

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

