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
        r.mustcontain('A REST way to manage your Cron')
        r.mustcontain('curl -XGET http://localhost:8080/cron')
        r.mustcontain('curl -XGET http://localhost:8080/cron/1')
        r.mustcontain('curl -XDELETE http://localhost:8080/cron/2')

    def test_cron_list_route(self):
        r = self.testApp.get('/cron')
        assert_equal(r.status, 200)
        r.mustcontain('"id": 1')
        r.mustcontain('"minute": "0"')
        r.mustcontain('"hour": "3"')
        r.mustcontain('"day_of_month": "*"')
        r.mustcontain('"day_of_week": "*"')
        r.mustcontain('"month": "*"')
        r.mustcontain('curl -I http://eher.com.br/')
        r.mustcontain('"id": 2')
        r.mustcontain('"minute": "1"')
        r.mustcontain('"hour": "*"')
        r.mustcontain('"day_of_month": "*"')
        r.mustcontain('"day_of_week": "*"')
        r.mustcontain('"month": "*"')
        r.mustcontain('curl -I http://chegamos.com/')

    def test_cron_route(self):
        r = self.testApp.get('/cron/1')
        assert_equal(r.status, 200)
        r.mustcontain('"id": 1')
        r.mustcontain('"minute": "0"')
        r.mustcontain('"hour": "3"')
        r.mustcontain('"day_of_month": "*"')
        r.mustcontain('"day_of_week": "*"')
        r.mustcontain('"month": "*"')
        r.mustcontain('curl -I http://eher.com.br/')
