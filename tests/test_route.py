import unittest

from app import create_app


class TestRoute(unittest.TestCase):
    def setUp(self):
        self.app = create_app()

    def test_main(self):
        rv = self.app.get('/')
        assert rv.status == '200 OK'
        assert b'Index' in rv.data

    def test_404(self):
        rv = self.app.get('/other')
        self.assertEqual(rv.status, '404 NOT FOUND')

    # TODO: Faltaría el de registrar, login, recuperar.