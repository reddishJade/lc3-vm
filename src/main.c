int main(int argc, const char* argv[])
{
    @{Load Arguments}
    @{Setup}

    reg[R_COND] = FL_ZRO; // Initialize condition flags to zero

    enum { PC_START = 0x3000 }; // Starting address for the program
    reg[R_PC] = PC_START; // Set the program counter to the starting address

    int running = 1;
    while (running)
    {
        /* FETCH */
        uint16_t instr = memory[reg[R_PC]++]; // Fetch the instruction at the current PC and increment PC
        uint16_t op = instr >> 12; // Extract the opcode

        switch (op)
        {
            case OP_ADD:
                @{ADD}
                break;
            case OP_AND:
                @{AND}
                break;
            case OP_NOT:
                @{NOT}
                break;
            case OP_BR:
                @{BR}
                break;
            case OP_JMP:
                @{JMP}
                break;
            case OP_JSR:
                @{JSR}
                break;
            case OP_LD:
                @{LD}
                break;
            case OP_LDI:
                @{LDI}
                break;
            case OP_LDR:
                @{LDR}
                break;
            case OP_LEA:
                @{LEA}
                break;
            case OP_ST:
                @{ST}
                break;
            case OP_STI:
                @{STI}
                break;
            case OP_STR:
                @{STR}
                break;
            case OP_TRAP:
                @{TRAP}
                break;
            case OP_RES:
            case OP_RTI:
            default:
                @{BAD OPCODE}
                break;
        }
    }
}