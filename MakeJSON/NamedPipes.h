
#ifndef MAKEJSON_NAMEDPIPES_H
#define MAKEJSON_NAMEDPIPES_H
//header voor windows systeem
#ifdef _WIN64
#include <windows.h>
HANDLE createPipe(char * pipename);
//returnt een array met de geleze info
char *readPipe(HANDLE pipename, int size);
//schrijft info naar de pipe
int writePipe(HANDLE pipename, char *message);
//opent een bestaande pipe
HANDLE openPipe(char * pipename);
//sluit een bestaande pipe
int closePipe(HANDLE pipename);
#endif
//header voor linux systeem
#ifdef __linux__
//makes a pipe
int createPipe(char * pipename);
//reads from pipe
char *readPipe(int pipe, int size);
//writes to pipe
int writePipe(int pipe, int *message);
//opens a pipe
int openPipe(char * pipename);
//closes a pipe
int closePipe(int pipe);
#endif

#endif //MAKEJSON_NAMEDPIPES_H
