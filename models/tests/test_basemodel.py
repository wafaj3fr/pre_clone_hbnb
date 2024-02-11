import unittest
from datetime import datetime
from models import BaseModel  # Replace 'my_module' with the actual module name where your BaseModel is defined

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_attributes_after_creation(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)
        self.assertEqual(self.base_model.created_at, self.base_model.updated_at)

    def test_save_updates_updated_at(self):
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        data = self.base_model.to_dict()
        self.assertIsInstance(data, dict)
        self.assertIn('id', data)
        self.assertIn('created_at', data)
        self.assertIn('updated_at', data)
        self.assertIn('__class__', data)
        self.assertEqual(data['__class__'], 'BaseModel')

    def test_init_with_arguments(self):
        data = {
            'id': '123',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-02T12:00:00.000000',
            'custom_field': 'value'
        }
        instance = BaseModel(**data)
        self.assertEqual(instance.id, '123')
        self.assertEqual(instance.created_at, datetime(2022, 1, 1, 12, 0, 0))
        self.assertEqual(instance.updated_at, datetime(2022, 1, 2, 12, 0, 0))
        self.assertEqual(instance.custom_field, 'value')

if __name__ == '__main__':
    unittest.main()
