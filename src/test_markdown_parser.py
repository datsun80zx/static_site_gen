import unittest

from textnode import TextNode, TextType
from markdown_parser import (
    extract_markdown_links,
    extract_markdown_images,
    split_nodes_delimiter,
)

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
    
    def test_image_extraction(self):
        text1 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"    
        text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        text3 = "![cat](cat.jpg) Here's a [link](https://example.com)"
        text4 = "No markdown here"
        text5 = "![](empty.jpg) [](empty.com)"

        self.assertEqual(
            [
                extract_markdown_images(text1),
                extract_markdown_images(text2),
                extract_markdown_images(text3),
                extract_markdown_images(text4),
                extract_markdown_images(text5),
            ],
            [
                [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')],
                [],
                [('cat', 'cat.jpg')],
                [],
                [],
            ],
            'this should show that images are properly handled'
        )

    def test_link_extraction(self):
        text1 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"    
        text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        text3 = "![cat](cat.jpg) Here's a [link](https://example.com)"
        text4 = "No markdown here"
        text5 = "![](empty.jpg) [](empty.com)"

        self.assertEqual(
            [
                extract_markdown_links(text1),
                extract_markdown_links(text2),
                extract_markdown_links(text3),
                extract_markdown_links(text4),
                extract_markdown_links(text5),
            ],
            [
                [],
                [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')],
                [('link', 'https://example.com')],
                [],
                [('', 'empty.com')],
            ],
            'this should show that images are properly handled'
        )
