import logging
import argparse
import sys
import psycopg2


# Set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)


# Connect to DB from Python
logging.debug("Connecting to PostgreSQL")
connection = psycopg2.connect("dbname='snippets' user='action' host='localhost'")
logging.debug("Database connection established.")



# Main function
def main():
	"""Main function"""
	logging.info("Constructing parser")
	parser = argparse.ArgumentParser(description="Store, retrieve,... snippets of text")

	# Add subparsers
	subparsers = parser.add_subparsers(dest="command", help="Available commands")

	# Subparser for the put command
	logging.debug("Constructing put subparser")
	put_parser = subparsers.add_parser("put",help="Stores a snippet")
	put_parser.add_argument("name",help="The name of the snippet")
	put_parser.add_argument("snippet",help="The snippet text")
	put_parser.add_argument("--hide", help="Hides row")

	# Subparser for the get command
	logging.debug("Constructing get subparser")
	get_parser = subparsers.add_parser("get",help="Retrieves a snippet")
	get_parser.add_argument("name",help="The name of the snippet")

	# Subparser for the delete command
	logging.debug("Constructing delete subparser")
	delete_parser = subparsers.add_parser("delete",help="Deletes a snippet")
	delete_parser.add_argument("name",help="The name of the snippet")

	# Subparser for the update command
	logging.debug("Constructing update subparser")
	update_parser = subparsers.add_parser("update",help="Updates a snippet")
	update_parser.add_argument("name",help="The name of the snippet")
	update_parser.add_argument("newname",help="The new name of the snippet")
	update_parser.add_argument("newsnippet",help="The new snippet")

	# Subparser for the catalog command
	logging.debug("Constructing catalog subparser")
	catalog_parser = subparsers.add_parser("catalog",help="Retrieves list of DB entries")

	# Subparser for the search command
	logging.debug("Constructing search subparser")
	search_parser = subparsers.add_parser("search", help="Retrieves seach results")
	search_parser.add_argument("query",help="This is the query string")


	arguments = parser.parse_args(sys.argv[1:])
	arguments = vars(arguments)
#	logging.debug("These are the arguments: s%",(arguments))
	command = arguments.pop("command")

	if command == "put":
		logging.debug("Inside put function")
		name, snippet = put(**arguments)
		print("Stored {!r} as {!r}".format(snippet,name))
	elif command == "get":
		name = get(**arguments)
		if name:
			print("Retrieved snippet:{!r}".format(name))
	elif command == "delete":
		name = delete(**arguments)
		print("Deleted snippet:{!r}".format(name))
	elif command == "update":
		name, newname, newsnippet = update(**arguments)
		print("Updated {!r} to {!r} saying: {!r}".format(name,newname,newsnippet))
	elif command == "catalog":
		entries = catalog(**arguments)
		print("These are all the DB entries: {!r}".format(entries))
	elif command == "search":
		logging.debug("In search elif")
		searchresult = search(**arguments)
		print("These are the search results: {!r}".format(searchresult))


# A couple of stubs
def put(name,snippet,hide):
	"""
	Store a snippet with an associated name.
	Returns the name and the snippet.
	"""
	logging.info("Storing snippet ({!r},{!r})".format(name,snippet))
	try:
		with connection, connection.cursor() as cursor:
			cursor.execute("Insert into snippets values (%s,%s)",(name, snippet))
	except psycopg2.IntegrityError as e:
		with connection, connection.cursor() as cursor:
			cursor.execute("update snippets set message=%s where keyword=%s",(snippet,name))
	if hide:
		with connection, connection.cursor() as cursor:
			cursor.execute("update snippets set hidden = 'True' where keyword=%s",(name))

	logging.debug("Snippet stored successfully.")
	return name, snippet


def get(name):
	"""
	Retrieve the snippet with a given name.
	If there's no such snippet, show message: "Entry not found, pls check for spelling errors"
	Returns the snippet.
	"""
	logging.info("Retrieving snippet {!r}".format(name))
	with connection, connection.cursor() as cursor:
		cursor.execute("select message from snippets where keyword=%s", (name,))
		row = cursor.fetchone()
	logging.debug("Retrieved snippet successfully.")
	if not row:
		print "Entry not found, pls check for spelling errors"
	else:
		return row[0]

def delete(name):
	"""
	Delete the snippet with a given name.
	If there's no such snippet, show message: "Entry not found, pls check for spelling errors"
	Returns the snippet.
	"""
	logging.error("FIXME: Unimplemented - get({!r})".format(name))
	return name

def update(name, newname, newsnippet):
	"""
	Update the snippet with a given name.
	If there's no such snippet, show message: "Entry not found, pls check for spelling errors"
	Returns the snippet.
	"""
	logging.error("FIXME: Unimplemented - get({!r})".format(name))
	return name, newname, newsnippet

	#####>>>> Enter subcommand "--unhide" here????

def catalog():
	"""
	Get a list of all DB entries
	"""
	logging.info("Retrieving DB entries")
	with connection, connection.cursor() as cursor:
		cursor.execute("select * from snippets")
		entries = cursor.fetchall()
	logging.debug("Retrieved entries successfully.")
	return entries

def search(query):
	"""
	Searches for a string in the message and returns the keys and messages.
	"""
	logging.info("Searching for {!r}".format(query))
	with connection, connection.cursor() as cursor:
		cursor.execute("select * from snippets where message like %s" %("'"'%' + query + '%'"'"),)
		searchresult = cursor.fetchall()
	logging.debug("Retrieved search results for {!r} successfully.".format(query))
	return searchresult    
    
    
if __name__ == "__main__":
	main()


