import logging
import argparse
import sys


# Set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)


# Main function
def main():
	"""Main function"""
	logging.info("Constructing parser")
	parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")
	arguments = parser.parse_args(sys.argv[1:])

if __name__ == "__main__":
	main()


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
	return ""



def delete(name):
	"""
	Delete the snippet with a given name.

	If there's no such snippet, show message: "Entry not found, pls check for spelling errors"

	Returns the snippet.
	"""
	logging.error("FIXME: Unimplemented - get({!r})".format(name))
	return ""


def update(name, newname, snippet):
	"""
	Update the snippet with a given name.

	If there's no such snippet, show message: "Entry not found, pls check for spelling errors"

	Returns the snippet.
	"""
	logging.error("FIXME: Unimplemented - get({!r})".format(name))
	return ""



