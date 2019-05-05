################################################################################################
###Name: Mariessa Logan
###Class: CS 372
###File Name: chatserve.py
###Date: 5/5/2019
###Description: This program will create a chat server that works with a c++ code chatclient 
###and allows the two to talk to each other. 
###Sources: Geeks for geeks, stack overflow, lectures, docs.python.org/3/library/socket.html
################################################################################################

import socket
import select
import sys


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#First step is to make sure there were a correct amount of arguments included
if len(sys.argv) != 3:
	print "Error!! Not enough arguments. Include IP address and port number"
	exit()

#IP address is the 2nd argument passed in the command line
#must use string operator instead of int 
server_IP_Address = str(sys.argv[1])

#Port is the 3rd, should be a simple number so int is ok
server_Port = int(sys.argv[2])

print " Server IP address and port are: ", server_IP_Address, " ", server_Port
print "Welcome! If you want to quit while the client is connected, please type \quit and the server will be shut down"
print "If you want to quit before the client connects, hit CTRL-Z"
#Creates a server at the given IP address and port number taken from python 3 documentation
server.bind((server_IP_Address, server_Port))
#Listens for active connections from clients. I have it set to 1 connection
server.listen(1)
client_Conn, client_Address = server.accept()
#alert server client is connected
print "The client at Address ", client_Address, " is connected"

#Receive names with a smaller character limit than a message
client_name = client_Conn.recv(10)


# This is a loop that will continue forever, unless \quit is called
while 1:
	
	#set the server to receive file and print message
	client_message = client_Conn.recv(4096)
	if client_message:
		print client_name, " > ", client_message
		
	##Handle the server messages
	server_Message = raw_input("... ")
	while(len(server_Message) < 1 or len(server_Message) > 500):
		print "Error, you can only type between 1-500 characters. Try again, keep it brief but not too brief"
		server_Message = raw_input("... ")
		
	
	if server_Message == "\quit":
		#server wants to quit, 
		print "Have fun storming the castle!"
		client_Conn.send("You're getting kicked now")
		client_Conn.close()
		server.close()
		exit()
	else:
		print "Server \n >", server_Message
		client_Conn.send(server_Message)