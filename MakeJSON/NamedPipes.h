

#ifndef MAKEJSON_NAMEDPIPES_H
#define MAKEJSON_NAMEDPIPES_H
//header voor windows systeem
#ifdef _WIN64
void createPipe(char * pipename);
#endif
//header voor linux systeem
#ifdef __linux__
void createPipe(char * pipename);
#endif

#endif //MAKEJSON_NAMEDPIPES_H
