#include <bemapiset.h>
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
#include <windows.h>
#ifdef __linux__
#include <LeapC.h>
#endif
#ifdef _WIN64
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

    int *lijstie = createArrayInt(5);

    lijstie[0] = 0;
    lijstie[1] = 3;
    lijstie[2] = 2;
    lijstie[3] = 3;
    lijstie[4] = 4;
//testje
    printf("lijstie[0] = %d\n", lijstie[0]);
    printf("lijstie[1] = %d\n", lijstie[1]);
    printf("lijstie[2] = %d\n", lijstie[2]);
    printf("lijstie[3] = %d\n", lijstie[3]);
    printf("lijstie[4] = %d\n", lijstie[4]);
    free(lijstie);

    //maak ipc pipe aan
#ifdef __linux__
    char *pipename = createArrayString(13);
    strcpy(pipename, "/tmp/Leapcam");
#endif

#ifdef _WIN64
    char *pipename = createArrayString(17);
    strcpy(pipename, "\\\\.\\pipe\\Leapcam");
#endif

    char *woordje = createArrayString(8);
    strcpy(woordje, "woordje");
    HANDLE pipe = createPipe(pipename);

    sleep(10);

    writePipe(pipe, woordje);

    CloseHandle(pipe);

    //int size = sizeof(woordje);
    //char *woorduit = readPipe(pipe,size);
    //printf("%s\n",woorduit);




    /*

    int pipe = open(pipename, O_RDWR);

    write(pipe,woordje,strlen(woordje));

    char woorduit[8];
    read(pipe,woorduit,sizeof(char)*8);
    printf("%s\n", woorduit);
    close(pipe);
    */

    //track en schijf loop

    return 0;
}
