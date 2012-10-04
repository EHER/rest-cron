from paste.fixture import TestApp
from nose.tools import assert_equal
from main import app


class Test():
    def setUp(self):
        middleware = []
        self.testApp = TestApp(app.wsgifunc(*middleware))

    def test_homepage_route(self):
        r = self.testApp.get('/')
        assert_equal(r.status, 200)

    def test_cron_list_route(self):
        r = self.testApp.get('/cron')
        assert_equal(r.status, 200)

    def test_cron_route(self):
        r = self.testApp.get('/cron/1')
        assert_equal(r.status, 200)
