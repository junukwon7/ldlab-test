import sys
import re

f = open(sys.argv[1], 'r')
content = f.readlines()
f.close()

instructions = re.findall(r'[01]{8}', content)

REG = [0] * 4
MEM = [ (i if i < 16 else 16 - i) for i in range(32)]
print(MEM)
disp = 0
pc = 0

if __name__ == '__main__':
    while True:
        instr = instructions[pc]
        print(f'[{pc}] instruction: {instr}')
        opcode = instr[0:2]
        rs = int(instr[2:4], 2)
        rt = int(instr[4:6], 2)
        rd_imm = int(instr[6:8], 2)

        if rd_imm > 1:
            rd_imm -= 2

        if opcode == '00':
            print(f' [ADD] REG[{REG[rs]}]({hex(REG[rs])}) + REG[{REG[rt]}]({hex(REG[rt])}) to REG[{rd_imm}]')
            res = REG[rs] + REG[rt]
            REG[rd_imm] = res
            disp = res
        elif opcode == '01':
            print(f' [SAVE] MEM[{REG[rs] + rd_imm}]({MEM[REG[rs] + rd_imm]}) to REG[{rt}]')
            res = MEM[REG[rs] + rd_imm]
            REG[rt] = res
            disp = res
        elif opcode == '10':
            print(f' [LOAD] REG[{rt}]({hex(REG[rt])}) to MEM[{REG[rs] + rd_imm}]')
            res = REG[rt]
            MEM[REG[rs] + rd_imm] = res
        elif opcode == '11':
            print(f' [JMP] IMM({rd_imm})')
            if rd_imm == -1:
                print(' End Of Instructions: Infinite loop')
                break
        
        for i, r in enumerate(REG):
            print(f'REG[{i}]({hex(r)})', end=' ')
        print(f'DISP({hex(disp)})', end=' ')

        print('\n')
        pc += 1

