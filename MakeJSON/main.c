#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include "memoryalocation.h"
#include "NamedPipes.h"
#include <time.h>
#ifdef __linux__
#include <LeapC.h>
#endif
#ifdef _WIN64
#include <bemapiset.h>
#include <windows.h>
#include "C:\Program Files\Ultraleap\LeapSDK\include/LeapC.h"
#endif

int main() {
    // Create root array

    //maak ipc pipe aan

#ifdef __linux__
    char *pipename = createArrayString(13);
    strcpy(pipename, "/tmp/Leapcam");
    int pipe = createPipe(pipename);
#endif

#ifdef _WIN64
    char *pipename = createArrayString(17);
    strcpy(pipename, "\\\\.\\pipe\\Leapcam");
    HANDLE pipe = createPipe(pipename);
#endif

    //close the pipe
    closePipe(pipe);
//delete pipe from files not needed in windows
#ifdef __linux__
    remove(pipename);
#endif
    free(pipename);
    return 0;
}
