/*************************************************************************************************
Name: Mariessa Logan
FileName: chatclient.c
Date: 5/5/19
Description: This is the client side application of the chat that works with chatserve.py.
Sources: lectures, stack overflow, cs.rpi.edu
*************************************************************************************************/
#include <unistd.h>
#include <stdio.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>
int main(int argc, char const *argv[])
{
	

	//Check that the server ip and port are in the command line
	if(argc < 3)
	{
		printf("Error, please put server IP address and port in the command\n");
	}
	printf("Server IP Address is %s, Port is %s\n", argv[1], argv[2]);
	printf("If you want to leave the chat, type \"quit\"\n");
	int sock = socket(AF_INET, SOCK_STREAM, 0);
	if(sock < 0)
	{
		printf("Socket was not created :(\n");
		return -1;
	}
	struct sockaddr_in client_Address;
	struct sockaddr_in server_Address;
    
	server_Address.sin_family = AF_INET;
    server_Address.sin_addr.s_addr = inet_addr(argv[1]);
	server_Address.sin_port = htons(atoi(argv[2]));
    if (connect(sock, (struct sockaddr *)&server_Address, sizeof(server_Address)) != 0) {
        printf("connection with the server failed...\n");
        exit(0);
    }
	char username[10];
	int i = 0;
	char message[500];
	char rec_message[500];
	int is_it_read;
	printf("What's your name?\n");
		scanf("%s", username);
		printf("Your name is: %s\n", username);
		send(sock , username , strlen(username) , 0 );
	while (i == 0)
	{
		printf("%s >...", username);
		scanf("%s", message);
		printf("For tests %s", message);
		send(sock , message , strlen(message) , 1024 );
		read(sock, rec_message, 1024);
		printf("Server > %s\n", rec_message);
		memset(rec_message, '\0', 500);
		memset(message, '\0', 500);
		if(strcmp(message, "quit") == 0)
			{
				printf("Have fun storming the castle!\n");
				return 0;
			}
	}
	return 0;
}