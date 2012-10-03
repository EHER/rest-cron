import web
from controllers import Homepage, CronList, Cron


render = web.template.render('templates/')

urls = (
        '/', Homepage,
        '/cron', CronList,
        '/cron/(\d+)$', Cron,
        )


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
