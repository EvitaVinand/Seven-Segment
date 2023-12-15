def binary_to_SevenSegment(A):
    segment = []
    if A == 0:
        segment = [1, 1, 0, 1, 1, 1, 1]
    elif A == 1:
        segment = [0, 0, 0, 1, 0, 0, 1]
    elif A == 2:
        segment = [1, 0, 1, 1, 1, 0, 0]
    elif A == 3:
        segment = [1, 0, 1, 1, 0, 1, 1]
    elif A == 4:
        segment = [0, 1, 1, 1, 0, 0, 1]
    elif A == 5:
        segment = [1, 1, 1, 0, 0, 1, 1]
    elif A == 6:
        segment = [1, 1, 1, 0, 1, 1, 1]
    elif A == 7:
        segment = [1, 0, 0, 1, 0, 0, 1]
    elif A == 8:
        segment = [1, 1, 1, 1, 1, 1, 1]
    elif A == 9:
        segment = [1, 1, 1, 1, 0, 1, 1]

    return segment


def Draw_TruthTable(segment):
    print("#############################")
    print("[ a | b | c | d | e | f | g ]")
    print("_____________________________")
    print("[" + str(segment[0]) + " | " + str(segment[1]) + " | " + str(segment[2]) + " | " + str(
        segment[3]) + " | " + str(segment[4]) + " | " + str(segment[5]) + " | " + str(segment[6]) + "]")
    print("#############################")


def Seven_Segment_Display(Number):
    segment = {
        0: ['  _', '|  |','|  |', '  _'],
        1: [' ', '|', '|'],
        2: [' _', ' _|', '|_'],
        3: ['_', '_|', '_|'],
        4: [' ', '|_|', '  |'],
        5: [' _', '|_', ' _|'],
        6: [' _', '|_', '|_|'],
        7: [' _', '  |', '  |'],
        8: [' _', '|_|', '|_|'],
        9: [' _', '|_|', ' _|'],
    }

    return segment.get(A, [' ', ' ', ' '])

A = int(input("Masukkan angka di antara 0 sampai 9: "))
if 0 <= A <= 9:
    Segment = binary_to_SevenSegment(A)
    print(str(A) + " to Seven_Segment Representation in Table : ")
    Draw_TruthTable(Segment)
    print("Seven_Segment Display of " + str(A) + " : ")
    print('\n'.join(Seven_Segment_Display(A)))
    print()
else:
    print("Masukkan angka di antara 0 sampai 9 : ")
