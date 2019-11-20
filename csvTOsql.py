import mysql.connector
from mysql.connector import Error
from python_mysql_dbconfig import read_db_config
import csv
def connect():
    db_config = read_db_config()
    conn = None
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print('Connected to MySQL database')
            return conn
    except Error as e:
        print(e)
        return None
def insert_articles(articles):
    query =  "INSERT INTO articles(id,title,author,tag,link,content) " \
            "VALUES(%s,%s,%s,%s,%s,%s)"
    conn = connect()
    if conn!=None:
        try:
            cursor = conn.cursor()
            cursor.executemany(query, articles)
            conn.commit()
        except Error as e:
            print("Error : ",e)
        finally:
            cursor.close()
            conn.close()
def fetchall():
    print("hi......................")
    conn = connect()
    if conn!=None:
        cursor = conn.cursor()
        cursor.execute("SELECT content FROM articles")
        rowss = cursor.fetchall()
        rows = []
        for row in rowss:
            rows.append(row[0])
        return rows
        

if __name__ == '__main__':
    file_name = "../../data/articles.csv"
    with open(file_name, 'r') as csvfile:  
        csvreader = csv.reader(csvfile)  
        next(csvreader)
        articles=[]
        for row in csvreader:
            articles.append(("0",row[4],row[0],"tt",row[3],row[-1]))
        # insert_articles(articles)
    
    