# LC-3 Virtual Machine

A complete implementation of the LC-3 (Little Computer 3) virtual machine in C. This project includes both the VM and an assembler for converting LC-3 assembly code into executable object files.

## Features

- Full implementation of the LC-3 instruction set
- Memory-mapped I/O for keyboard input and display output
- Support for all LC-3 trap routines (GETC, OUT, PUTS, IN, PUTSP, HALT)
- Built-in assembler for compiling LC-3 assembly code
- Simple and clean codebase with clear separation of concerns

## Project Structure

```
lc3-vm/
├── assembler/         # LC-3 Assembler implementation
│   ├── assembler.py   # Python-based assembler script
│   └── README.md      # Assembler documentation
├── bin/               # Compiled binaries
│   └── lc3vm          # Main VM executable
├── build/             # Build artifacts
├── include/           # Header files
│   └── lc3.h          # LC-3 VM header
├── src/               # Source code
│   ├── lc3.c          # Main VM implementation
│   └── main.c         # Entry point
├── test/              # Test programs
│   ├── hello.asm      # Example assembly
│   ├── hello.s        # Assembled output
│   └── hello.obj      # Object file
├── Makefile           # Build configuration
├── README.md          # This file
├── LICENSE            # MIT License
└── lc3-vm.md          # Technical documentation
```

## Prerequisites

- GCC or Clang
- Python 3.x (for the assembler)
- Make

## Building

To build the VM:

```bash
make
```

This will compile the VM and place the executable in `bin/lc3vm`.

## Usage

### Running Programs

To run an LC-3 object file:

```bash
./bin/lc3vm test/hello.obj
```

### Assembling Programs

First, assemble your LC-3 assembly file:

```bash
python3 assembler/assembler.py test/hello.asm
```

This will generate a `.obj` file that can be run with the VM.

## Examples

The `test/` directory contains example programs:

- `hello.asm`: A simple "Hello, World!" program

## Documentation

For detailed information about the LC-3 architecture and instruction set, see [lc3-vm.md](lc3-vm.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
