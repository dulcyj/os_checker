import subprocess
import ConfigParser
import xml.etree.ElementTree as ET

class my_os:
	
	
	os_name = "unknown"
	xml_root = ET.Element('root')
 	
	def __init__(self):
		print "what is my  computer"
		config = ConfigParser.RawConfigParser()
                config.read('config.cfg')
                verbosity = config.get("general","log-level")
		print verbosity
		b = ET.SubElement(self.xml_root, 'b')
		ET.dump(self.xml_root)
		ET.ElementTree(self.xml_root).write("output.xml")
	def whoami(self):
		print "who ami"
		me = subprocess.check_output(["whoami"])
		print me
	def osinfo(self):
		print "os info"
		#os1 = subprocess.check_output(["cat /etc/issue"])
		#os2 = subprocess.check_ouput(["uname -a"])
		#print os1 + os2 
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
