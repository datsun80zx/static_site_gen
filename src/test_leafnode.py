import unittest

from leafnode import LeafNode


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
