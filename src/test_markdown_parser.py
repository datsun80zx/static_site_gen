import unittest

from textnode import TextNode, TextType
from markdown_parser import (
    extract_markdown_links,
    extract_markdown_images,
    split_nodes_delimiter,
    split_nodes_images,
    split_nodes_links,
    text_to_textnodes,
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

    def test_split_images(self):
        node1 = TextNode("This is an ![image](https://i.imgur.com/123.png) in text.", TextType.TEXT)
        node2 = TextNode("![first](img1.png) Some text ![second](img2.png)", TextType.TEXT)
        node3 = TextNode("![img1](url1)![img2](url2)![img3](url3)", TextType.TEXT)
        node4 = TextNode("![start](url1) middle text ![end](url2)", TextType.TEXT)
        node5 = TextNode("Start ![img1](url1) middle ![img2](url2) end", TextType.TEXT)
        node6 = TextNode("![preserved](url)", TextType.IMAGE, "url")

        test_cases = [
            node1,
            node2, 
            node4,
            node6,
        ]
        self.assertEqual(
            split_nodes_images(test_cases), 
            [
                TextNode('This is an ', TextType.TEXT),
                TextNode('image', TextType.IMAGE, 'https://i.imgur.com/123.png'),
                TextNode(' in text.', TextType.TEXT),
                TextNode('first', TextType.IMAGE, 'img1.png'),
                TextNode(' Some text ', TextType.TEXT),
                TextNode('second', TextType.IMAGE, 'img2.png'),
                TextNode('start', TextType.IMAGE, 'url1'),
                TextNode(' middle text ', TextType.TEXT),
                TextNode('end', TextType.IMAGE, 'url2'),
                TextNode("![preserved](url)", TextType.IMAGE, "url"),
            ]
        )

    def test_split_links(self):
        node2 = TextNode("This is a [link](https://boot.dev) in text.", TextType.TEXT)
        node4 = TextNode("[link1](url1.com) middle [link2](url2.com)", TextType.TEXT)
        node6 = TextNode("[link1](url1)[link2](url2)[link3](url3)", TextType.TEXT)

        test_cases = [
            node2,
            node4,
        
        ]

        self.assertEqual(
            split_nodes_links(test_cases), 
            [
                TextNode('This is a ', TextType.TEXT),
                TextNode('link', TextType.LINK, 'https://boot.dev'),
                TextNode(' in text.', TextType.TEXT),
                TextNode('link1', TextType.LINK, 'url1.com'),
                TextNode(' middle ', TextType.TEXT),
                TextNode('link2', TextType.LINK, 'url2.com'),
            ]
        )

    def test_text_to_textnodes(self):
        text = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )
        