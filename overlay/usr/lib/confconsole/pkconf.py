# Class for reading and writing PageKite configuration files

import os

conf_file = "/etc/pagekite.d/pagekite.rc"

def read():
	keys = []
	values = []
	if not os.path.exists(conf_file):
		f = open(conf_file, "w")
		f.close()
	
	for line in file(conf_file).readlines():
		if line.startswith("#"):
			continue
		try:
			key, value = line.split('=', 1)
		except:
			continue
		keys.append(key.strip())
		values.append(value.strip())

	return keys, values

def saveandreload(keys, values):
	f = open(conf_file, "w")
	f.write("defaults\n") # use the pagekite.net service
	i = 0
	for key in keys:
		f.write(key+"="+values[i]+"\n")
		i = i+1
	f.close()
	os.system("/usr/sbin/service pagekite restart")
	return

