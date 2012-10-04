import json
import web


render = web.template.render('templates/')
db = web.database(dbn='sqlite', db='database/rest-cron.db')


class Homepage:
    def GET(self):
        return render.index()


class CronList:
    def GET(self):
        cron_list = db.select('cron')
        return json.dumps(list(cron_list))


class Cron:
    def GET(self, id):
        cron = db.select('cron', dict(cron_id=id), where="id=$cron_id")
        return json.dumps(list(cron))
