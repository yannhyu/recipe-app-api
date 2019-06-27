from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db becomes available"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            # Check that it is only called once
            self.assertEqual(gi.call_count, 1)

    # Similar to with patch, pass in arg ts
    # This mock replaces the behavior of time.sleep
    # with a mock function that always returns True
    # That means during our tests it will not wait.
    # This avoid unneccesary waitings during each test
    # that slow down our tests execution.
    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # Set side effect
            # For the first five times it will raise the OperationalError
            # On the sixth time it will let is pass
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
