#include "my_string.h"


char * my_strcpy( char * destination, const char * source )
{
    //your code goes here
    char *my_str = destination;
    while(*source)
    {
        *destination++ = *source++;
    }
    *destination = 0;
    return my_str;
}

char * my_strchr ( const char * str, int character )
{
    while (*str != (char) character){
        if (!*str++) {
            return 0;
        }
    }
    return (char *) str;
}

void * my_memmove ( void * destination, const void * source, size_t num )
{
    char *dest = (char *) destination;
    char *s = (char *) source;
    if(dest < s) {
		while(num--)
			*dest++ = *s++;
	} else {
		dest += num;
		s += num;
		while(num--)
			*--dest = *--s;
	}
}

char * my_strncat ( char * destination, const char * source, size_t num )
{
    char *my_str = destination;
    while (*destination) {
        destination++;
    }
    while(num--){
        *destination++ = *source;
        if (!*source++){
            return my_str;
        }
    }
    *destination = 0;
    return my_str;
}

int my_strncmp ( const char * str1, const char * str2, size_t num )
{
    while (num--) {
        if (!*str1 || *str1 != *str2) {
            return *(unsigned char *) str1 - *(unsigned char *) str2;
        }
        str1++;
        str2++;
    }
    return 0;
}

int my_strcmp ( const char * str1, const char * str2 )
{
    do {
        if (!*str1) {
            return *(unsigned char *)str1 - *(unsigned char *)str2;
        }
    } while (*str1++ == *str2++);
    return *(unsigned char *)(str1 - 1) - *(unsigned char *)(str2 - 1);
}

char * my_strrchr ( const char * str, int character )
{
    char *my_str = 0;
    while (*str) {
        if (*str == (char) character) {
            my_str = str;
        }
        str++;
    }
    return my_str;
}

char * my_strstr ( const char * str1, const char * str2 )
{
    char *str1_copy, *str2_copy;
    if (!*str2) {
        return str1;
    }
    while (*str1) {
        if (*str1 == *str2){
            str1_copy = str1;
            str2_copy = str2;
            while(1) {
                if (!*str2_copy) {
                    return str1;
                }
                if (*str1_copy++ != *str2_copy++) {
                    break;
                }
            }
        }
        str1++;
    }
    return (char *) 0;
}