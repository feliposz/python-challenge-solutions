import xmlrpc.client
url = "http://www.pythonchallenge.com/pc/phonebook.php"
proxy = xmlrpc.client.ServerProxy(url)
print(proxy.system.listMethods())
print(proxy.system.methodHelp("phone"))
#from http://www.pythonchallenge.com/pc/return/evil4.jpg
print(proxy.phone("Bert"))
#555-ITALY
