from subprocess import check_output


tests = [
    ("strlen", "helloworld"),
# ]

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

