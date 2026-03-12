//
// Created by zooi on 3/12/26.
//
#include <stdio.h>
#include <stdlib.h>
#include "memoryalocation.h"

//Array in heap alocator
int* createArrayInt(int size)
{
    int* array = (int*)malloc(sizeof(int) * size);
    if (array == NULL)
    {
        printf("Error allocating memory\n");
        exit(1);
    }
    return array;
}
float* createArrayfloat(int size)
{
    float* array = (float*)malloc(sizeof(float) * size);
    if (array == NULL)
    {
        printf("Error allocating memory\n");
        exit(1);
    }
    return array;
}