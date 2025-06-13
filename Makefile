CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -Iinclude
TARGET = bin/lc3vm
SRC = src/lc3.c
OBJ = build/lc3.o
ASM = python3 assembler/assembler.py

all: bin build $(TARGET)

bin:
	@mkdir -p bin

build:
	@mkdir -p build

build/lc3.o: src/lc3.c
	$(CC) $(CFLAGS) -c $< -o $@

$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) -o $@ $^

test/hello.obj: test/hello.asm
	$(ASM) $< $@

run: $(TARGET) test/hello.obj
	./$(TARGET) test/hello.obj

clean:
	rm -rf build/*.o bin/lc3vm test/*.obj

.PHONY: all clean run bin build
