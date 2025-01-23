import unittest

from textnode import TextNode, TextType
from markdown_parser import split_nodes_delimiter

class TestMarkdownParser(unittest.TestCase):
    def test_multiple_type(self):

        node = [
            TextNode('hello **world** and **python**', TextType.TEXT),
            TextNode('before `code` after `code`', TextType.TEXT), 
            TextNode('boots is a *pain* in the *ass*', TextType.TEXT), 
        ]

        self.assertEqual(
            split_nodes_delimiter(node, '**', TextType.BOLD),
            [
                TextNode('hello ', TextType.TEXT),
                TextNode('world', TextType.BOLD),
                TextNode(' and ', TextType.TEXT),
                TextNode('python', TextType.BOLD),
                TextNode('before `code` after `code`', TextType.TEXT), 
                TextNode('boots is a *pain* in the *ass*', TextType.TEXT),
            ],
            'This should pass if it appropriately handles multiple bold cases'
            )
        