import logging
import argparse
import sys


# Set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)


# A couple of stubs
def put(name,snippet):
	"""
	Store a snippet with an associated name.
	Returns the name and the snippet.
	"""
	logging.error("FIXME Unimplemented - put({!r},{!r})".format(name,snippet))
	return name, snippet

put("list","A sequence of things created by []")

def get(name):
	"""
	Retrieve the snippet with a given name.

	If there's no such snippet, show message: "Entry not found, pls check for spelling errors"

	Returns the snippet.
	"""
	logging.error("FIXME: Unimplemented - get({!r})".format(name))
	return name

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



# Main function
def main():
	"""Main function"""
	logging.info("Constructing parser")
	parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")

	# Add subparsers
	subparsers = parser.add_subparsers(dest="command", help="Available commands")

	# Subparser for the put command
	logging.debug("Constructing put subparser")
	put_parser = subparsers.add_parser("put",help="Stores a snippet")
	put_parser.add_argument("name",help="The name of the snippet")
	put_parser.add_argument("snippet",help="The snippet text")

	# Subparser for the get command
	logging.debug("Constructing get subparser")
	get_parser = subparsers.add_parser("get",help="Retrieves a snippet")
	get_parser.add_argument("name",help="The name of the snippet")

	# Subparser for the delete command
	logging.debug("Constructing delete parser")
	delete_parser = subparsers.add_parser("delete",help="Deletes a snippet")
	delete_parser.add_argument("name",help="The name of the snippet")

	# Subparse for the update command
	logging.debug("Constructing update parser")
	update_parser = subparsers.add_parser("update",help="Updates a snippet")
	update_parser.add_argument("name",help="The name of the snippet")
	update_parser.add_argument("newname",help="The new name of the snippet")
	update_parser.add_argument("newsnippet",help="The new snippet")

	arguments = parser.parse_args(sys.argv[1:])
	arguments = vars(arguments)
	command = arguments.pop("command")

	if command == "put":
		name, snippet = put(**arguments)
		print("Stored {!r} as {!r}".format(snippet,name))
	elif command == "get":
		name = get(**arguments)
		print("Retrieved snippet:{!r}".format(name))
	elif command == "delete":
		name = delete(**arguments)
		print("Deleted snippet:{!r}".format(name))
	elif command == "update":
		name, newname, newsnippet = update(**arguments)
		print("Updated {!r} to {!r} saying: {!r}".format(name,newname,newsnippet))

if __name__ == "__main__":
	main()


