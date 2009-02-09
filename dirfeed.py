from dirobject import Directory
import os
import sys
import datetime
import PyRSS2Gen

def parse_directory (dir, depth):
	if depth == 0:
		return
	for entry in os.listdir(dir):
		type = ''
		fullpath = os.path.join (dir, entry)
		if os.path.isdir (fullpath):
			parse_directory (fullpath, depth-1)

		result = Directory.select (Directory.q.path == fullpath)
		if result.count() == 0:
			d = Directory(path=fullpath, date_added=datetime.datetime.now())

def build_feed ():
	dirs = Directory.select (orderBy="-date_added")[0:10]
	items = []
	for dir in dirs:
		items.append(PyRSS2Gen.RSSItem(
				title = dir.split('/')[-1],
				link = 'http://whatever/',
				description = 'This file is now available: %s' % dir.path,
				pubDate = dir.date_added
		));
	rss = PyRSS2Gen.RSS2(
			title = 'My awesome dir feed',
			link = 'http://whatever/',
			description = 'Files available',
			lastBuildDate = datetime.datetime.now(),
			items = items,
	)
	print rss.to_xml()


if __name__ == '__main__':
	if len (sys.argv) != 3:
		print 'Usage: %s <path> <depth>' % (sys.argv[0])
		sys.exit(1)
	
	path = sys.argv[1]
	depth = int(sys.argv[2])

	parse_directory (path, depth)
	build_feed ()
