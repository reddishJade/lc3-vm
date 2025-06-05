.ORIG x3000           ; Start the program at x3000
LEA R0, HELLO_STR    ; Load the address of HELLO_STR into R0
PUTS                 ; Output the string pointed to by R0
HALT                 ; Halt the program

HELLO_STR .STRINGZ "Hello, LC-3!\n" ; Store the string in memory
.END                 ; End of the program
