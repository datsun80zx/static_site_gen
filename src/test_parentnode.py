import unittest

from parentnode import ParentNode
from leafnode import LeafNode

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