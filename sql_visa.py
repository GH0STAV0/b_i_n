import mysql.connector

import time ,os
from datetime import datetime






# MySQL Username  epiz_30595619
# MySQL Password
# Gu82q1fZDC7h5
# MySQL Hostname  sql105.epizy.com
# MySQL Port (optional)   3306
# Database Name   epiz_30595619_XXX


# Base de données: test_db4freex01
# Nom d'utilisateur: test_db4freex01
# Email: mysql_visa1@r0b-in.nl.eu.org

# bot_name='bot_tow'3306
# bot_name='bot_one'
bot_name='bot_tow'
# 
# 
# 
# mydb = mysql.connector.connect(host="sql4.freesqldatabase.com",user="sql4471825",passwd="v5PgElNLfu",database="sql4471825")
# mydb = mysql.connector.connect(host="sql11.freemysqlhosting.net",user="sql11471517",passwd="CKwuJiGtsA",database="sql11471517")
# 
mydb = mysql.connector.connect(host="db4free.net",user="test_db4freex01",passwd="SkPsU4PrbQEH!DJ",database="test_db4freex01")

# last_bin="40001799"

today_date = datetime.today().strftime('%d-%m-%Y')
###############################

host_sql="db4free.net"
user="test_db4freex01"
passwd="SkPsU4PrbQEH!DJ"
database="test_db4freex01"
############################

def drop_sql_table():
	print(" drop_sql_table  OF  : ",end='',flush=True)
	mydb = mysql.connector.connect(host=host_sql,user="test_db4freex01",passwd="SkPsU4PrbQEH!DJ",database="test_db4freex01")
	mycursor = mydb.cursor()
	sql = "DROP TABLE IF EXISTS nord_list2"
	mycursor.execute(sql)
	print("[ SUCCED ] ")


def restored_fresh_sql_table():
	drop_sql_table()
	print(" restored_fresh_sql_table  OF nord_list2 last_bin_sql.sql : ",end='',flush=True)
	os.system("mysql -h db4free.net -u test_db4freex01 -pSkPsU4PrbQEH!DJ test_db4freex01 < last_bin_sql.sql")
	print("[ SUCCED ] ")





def check_if_exist():

	print(" CHECK THE FILE  LAST_BIN IF EXIST  : ",end='',flush=True)
	PATH = './last_bin'
	if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
	    print("FILE EXIST : )")
	else:
	    print("MISSING FILE !!!")
	    open("last_bin", 'w').close()
	    creat_last_bin()






def insert_to_db():

	
	mycursor = mydb.cursor()

	sql = "INSERT INTO last_bin_sql (bot_name, last_bin,last_ssen) VALUES (%s, %s, %s)"
	val = ("bot_tow", "50000000","12-11-2021")
	mycursor.execute(sql, val)
	time.sleep(2)

	mydb.commit()


def check_connect_mysql():
	print(" CHECK SQL  CONNECTION       : ",end='',flush=True)
	try:
		
		mycursor = mydb.cursor()
		print("MYSQL CONNECTED OK ")
	except  Exception as e :
		print(" SQL ERROR CONNECTION        : "+str(e)+" ",end='',flush=True)


def update_to_db(bin0):
	check_connect_mysql()
	print(" UPDATE_SQL BIN [ "+bin0+" ] : ",end='',flush=True)

	
	mycursor = mydb.cursor()
	
	input=(bin0,today_date,bot_name)
	sql = "UPDATE last_bin_sql SET last_bin = %s , last_ssen= %s  WHERE bot_name = %s"
	mycursor.execute(sql,input)
	mydb.commit()
	print("[ SUCCED ] ")

def creat_last_bin():
	# print(" CREAT THE FILE LAST_BIN  : ",end='',flush=True)
	bina=get_value_last_bin()
	print("[ "+bina+" ]")
	with open('last_bin', "w") as myfile:
		myfile.write(bina)







def get_value_last_bin():

	print(" SEARCH_SQL LAST BIN OF [ "+bot_name+" ] : ",end='',flush=True)
	mycursor = mydb.cursor()
	sql = "SELECT * FROM last_bin_sql WHERE bot_name = %s"
	mycursor.execute(sql,(bot_name,))
	record = mycursor.fetchall()
	for row in record:
		sql_last_bin=row[2]
		print(row[2])
	return sql_last_bin










# update_to_db("543896")
# insert_to_db()



# password wifi 36038860

# host remotemysql.com:3306

# user f6V3kVwxvH

# database f6V3kVwxvH

# pass sOVnW1130i
check_connect_mysql()
# restored_fresh_sql_table()

get_value_last_bin()

# get_value_last_bin(bot_name)
# check_if_exist()
# creat_last_bin()