#REST Cron
A REST way to manage your Cron.

##Dependencies
[git](http://git-scm.com/)
[python](http://www.python.org/)
[virtualenv](http://pypi.python.org/pypi/virtualenv)
[pip](http://www.pip-installer.org/en/latest/index.html)
[sqlite](http://www.sqlite.org/)
[make](http://www.gnu.org/software/make/)

##Setup
```
git clone git://github.com/EHER/rest-cron.git
virtualenv rest-cron
cd rest-cron
source bin/activate
pip install -r deps.txt
```

##Database
```
sqlite3 database/rest-cron.db < database/rest-cron.sql
```

##Running
```
python main.py
```
