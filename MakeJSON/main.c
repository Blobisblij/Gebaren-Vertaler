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
#include <unistd.h>
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
        	const LEAP_TRACKING_EVENT* frame = msg.tracking_event;

        	if (frame && frame->nHands > 0)
        	{
        		int numHands = frame->nHands;
        		printf("Hands: %d\n", numHands);

        		const LEAP_HAND* hand1 = &frame->pHands[0];

				LEAP_VECTOR palm = hand1->palm.position;

				for (int i = 0; i < 5; i++)
				{
				    LEAP_DIGIT digit = hand1->digits[i];
				    LEAP_VECTOR tip = digit.bones[3].next_joint;

				    LEAP_VECTOR delta;
				    delta.x = tip.x - palm.x;
				    delta.y = tip.y - palm.y;
				    delta.z = tip.z - palm.z;

				    printf("Finger %d delta: %d, %d, %d\n", i, (int)delta.x, (int)delta.y, (int)delta.z);
				}
        	}
        	else
        	{
        		printf("No hands detected\n");
			}

        }
    }
    printf("No Connection");
    LeapCloseConnection(connection);
    LeapDestroyConnection(connection);
    //close the pipe
    //closePipe(pipe);
//delete pipe from files not needed in windows
//#ifdef __linux__
    //remove(pipename);
//#endif
    //free(pipename);
    return 0;
}
