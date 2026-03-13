#ifdef _WIN64
#include <windows.h>
#endif
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include "NamedPipes.h"

// wrapper voor windows en linux named pipes zodat de aplicatie cross platform is


//Pipe code als systeem linux draaid
#ifdef __linux__
void createPipe(char * pipename) {
    mkfifo(pipename, 0600);
}
#endif
//Pipe code als systeem windows draait
#ifdef _WIN64
void createPipe(char * pipename) {
    //
}
#endif