import sys
data = sys.stdin.readlines()
for s in range(len(data)):
    for l in range(len(data[s])):
        if '='  ==data[s][l]: print("-", end="")
        if '-'  ==data[s][l]: print("0", end="")
        if '0'  ==data[s][l]: print("9", end="")
        if '9'  ==data[s][l]: print("8", end="")
        if '8'  ==data[s][l]: print("7", end="")
        if '7'  ==data[s][l]: print("6", end="")
        if '6'  ==data[s][l]: print("5", end="")
        if '5'  ==data[s][l]: print("4", end="")
        if '4'  ==data[s][l]: print("3", end="")
        if '3'  ==data[s][l]: print("2", end="")
        if '2'  ==data[s][l]: print("1", end="")
        if '1'  ==data[s][l]: print("`", end="")
        
        if '\\' ==data[s][l]: print("]", end="")
        if ']'  ==data[s][l]: print("[", end="")
        if '['  ==data[s][l]: print("P", end="")
        if 'P'  ==data[s][l]: print("O", end="")
        if 'O'  ==data[s][l]: print("I", end="")
        if 'I'  ==data[s][l]: print("U", end="")
        if 'U'  ==data[s][l]: print("Y", end="")
        if 'Y'  ==data[s][l]: print("T", end="")
        if 'T'  ==data[s][l]: print("R", end="")
        if 'R'  ==data[s][l]: print("E", end="")
        if 'E'  ==data[s][l]: print("W", end="")
        if 'W'  ==data[s][l]: print("Q", end="")
        
        if "'"  ==data[s][l]: print(";", end="")
        if ';'  ==data[s][l]: print("L", end="")
        if 'L'  ==data[s][l]: print("K", end="")
        if 'K'  ==data[s][l]: print("J", end="")
        if 'J'  ==data[s][l]: print("H", end="")
        if 'H'  ==data[s][l]: print("G", end="")
        if 'G'  ==data[s][l]: print("F", end="")
        if 'F'  ==data[s][l]: print("D", end="")
        if 'D'  ==data[s][l]: print("S", end="")
        if 'S'  ==data[s][l]: print("A", end="")
        
        if '/'  ==data[s][l]: print(".", end="")
        if '.'  ==data[s][l]: print(",", end="")
        if ','  ==data[s][l]: print("M", end="")
        if 'M'  ==data[s][l]: print("N", end="")
        if 'N'  ==data[s][l]: print("B", end="")
        if 'B'  ==data[s][l]: print("V", end="")
        if 'V'  ==data[s][l]: print("C", end="")
        if 'C'  ==data[s][l]: print("X", end="")
        if 'X'  ==data[s][l]: print("Z", end="")
        
        if ' '  ==data[s][l]: print(" ", end="")
        if '\n'  ==data[s][l]: print("\n", end="")
