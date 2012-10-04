import json
import web


render = web.template.render('templates/')
web.config.debug = False
db = web.database(dbn='sqlite', db='database/rest-cron.db')


class Homepage:
    def GET(self):
        return render.index()


class CronList:
    def GET(self):
        web.header('Content-Type', 'application/json')
        cron_list = db.select('cron')
        return json.dumps(list(cron_list))


class Cron:
    def GET(self, id):
        web.header('Content-Type', 'application/json')
        cron = db.select('cron', vars=locals(), where="id=$id")
        return json.dumps(list(cron))

    def DELETE(self, id):
        web.header('Content-Type', 'application/json')
        db.delete('cron', vars=locals(), where="id=$id")
        return json.dumps({"message": "OK"})
