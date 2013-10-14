import subprocess
import ConfigParser
import xml.etree.ElementTree as ET
from xml.dom import minidom

class my_os:
	
	
	os_name = "unknown"
	xml_root = ET.Element('root')
 	
	def __init__(self):
		print "what is my  computer"
		config = ConfigParser.RawConfigParser()
                config.read('config.cfg')
                verbosity = config.get("general","log-level")
		general_xml = ET.SubElement(self.xml_root, "general")
		verbosity_xml = ET.SubElement(general_xml, "verbosity")
		verbosity_xml.text = verbosity 	
		print verbosity 	
	def whoami(self):
		print "who ami"
		me = subprocess.check_output(["whoami"])
		group = subprocess.check_output(["groups"])
		user = ET.SubElement(self.xml_root, "user")
		user.text = me.rstrip('\n')
		group_xml = ET.SubElement(self.xml_root,"group")
		group_xml.text = group.rstrip('\n')
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
	def export(self):
		rough_string = ET.tostring(self.xml_root, 'utf-8')
		reparsed = minidom.parseString(rough_string)
		print reparsed.toprettyxml(indent="  ")
		ET.dump(self.xml_root)
		ET.ElementTree(self.xml_root).write("output.xml")


if __name__ == '__main__':
	me = my_os()
	me.whoami()
	me.osinfo()
	me.network_info()
	me.export()
