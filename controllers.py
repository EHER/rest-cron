import json
import web


render = web.template.render('templates/')


class Homepage:
    def GET(self):
        return render.index()


class CronList:
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


class Cron:
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
