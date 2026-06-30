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
	int *deltaarray = createArrayInt(15*sizeof(int));
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

        		//delta maken en als int opslaam

        		LEAP_DIGIT thumb = hand1->digits[0];
        		LEAP_VECTOR thumb_tip = thumb.bones[3].next_joint;

        		int thumb_delta_x = (int)thumb_tip.x - (int)palm.x;
        		int thumb_delta_y = (int)thumb_tip.y - (int)palm.y;
        		int thumb_delta_z = (int)thumb_tip.z - (int)palm.z;

        		LEAP_DIGIT index = hand1->digits[1];
        		LEAP_VECTOR index_tip = index.bones[3].next_joint;

        		int index_delta_x = (int)index_tip.x - (int)palm.x;
        		int index_delta_y = (int)index_tip.y - (int)palm.y;
        		int index_delta_z = (int)index_tip.z - (int)palm.z;

        		LEAP_DIGIT middle = hand1->digits[2];
        		LEAP_VECTOR middle_tip = middle.bones[3].next_joint;

        		int middle_delta_x = (int)middle_tip.x - (int)palm.x;
        		int middle_delta_y = (int)middle_tip.y - (int)palm.y;
        		int middle_delta_z = (int)middle_tip.z - (int)palm.z;

        		LEAP_DIGIT ring = hand1->digits[3];
        		LEAP_VECTOR ring_tip = ring.bones[3].next_joint;

        		int ring_delta_x = (int)ring_tip.x - (int)palm.x;
        		int ring_delta_y = (int)ring_tip.y - (int)palm.y;
        		int ring_delta_z = (int)ring_tip.z - (int)palm.z;

        		LEAP_DIGIT pinky = hand1->digits[4];
        		LEAP_VECTOR pinky_tip = pinky.bones[3].next_joint;

        		int pinky_delta_x = (int)pinky_tip.x - (int)palm.x;
        		int pinky_delta_y = (int)pinky_tip.y - (int)palm.y;
        		int pinky_delta_z = (int)pinky_tip.z - (int)palm.z;

				//ints toevoegen aan array
        		//0

        		/*XYZcoord[0] = thumb_delta_x;
        		XYZcoord[1] = thumb_delta_y;
        		XYZcoord[2] = thumb_delta_z;*/
        		deltaarray[0] = thumb_delta_x;
        		deltaarray[1] = thumb_delta_y;
        		deltaarray[2] = thumb_delta_z;
        		//1
        		/*XYZcoord[0] = index_delta_x;
        		XYZcoord[1] = index_delta_y;
        		XYZcoord[2] = index_delta_z;*/
        		deltaarray[3] = index_delta_x;
        		deltaarray[4] = index_delta_y;
        		deltaarray[5] = index_delta_z;
				//2
        		/*XYZcoord[0] = middle_delta_x;
        		XYZcoord[1] = middle_delta_y;
        		XYZcoord[2] = middle_delta_z;*/
        		deltaarray[6] = middle_delta_x;
        		deltaarray[7] = middle_delta_y;
        		deltaarray[8] = middle_delta_z;
				//3
        		/*XYZcoord[0] = ring_delta_x;
        		XYZcoord[1] = ring_delta_y;
        		XYZcoord[2] = ring_delta_z;*/
        		deltaarray[9] = ring_delta_x;
        		deltaarray[10] = ring_delta_y;
        		deltaarray[11] = ring_delta_z;
				//4
        		/*XYZcoord[0] = pinky_delta_x;
        		XYZcoord[1] = pinky_delta_y;
        		XYZcoord[2] = pinky_delta_z;*/
        		deltaarray[12] = pinky_delta_x;
        		deltaarray[13] = pinky_delta_y;
        		deltaarray[14] = pinky_delta_z;

        		writePipe(pipe, deltaarray,60);

        		int i = 0;
        		while (i <= 14) {
        			printf("%d\t", deltaarray[i]);
        			i ++;
        		}

				//for (int i = 0; i < 5; i++)
				//{
				//    LEAP_DIGIT digit = hand1->digits[i];
				//    LEAP_VECTOR tip = digit.bones[3].next_joint;

				//    LEAP_VECTOR delta;
				//    delta.x = tip.x - palm.x;
				//    delta.y = tip.y - palm.y;
				//    delta.z = tip.z - palm.z;

				//    printf("Finger %d delta: %d, %d, %d\n", i, (int)delta.x, (int)delta.y, (int)delta.z);
				//}
        	}
        	else
        	{
        		writePipe(pipe, deltaarray,60);
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
#ifdef __linux__
    //remove(pipename);
#endif
	free(deltaarray);
	free(pipename);
    return 0;
}