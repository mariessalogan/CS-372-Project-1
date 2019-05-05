# CS-372-Project-1
Socket programming - creating a simple chat server and client



#chatserve.py
#the python code to run the server
Compile/run by writing in command line: 
   python chatserve.py [your IP address] [Port number to run on]
   for example python chatserve.py 128.56.45.3.1 3676
   
#chatclient.c
#the c code to run the client
Compile by using gcc -o chatclient chatclient.c
Run by using ./chatclient [server IP Address] [server port number]
  for example ./chatclient 128.56.45.3.1 3676
  
To start both, first run server, then run client.  When your client connects it should post a message in the server with the client's ip address
Then it will ask for the client's username in the client window. Enter that and hit enter. 
The client will have to start the conversation. Once they send a message to the server, the server can reply, continuing on forever
if the client wants to quit, type in "quit". If the server wants to quit, type in "\quit".  
