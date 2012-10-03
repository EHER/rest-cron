import web
import json

render = web.template.render('templates/')

urls = (
        '/', 'index',
        '/cron', 'cron',
        '/cron/(\d+)$', 'cron_id'
        )

class index:
    def GET(self):
        return render.index()

class cron:
    def GET(self):
        return json.dumps(
                {"cron": [
                    {
                        "id": "1",
                        "minute": "1",
                        "hour": "*",
                        "day_of_month": "*",
                        "month": "*",
                        "day_of_week": "*",
                        "command": "ls -lah"
                    },
                    {
                        "id": "2",
                        "minute": "1",
                        "hour": "*",
                        "day_of_month": "*",
                        "month": "*",
                        "day_of_week": "*",
                        "command": "ls -lah"
                    }
                ]}
            )

class cron_id:
    def GET(self, id):
        return json.dumps({
            "id": id,
            "minute": "1",
            "hour": "*",
            "day_of_month": "*",
            "month": "*",
            "day_of_week": "*",
            "command": "ls -lah"
            })

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

