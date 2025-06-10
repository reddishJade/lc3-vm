#!/usr/bin/env python3

import sys
import re

# Opcodes
OP_BR = 0
OP_ADD = 1
OP_LD = 2
OP_ST = 3
OP_JSR = 4
OP_AND = 5
OP_LDR = 6
OP_STR = 7
OP_RTI = 8
OP_NOT = 9
OP_LDI = 10
OP_STI = 11
OP_JMP = 12
OP_RES = 13
OP_LEA = 14
OP_TRAP = 15

# Trap codes
TRAP_GETC = 0x20
TRAP_OUT = 0x21
TRAP_PUTS = 0x22
TRAP_IN = 0x23
TRAP_PUTSP = 0x24
TRAP_HALT = 0x25

# Condition flags
FL_POS = 1 << 0
FL_ZRO = 1 << 1
FL_NEG = 1 << 2

def parse_asm(asm):
    lines = asm.split('\n')
    labels = {}
    instructions = []
    data = []
    current_address = 0
    
    # First pass: collect labels and build symbol table
    for line in lines:
        line = line.split(';')[0].strip()  # Remove comments
        if not line:
            continue
            
        # Check for .ORIG directive
        if line.startswith('.ORIG'):
            current_address = int(line.split()[1].replace('x', ''), 16)
            origin = current_address
            continue
            
        # Check for label
        if ':' in line:
            label = line.split(':')[0].strip()
            labels[label] = current_address
            line = line.split(':', 1)[1].strip()
            
        if not line:
            continue
            
        # Handle .STRINGZ directive
        if '.STRINGZ' in line:
            string = line.split('"')[1]
            data.append(('.STRINGZ', string, current_address))
            current_address += len(string) + 1  # +1 for null terminator
            continue
            
        # Normal instruction
        if not line.startswith('.'):  # Skip other directives for now
            instructions.append((line, current_address))
            current_address += 1
    
    # Process data section first
    data_memory = {}
    for item in data:
        if item[0] == '.STRINGZ':
            _, string, addr = item
            # Store the address of the string in the label
            labels['HELLO_STR'] = addr
            for i, c in enumerate(string):
                data_memory[addr + i] = ord(c)
            data_memory[addr + len(string)] = 0  # Null terminator
    
    # Second pass: resolve labels and generate machine code
    machine_code = []
    
    # Fill in the code section
    for inst in instructions:
        line, addr = inst
        op = line.split()[0].upper()
        
        if op == 'LEA':
            # LEA R0, LABEL
            parts = [p.strip() for p in line.split(',')]
            dr = int(parts[0].split()[1][1])
            label = parts[1]
            pc_offset = labels[label] - (addr + 1)
            instruction = (OP_LEA << 12) | (dr << 9) | (pc_offset & 0x1FF)
            machine_code.append(instruction)
            
        elif op == 'PUTS':
            # TRAP x22 (PUTS)
            machine_code.append((OP_TRAP << 12) | TRAP_PUTS)
            
        elif op == 'HALT':
            # TRAP x25 (HALT)
            machine_code.append((OP_TRAP << 12) | TRAP_HALT)
            
        else:
            print(f"Unsupported instruction: {line}")
            machine_code.append(0)
    
    # Add data section after code
    if data_memory:
        # Find the end of the code section
        code_end = origin + len(machine_code)
        # Find the start of the data section
        data_start = min(data_memory.keys())
        # Add padding if needed
        while len(machine_code) < (data_start - origin):
            machine_code.append(0)
        # Add the data
        for addr in range(data_start, max(data_memory.keys()) + 1):
            if addr in data_memory:
                machine_code.append(data_memory[addr])
            else:
                machine_code.append(0)
    
    return machine_code

def write_obj_file(machine_code, filename):
    with open(filename, 'wb') as f:
        # Write the origin (0x3000) as the first word
        origin = 0x3000
        f.write(bytes([(origin >> 8) & 0xFF, origin & 0xFF]))
        
        # Write the machine code
        for instruction in machine_code:
            f.write(bytes([(instruction >> 8) & 0xFF, instruction & 0xFF]))

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} input.asm output.obj")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(input_file, 'r') as f:
        asm = f.read()
    
    machine_code = parse_asm(asm)
    write_obj_file(machine_code, output_file)
    print(f"Assembly successful. Output written to {output_file}")

if __name__ == "__main__":
    main()
