import unittest
import add_new_md as md


class add_new_mdTests(unittest.TestCase):
    
    md_data = "+ [Test prog](#test-prog)\n+ [Title](#title)<!---split here-->\n## Title\n\n```python\n..."
    prog_data = "# title SomeTitle\n# author smb\n# description some code description"
    title ='Test prog'
    description = 'some code description'
    source_code = "print('hello_world')"

    def test_prepare_md_file(self):
        self.assertEqual(md.prepare_md_file(self.md_data), ('+ [Test prog](#test-prog)\n+ [Title](#title)', '## Title\n\n```python\n...'))

    def test_prepare_md_titles(self):
        expected = ('SomeTitle', 'some code description')
        self.assertEqual(md.prepare_md_titles(self.prog_data), expected)

    def test_prepare_md_format_data (self):
        test = md.prepare_md_format_data(self.title, self.description, self.source_code)
        expected = ('+ [Test prog](#test-prog)\n', "## Test prog\nsome code description\n    \n```python\nprint('hello_world')\n```")
        self.assertEquals(test, expected)


if __name__ == "__main__":
    unittest.main()