import web
from controllers import Homepage, CronList, Cron


urls = (
        '/', Homepage,
        '/cron', CronList,
        '/cron/(\d+)$', Cron,
        )

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
