import urllib2, json, smtplib, threading

def sendmail(msg):
	fromaddr = '#From Email adress'
	toaddrs = '#To Email adress'
	
	#Credentials
	
	username = ''
	password = ''
	
	#The actual send
	
	server = smtplib.SMTP("smtp.gmail.com", 587) #Defines server adress and port
	server.ehlo() 
	server.starttls()
	server.login(username,password) #logs in to server
	server.sendmail(fromaddr, toaddrs, msg) #actual part where mail is sent
	server.close() #closes connection
	#print "Sent mail succesfully" #for debug purposes

def checker():
	if exchange < 0.55: 
		#print "Time to cash in" #for debug
		sendmail("""The exchange rate is %s GBP to 1 CAD""" % exchange)
		#threading.Timer(43200, checker).start() #after 12h, checker func is run
	else:
		#print "Not time yet"
		threading.Timer(43200.0, checker).start() #after 12h, checker func is run
def maintenance():
	#print "The CAD To GBP Exchange script is still running."
	sendmail("The CAD To GBP Exchange script is still running.")
	threading.Timer(60.0, maintenance).start()
	
data = json.load(urllib2.urlopen('https://rate-exchange.herokuapp.com/fetchRate?from=CAD&to=GBP')) #loads a json api's contents into a dictionary named data
exchange = data[u'Rate'] #selects the rate key from dictionary
#print exchange #prints for debug purposes

maintenance()
sendmail("Testing initial run. It works!") #startup email
