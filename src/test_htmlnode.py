import unittest

from htmlnode import HTMLNode


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