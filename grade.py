from subprocess import check_output


tests = [
    ("strlen", "helloworld"),
# ]
    ("strcpy", "hi"),
    ("strcpy", ""),
    ("strcpy", "hello world"),
    ("strcpy", " "),
    ("strlen", "helloworld"),
    ("strlen", ""),
    ("strlen", "0"),
    ("strlen", " "),
    ("strlen", "sjsjsjsjsjsjsjsjsjsjsjsjsjsjsjs"),
    ("strlen", ";alskdjf;alk"),
    ("strcmp", "hello", "hello"),
    ("strcmp", "", "hello"),
    ("strcmp", "hello", ""),
    ("strcmp", "", ""),
    ("strcmp", "hello", "helloo"),
    ("strcmp", "helloo", "hello"),
    ("strcmp", "hello", "nope"),
    ("strcmp", "hella", "hello"),
    ("strcmp", "hello", "hella"),
    ("strcmp", "abcdefghijkl", "abcdefghijkm"),
    ("strncmp", "hello", "hello", "3"),
    ("strncmp", "", "hello", "4"),
    ("strncmp", "hello", "", "5"),
    ("strncmp", "hella", "hello", "5"),
    ("strncmp", "hella", "he", "10"),
    ("strncmp", "he", "hello", "10"),
    ("strncmp", "hi", "hello", "10"),
    ("strncmp", "", "", "4"),
    ("strncmp", "bello", "hello", "0"),
    ("strncmp", "hello", "hel", "1"),
    ("strncmp", "hello", "hel", "-1"),
    ("strchr", "something", "m"),
    ("strchr", "hello", "a"),
    ("strchr", "", "b"),
    ("strchr", "hello", "h"),
    ("strchr", "hello", "o"),
    ("strchr", "hello", "0"),
    ("strchr", "hello world", " "),
    ("strchr", "hello lo", "l"),
    ("strchr", "", "0"),
    ("strncat", "hello", "b", "5"),
    ("strncat", "hello", "b", "6"),
    ("strncat", "", "-", "6"),
    ("strncat", "he", "b", "6"),
    ("strncat", "hello", "-", "0"),
    ("strncat", "hello", "-", "15"),
    ("strncat", "hello;lkj;lkjdjdj", "b", "6"),
    ("strncat", "hello", "-", "-1"),
    ("strrchr", "something", "m"),
    ("strrchr", "hello", "a"),
    ("strrchr", "", "b"),
    ("strrchr", "hello", "h"),
    ("strrchr", "hello", "o"),
    ("strrchr", "hello", "0"),
    ("strrchr", "", "0"),
    ("strrchr", "hello world", " "),
    ("strrchr", "hello lo", "l"),
    ("strrchr", "", "0"),
    ("strrchr", "hello world", " "),
    ("strrchr", "hello lo", "l"),
    ("strrchr", "", "0"),
    ("strstr", "hello", "hello"),
    ("strstr", "hello", ""),
    ("strstr", "", "hello"),
    ("strstr", "he", "hello"),
    ("strstr", "hello", "h"),
    ("strstr", "h", "h"),
    ("strstr", "hellaaaaa", "he"),
    ("strstr", "", ""),
    ("strstr", "hello", "l"),
    ("strstr", "'hel askdjfal;slkdjf", "e"),
    ("memmove",),
    ("memmove",), 
    ("memset",), 
    ("strcspn", "haystack has a needle", "needle"),
    ("strcspn", "", "needle"),
    ("strcspn", "haystack has a needle", ""),
    ("strcspn", "", ""),
    ("strcspn", "needle", ""),
    ("strcspn", ";alskdj;alksjt;lkaj;rlg", "ad;slkfj;lsdkhgjkvlnjlfkajn"),
    ("strcspn", "world hello", "hello world"),
    ("strcspn", "hays", "needle a;lkdja;lksdjf"),
    ("strcspn", "haystack has a needle", "ne"),
    ("strcat", "hello", "hello"),
    ("strcat", "", "hello"),
    ("strcat", "hello", ""),
    ("strcat", "", ""),
    ("strcat", "hello", "nope"),
    ("strcat", "h", "n"),
    ("strcat", "hellosadflkjfl;kjrkr", "ne"),
    ("strcat", "h", "novhvjfjdkdkslkdj;flkdjfe"),
    ("strncpy", "hello", "5"),
    ("strncpy", "hello", "6"),
    ("strncpy", "", "6"),
    ("strncpy", "he", "6"),
    ("strncpy", "hello;lkj;lkjdjdj", "6"),
    ("strncpy", "hello", "0"),
    ("strncpy", "hello", "0"),
    ("strncpy", "hello", "8"),
    ("strncpy", "", "1"),
    ("strncpy", "hello", "10"),
    ("strncpy", "hello", "7"),
    ("strncpy", "hello", "5"),
    ("strcmp", "hello", "hello"),
    ("strcmp", "hello", "nope"),
    ("strncmp", "hello", "hello", "3"),
    ("strchr", "something", "m"),
    ("memmove",),
    ("memmove",),
    ("memset",),
    ("strcspn", "haystack has a needle", "needle"),
    ("strcpy", ""),
    ("strcpy", "hello world"),
    ("strcpy", "weeb"),
    ("strchr", "hello", "h"),
    ("strchr", "hello", "hi"),
    ("strchr", "hello", "helloooo"),
    ("strchr", "hello", "x"),
    ("strrchr", "hello", "h"),
    ("strrchr", "hello", "hi"),
    ("strrchr", "hello", "helloooo"),
    ("strrchr", "hello", "x"),
    ("memmove",),
    ("memmove",),
    ("memmove",),
    ("memmove",),
    ("strncat", "hello", "hi", "1"),
    ("strncat", "hello", "world", "5"),
    ("strncat", "hello", "world", "1000"),
    ("strncat", "hello", "world", "0"),
    ("strncmp", "hello", "hellllo", "4"),
    ("strncmp", "hello", "world", "1"),
    ("strncmp", "hello", "hello", "6"),
    ("strncmp", "hiiii", "iii", "3"),
    ("strcmp", "hello", "world"),
    ("strcmp", "hello", "hell"),
    ("strcmp", "hello", "helloooo"),
    ("strcmp", "hello", "hello"),
    ("strstr", "hello", "hello"),
    ("strstr", "hello", "world"),
    ("strstr", "helloooo", "hell"),
    ("strstr", "hell", "hello"),
    ("strlen", ""),
    ("strlen", "hello"),
    ("strlen", "hello world"),
    ("memset",),
    ("memset",),
    ("memset",),
    ("memset",),
    ("strcat", "hello", "world"),
    ("strcat", "hello", ""),
    ("strcat", "", "hello"),
    ("strcat", "helloooo", "helloooo"),
    ("strncpy", "hello world",  "5"),
    ("strncpy", "hello world", "0"),
    ("strncpy", "hello world", "3"),
    ("strcspn", "hello world", "world"),
    ("strcspn", "hello world", "xqvzy"),
    ("strcspn", "hello world", "hello"),
    ("strcspn", "weeb", "weeb")，
#
# As you do the assignment, you can put more tests into the tests array.
# Here's a few. Don't forget to separate them with a comma
#

    ("strcmp", "hello", "hello"),
    ("strcmp", "hello", "nope"),
    ("strncmp", "hello", "hello", "3"),
    ("strchr", "something", "m"),
    ("memmove",),  #memmove test takes no parameter
    ("memmove",),  #the comma inside the tuple is important
    ("memset",),   #same with memset
    ("strcspn", "haystack has a needle", "needle"),
    ("strcpy", "hello world"),
    ("strncpy", "hello world", "5"),
    ("strrchr", "hello world", "l"),
    ("strcat", "hello ", "world"),
    ("strncat", "hello ", "world", "10"),
    ("strstr", "hello world", "way")
]

for test in tests:
    cmd = ["./grade"] + list(test)
    print("test: {}    {}".format(test, "CORRECT" if "1" in str(check_output(cmd)) else "WRONG"))

