PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE cron (id integer serial primary key, minute text, hour text, day_of_month text, month text, day_of_week text, command text);
INSERT INTO "cron" VALUES(1,'0','3','*','*','*','curl -I http://eher.com.br/');
INSERT INTO "cron" VALUES(2,'1','*','*','*','*','curl -I http://chegamos.com/');
COMMIT;
