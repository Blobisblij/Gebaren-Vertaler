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
#include "memoryalocation.h"

// wrapper voor windows en linux named pipes zodat de aplicatie cross platform is


//Pipe code als systeem linux draaid
#ifdef __linux__
int createPipe(char *pipename) {
    mkfifo(pipename, 0600);
    int pipe = open(pipename,O_RDWR);
    if (pipe == 1) {
        printf("failed to open pipe");
        return 1;
    }
    return pipe;
}

char *readPipe(int pipe, int size) {
    char *readOutput = createArrayString(size);
    read(pipe, readOutput, size);
    return readOutput;
}

int writePipe(int pipe, int *message) {
    int succes = write(pipe,message,sizeof(message));

    if (!succes) {
        printf("failed to write to pipe");
        return 1;
    }
    return 0;
}

int openPipe(char *pipename) {
    int pipe = open(pipename,O_RDWR);
    if (pipe == 1) {
        printf("failed to open pipe");
        return 1;
    }
    return pipe;
}

int closePipe(int pipe) {
    close(pipe);
    return 0;
}
#endif




//Pipe code als systeem windows draait
#ifdef _WIN64
HANDLE createPipe(char * pipename) {
    HANDLE hPipe;
    LPCSTR pipeName = pipename;

    // Create the named pipe
    hPipe = CreateNamedPipe(
        pipeName,              // Name of the pipe
        PIPE_ACCESS_DUPLEX,    // Read/write access
        PIPE_TYPE_BYTE |       // Byte-type pipe
        PIPE_READMODE_BYTE |   // Byte read mode
        PIPE_WAIT,             // Blocking mode
        PIPE_UNLIMITED_INSTANCES, // Maximum instances
        512,                   // Output buffer size
        512,                   // Input buffer size
        100,                     // Default timeout
        NULL);                 // Default security attributes

    if (hPipe == INVALID_HANDLE_VALUE) {
        printf("Error creating named pipe: %ld\n", GetLastError());
        return 0;
    }

    printf("Named pipe created successfully.\n");
    return hPipe;
}
//schrijf naar pipe voor windows
int writePipe(HANDLE pipename, int *message) {
    // schrijf naar de pipe
    DWORD numberOfBytesWritten;
    printf("%s\n", message);
    BOOL file = WriteFile(pipename, message, strlen(message),&numberOfBytesWritten, NULL);

    if (!file) {
        printf("Error writing to pipe: %ld\n", GetLastError());
        return 1;
    }
    return 0;
}

char *readPipe(HANDLE pipename, int size) {
    //Wacht tot er een client verbind en info stuurt
    DWORD numberOfBytesRead;
    DWORD numberOfBytesToRead;
    char * pipeout = createArrayString(size);
    BOOL file = ReadFile(pipename, pipeout, sizeof(pipeout),&numberOfBytesToRead, NULL);
    if (!file) {
        printf("Error reading from pipe: %ld\n", GetLastError());
        return NULL;
    }
    return pipeout;
}

HANDLE openPipe(char * pipename) {
    // opend een al bestaande pipe
    HANDLE pipeHandle = CreateFile(pipename,
       GENERIC_READ,
       0,
       NULL,
       OPEN_EXISTING,
       0,NULL);
    //check error
    if (pipeHandle == INVALID_HANDLE_VALUE) {
        printf("Error creating named pipe: %ld\n", GetLastError());
        return 0;
    }
    return pipeHandle;
}

int closePipe(HANDLE pipename) {
    CloseHandle(pipename);
    return 0;
}
#endif