import sys

non_printable_ascii = {
    0: "[NUL]",
    1: "[SOH]",
    2: "[STX]",
    3: "[ETX]",
    4: "[EOT]",
    5: "[ENQ]",
    6: "[ACK]",
    7: "[BEL]",
    8: "[BS]",
    9: "[HT]",
    10: "[LF]",
    11: "[VT]",
    12: "[FF]",
    13: "[CR]",
    14: "[SO]",
    15: "[SI]",
    16: "[DLE]",
    17: "[DC1]",
    18: "[DC2]",
    19: "[DC3]",
    20: "[DC4]",
    21: "[NAK]",
    22: "[SYN]",
    23: "[ETB]",
    24: "[CAN]",
    25: "[EM]",
    26: "[SUB]",
    27: "[ESC]",
    28: "[FS]",
    29: "[GS]",
    30: "[RS]",
    31: "[US]",
    32: "[SP]",
    127: "[DEL]"
}


def get_print_item(type, values):
    printable_value = " ".join(str(x) for x in values)
    return f"<item uuid=\"{type}\" valid=\"yes\" auto=\"\"><arg>{printable_value}</arg><title>{printable_value}</title><subtitle>{type}</subtitle></item>\n"


def dec2fun(fun, *args):
    try:
        return fun(*args)
    except:
        return "ERROR"


def convert(values, fun, *args):
    decs = []
    hexs = []
    bins = []
    asciis = []

    for value in values:
        dec = fun(value, *args)
        decs.append(dec)
        hexs.append(dec2fun(format, dec, '02x'))
        bins.append(dec2fun(format, dec, 'b'))
        a = non_printable_ascii.get(dec)
        if a is None:
            a = dec2fun(chr, dec)
        asciis.append(a)

    string = ""

    string += get_print_item("decimal", decs)
    string += get_print_item("hexadecimal", hexs)
    string += get_print_item("binary", bins)
    string += get_print_item("ascii", asciis)

    return string


if __name__ == "__main__":
    option = sys.argv[1]
    input = sys.argv[2]

    string = ""
    if option == 'h':  # hexadecimal input
        string = convert(input.split(), int, 16)
    elif option == 'd':  # decimal input
        string = convert(input.split(), int)
    elif option == 'b':  # binary input
        string = convert(input.split(), int, 2)
    elif option == 'a':  # ascii input
        string = convert(list(input), ord)

    print("<items>\n" + string + "</items>")

