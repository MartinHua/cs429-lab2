#include <stdio.h>

#include <string.h>
#include "my_string.h"



int main(int argc, char** argv)
{
    char *str1, *str2;
    //allocate dynamic memory, 100 bytes for each string
    str1 = (char*) malloc(100);
    str2 = (char*) malloc(100);

    //this is static memory, does not need malloc or free since
    //the compiler knows how much memory it needs, it reserves on
    //compile time, NOT run time
    char str3[100];
    char str4[100];

    strcpy(str1, "this is a string");
    strcpy(str2, "this is another string");


    /*****************************
     *  Testing strlen
     *****************************/

    printf("str1 strlen: %zu  my_strlen: %zu   are they equal?  %s\n",
        strlen(str1), my_strlen(str1),  
        strlen(str1) == my_strlen(str1) ? "yes" : "no" );
    
    strcpy(str3, "this is a string");
    my_memset(str3, '-', 5);
    strcpy(str4, "this is a string");
    memset(str4, '-', 5);
    printf("memset ?  %s\n%s\n%s\n", strcmp(str3, str4) == 0 ? "yes" : "no", str3, str4 );

    strcpy(str3, "this is a string");
    strcpy(str4, "this is a string");
    printf("%s\n%s\n", str3, str4);
    printf("strcat ?  %s\n%s\n", my_strcat(str3, str1), strcat(str4, str1) );

    strcpy(str3, "this is a string");
    strcpy(str4, "this is a string");
    my_strncpy(str3, str2, strlen(str2)+10);
    strncpy(str4, str2, strlen(str2)+10);
    printf("strncpy ?  %s\n", my_strcmp(str3, str4) == 0 ? "yes" : "no" );

    printf("strcspn ?  %s\n", my_strcspn(str1, "TMD") == strcspn(str1, "TMD") ? "yes" : "no" );
    printf("strcspn ?  %s\n", my_strcspn(str1, str2) == strcspn(str1, str2) ? "yes" : "no" );
    
    //'zu' is the format used to print the type size_t, which is what strlen returns
    //third print is a ternary operator, not necessary to know, just cool, pretty much a if-else in one statement

    //TODO: you should do more tests, especially corner cases, like empty strings.



    /*****************************
     *  Testing strcpy
     *****************************/

    //copying the same string as str1 into str3, compare to see if equal
    my_strcpy(str3, "this is a string");
    printf("strcpy str1 == str3 ?  %s\n", strcmp(str1, str3) == 0 ? "yes" : "no" );

    printf("strchr ? %s\n", strcmp(my_strchr(str1, 'i'), strchr(str1, 'i')) == 0 ? "yes" : "no" );
    printf("strchr ? %s\n", my_strchr(str1, 'T') == strchr(str1, 'T') ? "yes" : "no" );

    strcpy(str3, "this is a string");
    strcpy(str4, "this is a string");
    my_memmove(str3, str2, strlen(str2));
    memmove(str4, str2, strlen(str2));
    printf("memmove ? %s\n", strcmp(str3, str4) == 0 ? "yes" : "no" );
    
    strcpy(str3, "this is a string");
    strcpy(str4, "this is a string");
    printf("strncat ? %s\n", strcmp(my_strncat(str3, str2, strlen(str2)), strncat(str4, str2, strlen(str2))) == 0 ? "yes" : "no" );
    
    strcpy(str3, "this is a string");
    strcpy(str4, "this is a string");
    printf("strncmp ? %s\n", my_strncmp(str1, str2, 100) == strncmp(str1, str2, 100) ? "yes" : "no");
    printf("strncmp ? %s\n", my_strncmp(str1, str3, 100) == strncmp(str1, str3, 100) ? "yes" : "no");

    printf("strcmp ? %s\n", my_strcmp(str1, str2) == strcmp(str1, str2) ? "yes" : "no");
    printf("strcmp ? %s\n", my_strcmp(str1, str3) == strcmp(str1, str3) ? "yes" : "no");

    printf("strrchr ? %s\n", strcmp(my_strrchr(str1, 'i'), strrchr(str1, 'i')) == 0 ? "yes" : "no" );
    printf("strrchr ? %s\n", my_strrchr(str1, 'T') == strrchr(str1, 'T') ? "yes" : "no" );

    printf("strstr ? %s\n", strcmp(my_strstr(str1, "is"), strstr(str1, "is")) == 0 ? "yes" : "no" );
    printf("strstr ? %s\n", my_strstr(str1, "another") == strstr(str1, "another") ? "yes" : "no" );
    //TODO: more tests...



    /*****************************
     *  Testing <insert function here>
     *****************************/

    //TODO: this is where you test the other functions to make sure they work...
    //like in the real world, after you implement something, you have to test it
    //to make sure it works and doesn't break other parts of the code, or other
    //collaborators may be a little angry at you




    //before quiting the program, free all memory you allocated
    free(str1);
    free(str2);
    free(str3);
    free(str4);
    

    return 0;
}
