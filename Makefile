CC = gcc
CFLAGS = -Wall -Wextra -std=c99
TARGET = lc3vm
ASM = python3 assembler.py

all: $(TARGET)

$(TARGET): lc3.c
	$(CC) $(CFLAGS) -o $@ $<

hello.obj: hello.asm
	$(ASM) $< $@

run: $(TARGET) hello.obj
	./$(TARGET) hello.obj

clean:
	rm -f $(TARGET) *.o *.obj

.PHONY: all clean run
