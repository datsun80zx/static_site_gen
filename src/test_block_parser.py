import unittest

from block_parser import markdown_to_html_node

class TestBlockParser(unittest.TestCase):
    def test_block_parser(self):
        document = """
# Unit Test For Block Parser 

I have to write a unit test that will go over how a block parser *handles* different text in **markdown** format. 

## Next section 

```
this is to indicate some code blocks that might be present in the markdown document. 
``` 

![image](img.png) 

>above is supposed to be a block that is indicating an image. ~ a quote 
"""

        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        html = """<div><h1>Unit Test For Block Parser</h1><p>I have to write a unit test that will go over how a block parser <i>handles</i> different text in <b>markdown</b> format.</p><h2>Next section</h2><code>
this is to indicate some code blocks that might be present in the markdown document. 
</code><p><img src="img.png" alt="image"></p><blockquote>above is supposed to be a block that is indicating an image. ~ a quote</blockquote></div>"""

        self.assertEqual(markdown_to_html_node(document), html, "this should show things work")

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        html = markdown_to_html_node(md)

        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        html = markdown_to_html_node(md)

        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        html = markdown_to_html_node(md)

        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        html = markdown_to_html_node(md)

        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        html = markdown_to_html_node(md)
        
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )
