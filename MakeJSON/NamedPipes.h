

#ifndef MAKEJSON_NAMEDPIPES_H
#define MAKEJSON_NAMEDPIPES_H
//header voor windows systeem
#ifdef _WIN64
HANDLE createPipe(char * pipename);
//returnt een array met de geleze info
char *readPipe(HANDLE pipename, int size);
//schrijft info naar de pipe
int writePipe(HANDLE pipename, char *message);
//opent een bestaande pipe
HANDLE openPipe(char * pipename);
#endif
//header voor linux systeem
#ifdef __linux__
int createPipe(char * pipename);
#endif

#endif //MAKEJSON_NAMEDPIPES_H
