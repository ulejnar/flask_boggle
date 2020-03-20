from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def test_home_page(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<div id="game">', html)

    def test_session_board(self):
        with app.test_client() as client:
            resp = client.get('/')
            
            self.assertTrue(isinstance(session['board'], list))
            self.assertTrue(isinstance(session['board'][0], list))
            self.assertEqual(len(session['board']), 5)
            self.assertEqual(len(session['board'][0]), 5)




