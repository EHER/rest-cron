from paste.fixture import TestApp
from nose.tools import assert_equal
from main import app


class TestCode():
    def test_index(self):
        middleware = []
        testApp = TestApp(app.wsgifunc(*middleware))
        r = testApp.get('/')
        assert_equal(r.status, 200)
