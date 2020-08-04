import unittest
import app
from unittest.mock import patch


class Apptest(unittest.TestCase):



    def setUp(self):
        self.directories, self.documents = app.update_date()
        app.documents == self.documents
        app.directories == self.directories

    def test_update_data(self):
        data_in_update_data = app.update_date()
        self.assertIsInstance(data_in_update_data, tuple)
        self.assertIsInstance(data_in_update_data[0], dict)
        self.assertIsInstance(data_in_update_data[1], list)
        for result in data_in_update_data[1]:
            self.assertIsInstance(result, dict)

    def test_check_document_existance(self):
        check_false = app.check_document_existance('000000000000000')
        check_true = app.check_document_existance(app.documents[0].get('number'))
        self.assertTrue(check_true)
        self.assertFalse(check_false)

    def test_add_new_doc(self):
        self.assertNotIn('515', app.directories.get('123', []))
        with patch('app.input', side_effect=['515', 'passport', 'bob', '123']):
            app.add_new_doc()
        self.assertIn('515', app.directories.get('123', []))

    def test_move_doc_to_shelf(self):
        with patch('app.input', side_effect=['10006', '3']):
            app.move_doc_to_shelf()
        self.assertIn('515', app.directories.get('123', []))

    def test_get_doc_shelf(self):
        with patch('app.input', return_value=app.documents[len(app.documents) - 1].get('number')):
            shelf_num = app.get_doc_shelf()
        self.assertIsInstance(shelf_num, str)

    def test_append_doc_to_shelf(self):
        shelf_num = '999999'
        app.append_doc_to_shelf(app.documents[len(app.documents) - 1].get('number'), shelf_num)
        self.assertEqual(app.documents[len(app.documents) - 1].get('number'), app.directories.get(shelf_num)[0])

    # def test_delete(self):
    #     for iter in range(len(app.documents)):
    #         with patch('app.input', return_value=app.documents[0].get('number')):
    #             app.delete_doc()
    #     docs_on_directories = 0
    #     for directory in app.directories.values():
    #         docs_on_directories += len(directory)
    #     self.assertEqual(docs_on_directories, 1)
    #     self.assertEqual(len(app.documents), 1)

