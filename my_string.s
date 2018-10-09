.globl my_strlen
.globl my_memset
.globl my_strcat
.globl my_strncpy
.globl my_strcspn
#add a .globl for all other functions here

my_strlen:

    #rbp is a callee save register. this isn't really required because we are not
    #using the stack yet, but get used to it, these two lines are in pretty much 
    #every assembly function
    pushq %rbp
    movq %rsp, %rbp

    #lets say I want to use r12 and r13. Because they are callee save (the 
    #function that wants to use them must save) we need to push into the stack
    pushq %r12
    pushq %r13

    #end of prologue
    #the prologue of a function is only preparing for what we will do. it
    #involves saving callee registers and some other stuff, now we are actually
    #into the assembly code, the part that actually does something
    #more here:  https://en.wikipedia.org/wiki/Function_prologue


    ######start of actual code

    #your assembly code for strlen here
    
    #rax always holds the return value, in the case of strlen, it returns the 
    #length of the string, this is returning 0 just as a placeholder 
    movq $0, %rax
my_strlen_loop:
    cmpb $0, (%rdi)
    je my_strlen_end
    incq %rax
    incq %rdi
    jmp my_strlen_loop
    ######end of code

my_strlen_end:
    #we had the prologue at the beginning, now we have the epilogue, which is the
    #opposite: we will restore the registers to the way there were when someone
    #called us

    #before returning, we must restore the callee save registers, in opposite
    #order as they were pushed, because this is a stack (first in, last out)
    popq %r13
    popq %r12
    popq %rbp
    ret
    

#other string functions and their code

my_memset:
    pushq %rbp
    movq %rsp, %rbp
    pushq %r12
    pushq %r13
    movq $0, %rax
my_memset_loop:
    cmpq $0, %rdx
    je my_memset_end
    movb %sil, (%rdi)
    incq %rdi
    decq %rdx
    jmp my_memset_loop
my_memset_end:
    popq %r13
    popq %r12
    popq %rbp
    ret

my_strcat:
    pushq %rbp
    movq %rsp, %rbp
    pushq %r12
    pushq %r13
    movq %rdi, %rax
my_strcat_loop_1:
    cmpb $0, (%rdi)
    je my_strcat_loop_2
    incq %rdi
    jmp my_strcat_loop_1
my_strcat_loop_2:
    movb (%rsi), %r12b
    movb %r12b, (%rdi)
    cmpb $0, %r12b
    je my_strcat_end
    incq %rdi
    incq %rsi
    jmp my_strcat_loop_2
my_strcat_end:
    popq %r13
    popq %r12
    popq %rbp
    ret

my_strncpy:
    pushq %rbp
    movq %rsp, %rbp
    pushq %r12
    pushq %r13
    movq %rdi, %rax
my_strncpy_loop_1:
    cmpq $0, %rdx
    je my_strncpy_end
    decq %rdx
    movb (%rsi), %r12b
    movb %r12b, (%rdi)
    incq %rdi
    incq %rsi
    cmpb $0, %r12b
    je my_strncpy_loop_2
    jmp my_strncpy_loop_1
my_strncpy_loop_2:
    cmpq $0, %rdx
    je my_strncpy_end
    movb $0, (%rdi)
    incq %rdi
    decq %rdx
    jmp my_strncpy_loop_2
my_strncpy_end:
    popq %r13
    popq %r12
    popq %rbp
    ret

my_strcspn:
    pushq %rbp
    movq %rsp, %rbp
    pushq %r12
    pushq %r13
    movq $0, %rax
my_strcspn_loop_1:
    cmpb $0, (%rdi)
    je my_strcspn_end
    movb (%rdi), %r13b
    movq %rsi, %r12
my_strcspn_loop_2:
    cmpb $0, (%r12)
    je my_strcspn_else
    cmpb %r13b, (%r12)
    je my_strcspn_end
    incq %r12
    jmp my_strcspn_loop_2
my_strcspn_else:
    incq %rax
    incq %rdi
    jmp my_strcspn_loop_1
my_strcspn_end:
    popq %r13
    popq %r12
    popq %rbp
    ret

