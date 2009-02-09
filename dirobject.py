from sqlobject import *
import os

DATABASE_PATH = os.path.expanduser('~') + '/.dirfeed.db'

sqlhub.processConnection = connectionForURI('sqlite://%s' % DATABASE_PATH)

class Directory(SQLObject):
	path = StringCol()
	date_added = DateTimeCol ()

if __name__ == '__main__':
	Directory.createTable()
