import subprocess


class my_os:
	os_name="unknown"
	
	def __init__(self):
		print "what is my  computer"
	def whoami(self):
		print "who ami"
		subprocess.call(["whoami"])
	def osinfo(self):
		print "os info"
		subprocess.call(["cat","/etc/issue"])
	def network_info(self):# not working
		print "info on "
		subprocess.call(["ping", "-b", "3", "8.8.8.8"])	
	def test_network(self):
		print "start"	


if __name__ == '__main__':
	me = my_os()
	me.whoami()
	me.osinfo()
	#me.network_info()
