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
    LEAP_CONNECTION connection = NULL;
    eLeapRS result = LeapCreateConnection(NULL, &connection);
    if (result != eLeapRS_Success) return 1;
    LeapOpenConnection(connection);

    LEAP_CONNECTION_MESSAGE msg;
    LEAP_TRACKING_EVENT* frame = NULL;

    while (result == eLeapRS_Success) {
        // Poll for next message
        result = LeapPollConnection(connection, 1000, &msg);
        if (result != eLeapRS_Success) continue;

        if (msg.type == eLeapEventType_Tracking) {
            frame = msg.tracking_event;

            if (frame->nHands > 0) {
                int numHands = frame->nHands;
                printf("Hands: %d | ",numHands);

                const LEAP_HAND* hand1 = &frame->pHands[0]; // first hand
                float x_h1 = hand1->palm.position.x;
                float y_h1 = hand1->palm.position.y;
                float z_h1 = hand1->palm.position.z;
                printf("Palm Hand 1: x=%.0f y=%.0f z=%.0f\n", x_h1, y_h1, z_h1);

                if (numHands > 1) {
                    const LEAP_HAND* hand2 = &frame->pHands[1]; // 2nd hand
                    float x_h2 = hand2->palm.position.x;
                    float y_h2 = hand2->palm.position.y;
                    float z_h2 = hand2->palm.position.z;
                    printf(" | Palm Hand 2: x=%.0f y=%.0f z=%.0f\n", x_h2, y_h2, z_h2);
                }
            } else {
                printf("No hands detected\n");
            }
        }
    }
    printf("No Connection");
    LeapCloseConnection(connection);
    LeapDestroyConnection(connection);
    //close the pipe
    closePipe(pipe);
//delete pipe from files not needed in windows
#ifdef __linux__
    remove(pipename);
#endif
    free(pipename);
    return 0;
}
