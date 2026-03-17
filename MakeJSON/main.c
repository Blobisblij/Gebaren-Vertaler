#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include "cJSON.h"
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
    cJSON *root = cJSON_CreateArray();

    // Create JSON object
    cJSON *obj1 = cJSON_CreateObject();
    cJSON_AddNumberToObject(obj1, "X", 10);
    cJSON_AddNumberToObject(obj1, "Y", 20);
    cJSON_AddNumberToObject(obj1, "Z", 30);
    cJSON_AddItemToArray(root, obj1);

    // Create JSON object
    cJSON *obj2 = cJSON_CreateObject();
    cJSON_AddNumberToObject(obj2, "A", 1);
    cJSON_AddNumberToObject(obj2, "B", 2);
    cJSON_AddNumberToObject(obj2, "C", 3);
    cJSON_AddItemToArray(root, obj2);

    // Convert to string
    char *json_str = cJSON_Print(root);

    // Write to file
    FILE *fp = fopen("data.json", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        cJSON_Delete(root);
        free(json_str);
        return 1;
    }

    fputs(json_str, fp);
    fclose(fp);

    printf("JSON saved to data.json\n");

    // Cleanup
    cJSON_Delete(root);
    free(json_str);

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
