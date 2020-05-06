from sys import argv

script, filehandle = argv
txt = open(filehandle)
print txt.read()
txt.close()
