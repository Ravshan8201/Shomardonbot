import sqlite3
conn = sqlite3.connect('user_list.sqlite')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS Users(
TG_ID INTEGER ,
F_Name STRING ,
Phone_Num INTEGER,
Lang INTEGER ,
Stage INTEGER
)
''')
first_insert = '''
INSERT INTO Users VALUES ('{}',' ',' ',' ','{}')
'''
get_id = '''
SELECT TG_ID 
FROM Users
Where TG_ID = '{}'
'''
upd_name = '''
UPDATE Users 
SET F_Name = '{}' 
WHERE TG_ID = '{}'
'''
select_name = '''
SELECT F_Name
From Users
WHERE TG_ID = '{}'
'''

update_phone_num = '''
UPDATE Users 
SET Phone_Num = '{}' 
WHERE TG_ID = '{}'
'''
select_num = '''
SELECT Phone_Num 
FROM Users
WHERE TG_ID = '{}'
'''
lang = '''
UPDATE Users
SET lang = '{}'
WHERE TG_ID = '{}'
'''
lang_select = '''
SELECT Lang
FROM Users
WHERE TG_ID = '{}'
'''

stagee  = '''
UPDATE Users
SET Stage = '{}'
WHERE TG_ID = '{}'
'''
stage = '''
SELECT Stage
FROM Users
WHERE TG_ID = '{}'
'''