from pymysql import install_as_MySQLdb
import pymysql

pymysql.version_info = (1, 4, 13, 'final', 0)
install_as_MySQLdb()
