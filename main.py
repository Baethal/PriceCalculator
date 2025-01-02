from typing import List
from typing import Any
import math

# import curses
# stdscr = curses.initscr()

# LEYEND:
# LT  = 8.5x11
# TAB = 11x17
# ARC = 12x17
# LG = 8.5x14

# M = MATTE
# G = GLOSS
# HL = HILO

# DATABASE              0      1     2     3      4     5     6        7
LT_blk_24: List[float] = [0.35, 0.25, 0.17, 0.10, 0.09, 0.07, 0.06]
LT_blk_67_M: List[float] = [0.65, 0.55, 0.45, 0.40, 0.35, 0.30, 0.25]
LT_blk_24_HL: List[float] = [0.55, 0.55, 0.45, 0.40, 0.30, 0.25, 0.20]

LT_color_24: List[float] = [0.70, 0.45, 0.35, 0.30, 0.28, 0.23, 0.22, 0.17]
LT_color_67_M: List[float] = [0.90, 0.80, 0.70, 0.65, 0.60, 0.55, 0.40, 0.35]
LT_color_24_HL: List[float] = [0.90, 0.80, 0.70, 0.65, 0.60, 0.55, 0.40, 0.35]
LT_color_100_G: List[float] = [1.20, 1.10, 0.90, 0.80, 0.70, 0.65, 0.55, 0.50]
LT_color_100_T: List[float] = [1.10, 1.00, 0.85, 0.75, 0.65, 0.60, 0.50, 0.45]
LT_color_Bumper: List[float] = [1.75, 1.65, 1.60, 1.55, 1.50, 1.40, 1.25, 1.15]

LG_blk: List[float] = [0.45, 0.25, 0.22, 0.20, 0.18, 0.16, 0.15]
LG_color: List[float] = [0.85, 0.70, 0.50, 0.40, 0.35, 0.27, 0.25]

TAB_blk_24: List[float] = [0.70, 0.50, 0.34, 0.20, 0.18, 0.14, 0.12]
TAB_blk_67_M: List[float] = [1.30, 1.10, 0.90, 0.80, 0.70, 0.60, 0.50]
TAB_blk_24_HL: List[float] = [1.30, 1.10, 0.90, 0.80, 0.70, 0.60, 0.50]

TAB_color_24: List[float] = [1.40, 0.90, 0.70, 0.60, 0.56, 0.46, 0.44, 0.34]
TAB_color_67_M: List[float] = [1.80, 1.60, 1.40, 1.30, 1.20, 1.10, 0.80, 0.70]
TAB_color_24_HL: List[float] = [1.80, 1.60, 1.40, 1.30, 1.20, 1.10, 0.80, 0.70]
TAB_color_Bumper: List[float] = [3.40, 3.30, 3.20, 3.10, 3.00, 2.80, 2.50, 2.30]

ARC_color_100_G: List[float] = [2.40, 2.20, 1.80, 1.60, 1.40, 1.30, 1.10, 1.00]
ARC_color_100_T: List[float] = [2.20, 2.00, 1.70, 1.50, 1.30, 1.20, 1.00, 0.95]
ARC_color_Thermatac: List[float] = [3.75, 3.50, 3.25, 3.00, 2.75, 2.50, 2.25, 2.15]
ARC_color_Pearl: List[float] = [4.00, 3.00, 2.70, 2.60, 2.40, 2.20, 2.00, 1.90]
ARC_color_120: List[float] = [2.80, 2.60, 2.40, 2.20, 2.00, 1.70, 1.50, 1.30]
ARC_color_Synap: List[float] = [7.00, 6.00, 5.50, 4.00, 3.75, 3.65, 3.65, 3.65]
ARC_color_100_HLC: List[float] = [2.20, 2.00, 1.70, 1.50, 1.30, 1.20, 1.00, 0.90]

def copy_price(csize: str, ctype: str, cquantity:int, ccolumn: int) -> None:
    match csize:
        case "8511":
            match ctype:
                # LT 24
                case "ntt":
                    cprice: float = float(cquantity) * (LT_color_24[ccolumn] + LT_color_24[ccolumn])
                    return total(cprice)
                case "ntf":
                    cprice: float = float(cquantity) * LT_color_24[ccolumn]
                    return total(cprice)
                case "nft":
                    cprice: float = float(cquantity) * (LT_blk_24[ccolumn] + LT_blk_24[ccolumn])
                    return total(cprice)
                case "nff":
                    cprice: float = float(cquantity) * LT_blk_24[ccolumn]
                    return total(cprice)
                # LT 67
                case "mtt":
                    cprice: float = float(cquantity) * (LT_color_67_M[ccolumn] + LT_color_24[ccolumn])
                    return total(cprice)
                case "mtf":
                    cprice: float = float(cquantity) * LT_color_67_M[ccolumn]
                    return total(cprice)
                case "mft":
                    cprice: float = float(cquantity) * (LT_blk_67_M[ccolumn] + LT_blk_24[ccolumn])
                    return total(cprice)
                case "mff":
                    cprice: float = float(cquantity) * LT_color_67_M[ccolumn]
                    return total(cprice)
                # LT HL
                case "hltt":
                    cprice: float = float(cquantity) * (LT_color_24_HL[ccolumn] + LT_color_24[ccolumn])
                    return total(cprice)
                case "hltf":
                    cprice: float = float(cquantity) * LT_color_24_HL[ccolumn]
                    return total(cprice)
                case "hlft":
                    cprice: float = float(cquantity) * (LT_blk_24_HL[ccolumn] + LT_blk_24[ccolumn])
                    return total(cprice)
                case "hlff":
                    cprice: float = float(cquantity) * LT_blk_24_HL[ccolumn]
                    return total(cprice)

                # LT 100G
                case "gtf" | "gff":
                    cprice: float = float(cquantity) * LT_color_100_G[ccolumn]
                    return total(cprice)
                case "gft" | "gtt":
                    cprice: float = float(cquantity) * (LT_color_100_G[ccolumn] + LT_color_24[ccolumn])
                    return total(cprice)
                # LT 100T
                case "ttf" | "tff":
                    cprice: float = float(cquantity) * LT_color_100_T[ccolumn]
                    return total(cprice)
                case "tft" | "ttt":
                    cprice: float = float(cquantity) * (LT_color_100_T[ccolumn] + LT_color_24[ccolumn])
                    return total(cprice)
                # LT Bumpper
                case "btf":
                    cprice: float = float(cquantity) * LT_color_Bumper[ccolumn]
                    return total(cprice)

        case "8411":
            match ctype:
                case "ntt":
                    cprice: float = float(cquantity) * (LG_color[ccolumn] + LG_color[ccolumn])
                    return total(cprice)
                case "ntf":
                    cprice: float = float(cquantity) * LG_color[ccolumn]
                    return total(cprice)
                case "nft":
                    cprice: float = float(cquantity) * (LG_blk[ccolumn] + LG_blk[ccolumn])
                    return total(cprice)
                case "nff":
                    cprice: float = float(cquantity) * LG_blk[ccolumn]
                    return total(cprice)

        case "1117":
            match ctype:
                # 11x17 Normal
                case "ntt":
                    cprice: float = float(cquantity) * (TAB_color_24[ccolumn] + TAB_color_24[ccolumn])
                    return total(cprice)
                case "ntf":
                    cprice: float = float(cquantity) * TAB_color_24[ccolumn]
                    return total(cprice)
                case "nft":
                    cprice: float = float(cquantity) * (TAB_blk_24[ccolumn] + TAB_blk_24[ccolumn])
                    return total(cprice)
                case "nff":
                    cprice: float = float(cquantity) * TAB_blk_24[ccolumn]
                    return total(cprice)
                # 11x17 Matte
                case "mtt":
                    cprice: float = float(cquantity) * (TAB_color_24[ccolumn] + TAB_color_67_M[ccolumn])
                    return total(cprice)
                case "mtf":
                    cprice: float = float(cquantity) * TAB_color_67_M[ccolumn]
                    return total(cprice)
                case "mft":
                    cprice: float = float(cquantity) * (TAB_blk_67_M[ccolumn] + TAB_blk_24[ccolumn])
                    return total(cprice)
                case "mff":
                    cprice: float = float(cquantity) * TAB_color_67_M[ccolumn]
                    return total(cprice)
                # LT HL
                case "hltt":
                    cprice: float = float(cquantity) * (TAB_color_24_HL[ccolumn] + TAB_color_24[ccolumn])
                    return total(cprice)
                case "hltf":
                    cprice: float = float(cquantity) * TAB_color_24_HL[ccolumn]
                    return total(cprice)
                case "hlft":
                    cprice: float = float(cquantity) * (TAB_blk_24_HL[ccolumn] + TAB_blk_24[ccolumn])
                    return total(cprice)
                case "hlff":
                    cprice: float = float(cquantity) * TAB_blk_24_HL[ccolumn]
                    return total(cprice)

                # 11x17 100G
                case "gtf" | "gff":
                    cprice: float = float(cquantity) * ARC_color_100_G[ccolumn]
                    return total(cprice)
                case "gft" | "gtt":
                    cprice: float = float(cquantity) * (ARC_color_100_G[ccolumn] + TAB_color_24[ccolumn])
                    return total(cprice)
                # 11x17 100T
                case "ttf" | "tff":
                    cprice: float = float(cquantity) * ARC_color_100_T[ccolumn]
                    return total(cprice)
                case "tft" | "ttt":
                    cprice: float = float(cquantity) * (ARC_color_100_T[ccolumn] + TAB_color_24[ccolumn])
                    return total(cprice)
                # 11x17 Bumpper
                case "btf":
                    cprice: float = float(cquantity) * TAB_color_Bumper[ccolumn]
                    return total(cprice)

                # 11x17 HLC
                case "hltt":
                    cprice: float = float(cquantity) * (ARC_color_100_HLC[ccolumn] + TAB_color_24[ccolumn])
                    return total(cprice)

                case "hltf":
                    cprice: float = float(cquantity) * ARC_color_100_HLC[ccolumn]
                    return total(cprice)

        case "1218":
            match ctype:
                # 12x18 100G
                case "gtf" | "gff":
                    cprice: float = float(cquantity) * ARC_color_100_G[ccolumn]
                    return total(cprice)
                case "gft" | "gtt":
                    cprice: float = float(cquantity) * (ARC_color_100_G[ccolumn] + TAB_color_24[ccolumn])
                    return total(cprice)
                # 12x18 100T
                case "ttf" | "tff":
                    cprice: float = float(cquantity) * ARC_color_100_T[ccolumn]
                    return total(cprice)
                case "tft" | "ttt":
                    cprice: float = float(cquantity) * (ARC_color_100_T[ccolumn] + TAB_color_24[ccolumn])
                    return total(cprice)
                # 12x18 Thermatac
                case "thtf":
                    cprice: float = float(cquantity) * ARC_color_Thermatac[ccolumn]
                    return total(cprice)
                # 12x18 Synap
                case "stf":
                    cprice: float = float(cquantity) * ARC_color_Synap[ccolumn]
                    return total(cprice)
                case "stt":
                    cprice: float = float(cquantity) * (ARC_color_Synap[ccolumn] + TAB_color_24[ccolumn])
                    return total(cprice)
                # 12x18 120 Gloss
                case "120tt":
                    cprice: float = float(cquantity) * (ARC_color_Pearl[ccolumn] + TAB_color_24[ccolumn])
                    return total(cprice)
                case "120tf":
                    cprice: float = float(cquantity) * ARC_color_120[ccolumn]
                    return total(cprice)
                # 12x18 Pearlado
                case "ptt":
                    cprice: float = float(cquantity) * (ARC_color_Pearl[ccolumn] + TAB_color_24[ccolumn])
                    return total(cprice)
                case "ptf":
                    cprice: float = float(cquantity) * ARC_color_Pearl[ccolumn]
                    return total(cprice)
                # 12x18 HL Cover
                case "hltt":
                    cprice: float = float(cquantity) * (ARC_color_100_HLC[ccolumn] + TAB_color_24[ccolumn])
                    return total(cprice)

                case "hltf":
                    cprice: float = float(cquantity) * ARC_color_100_HLC[ccolumn]
                    return total(cprice)

def copy_calculation(csize: str, color: bool, ctype: str, cquantity: int, church: bool) -> None:

    if color:
        if church:
            ccolumn = 5
            return copy_price(csize, ctype, cquantity, ccolumn)

        if 0 <= cquantity <= 4:
            ccolumn = 0
            return copy_price(csize, ctype, cquantity, ccolumn)
        if 5 <= cquantity < 10:
            ccolumn = 1
            return copy_price(csize, ctype, cquantity, ccolumn)
        if 10 <= cquantity < 25:
            ccolumn = 2
            return copy_price(csize, ctype, cquantity, ccolumn)
        if 25 <= cquantity <= 50:
            ccolumn = 3
            return copy_price(csize, ctype, cquantity, ccolumn)
        if 51 <= cquantity <= 250:
            ccolumn = 4
            return copy_price(csize, ctype, cquantity, ccolumn)
        if 251 <= cquantity <= 1000:
            ccolumn = 5
            return copy_price(csize, ctype, cquantity, ccolumn)
        if 1001 <= cquantity <= 2000:
            ccolumn = 6
            return copy_price(csize, ctype, cquantity, ccolumn)
        else:
            ccolumn = 7
            return copy_price(csize, ctype, cquantity, ccolumn)

    else:
        if church:
            ccolumn = 4
            return copy_price(csize, ctype, cquantity, ccolumn)

        if 0 <= cquantity <= 1:
            ccolumn = 0
            return copy_price(csize, ctype, cquantity, ccolumn)
        if 2 <= cquantity < 5:
            ccolumn = 1
            return copy_price(csize, ctype, cquantity, ccolumn)
        if 5 <= cquantity < 50:
            ccolumn = 2
            return copy_price(csize, ctype, cquantity, ccolumn)
        if 51 <= cquantity < 250:
            ccolumn = 3
            return copy_price(csize, ctype, cquantity, ccolumn)
        if 250 <= cquantity < 1000:
            ccolumn = 4
            return copy_price(csize, ctype, cquantity, ccolumn)
        if 1000 <= cquantity < 2000:
            ccolumn = 5
            return copy_price(csize, ctype, cquantity, ccolumn)
        else:
            ccolumn = 6
            return copy_price(csize, ctype, cquantity, ccolumn)

def copy_type(csize: str, color: bool, twosides: bool) -> None:
    ctype: str = input("What type of paper are you using? ")
    ctype_low = ctype.lower()
    ctype_error = "Your paper size is unavailable for this type of paper\nRestarting Type Selection..."

    # Checking for "n" or "normal"
    if ctype_low == "n" or ctype_low == "normal":
        if color and twosides:
            ctype = "ntt"
        elif color and not twosides:
            ctype = "ntf"
        elif not color and twosides:
            ctype = "nft"
        else:
            ctype = "nff"
        return copy_quantity_church(csize, ctype, color)

    # Checking for "m" or "matte"
    elif ctype_low == "m" or ctype_low == "matte":
        if csize != "8511" and csize != "1117":
            print(f'{ctype_error}')
            return copy_type(csize, color, twosides)
        else:
            if color and twosides:
                ctype = "mtt"
                return copy_quantity_church(csize, ctype, color)
            elif color and not twosides:
                ctype = "mtf"
                return copy_quantity_church(csize, ctype, color)
            elif not color and twosides:
                ctype = "mft"
                return copy_quantity_church(csize, ctype, color)
            else:
                ctype = "mff"
                return copy_quantity_church(csize, ctype, color)

    # Checking for "g" or "gloss" or "glossy"
    elif ctype_low == "g" or ctype_low == "gloss" or ctype_low == "glossy":
        if csize == "8514":
            print(f'{ctype_error}')
            return copy_type(csize, color, twosides)
        else:
            if color and twosides:
                ctype = "gtt"
            elif color and not twosides:
                ctype = "gtf"
            elif not color and twosides:
                ctype = "gft"
            else:
                ctype = "gff"
            return copy_quantity_church(csize, ctype, color)

    # Checking for "t" or "texto"
    elif ctype_low == "t" or ctype_low == "texto":
        if csize == "8514":
            print(f"{ctype_error}")
            return copy_type(csize, color, twosides)
        else:
            if color and twosides:
                ctype = "ttt"
            elif color and not twosides:
                ctype = "ttf"
            elif not color and twosides:
                ctype = "tft"
            else:
                ctype = "tff"
            return copy_quantity_church(csize, ctype, color)

    # Checking for "th" or "thermatac" or "therma"
    elif ctype_low == "th" or ctype_low == "thermatac" or ctype_low == "therma":
        if csize != "1218":
            print(f"{ctype_error}")
            return copy_type(csize, color, twosides)
        else:
            if color and twosides:
                print(f"{ctype_error}")
                return copy_type(csize, color, twosides)
            elif color and not twosides:
                ctype = "thtf"
                return copy_quantity_church(csize, ctype, color)
            else:
                print(f"{ctype_error}")
                return copy_type(csize, color, twosides)

    # Checking for "b" or "bumper" or "bumpersticker"
    elif ctype_low == "b" or ctype_low == "bumper" or ctype_low == "bumpersticker":
        if csize != "8511" and csize != "1117":
            print(f'You cannot have 2sided bumperstickers')
            return copy_type(csize, color, twosides)
        else:
            if color and twosides:
                print(f'{ctype_error}')
                return copy_type(csize, color, twosides)
            elif color and not twosides:
                ctype = "btf"
                return copy_quantity_church(csize, ctype, color)
            else:
                print(f'{ctype_error}')
                return copy_type(csize, color, twosides)

    # Checking for "s" or "synap"
    elif ctype_low == "s" or ctype_low == "synap":
        if csize == "1218":
            if color and twosides:
                ctype = "stt"
                return copy_quantity_church(csize, ctype, color)
            elif color and not twosides:
                ctype = "stf"
                return copy_quantity_church(csize, ctype, color)
            else:
                print(f'{ctype_error}')
                return copy_type(csize, color, twosides)
        else:
            print(f'{ctype_error}')
            return copy_type(csize, color, twosides)

    # Checking for "120" or "gloss 120" or "gloss120"
    elif ctype_low == "120" or ctype_low == "gloss 120" or ctype_low == "gloss120":
        if csize != "1218":
            print(f'{ctype_error}')
            return copy_type(csize, color, twosides)
        else:
            if color and twosides:
                ctype = "120tt"
                return copy_quantity_church(csize, ctype, color)
            elif color and not twosides:
                ctype = "120tf"
                return copy_quantity_church(csize, ctype, color)
            else:
                print(f'{ctype_error}')
                return copy_type(csize, color, twosides)

    # Checking for "p" or "pearlado" or "pearl"
    elif ctype_low == "p" or ctype_low == "pearlado" or ctype_low == "pearl":
        if csize != "8511" and csize != "1218":
            print(f'{ctype_error}')
            return copy_type(csize, color, twosides)
        else:
            if color and twosides:
                ctype = "ptt"
                return copy_quantity_church(csize, ctype, color)
            elif color and not twosides:
                ctype = "ptf"
                return copy_quantity_church(csize, ctype, color)
            else:
                print(f'{ctype_error}')
                return copy_type(csize, color, twosides)

    # Checking for "h" or "hilo"
    elif ctype_low == "h" or ctype_low == "hilo":
        if csize == "8514":
            print(f'{ctype_error}')
            return copy_type(csize, color, twosides)
        else:
            if color and twosides:
                ctype = "htt"
                return copy_quantity_church(csize, ctype, color)
            elif color and not twosides:
                ctype = "htf"
                return copy_quantity_church(csize, ctype, color)
            else:
                print(f'{ctype_error}')
                return copy_type(csize, color, twosides)

    # Checking for "hl" or "hilocover" or "hilo cover"
    elif ctype_low == "hl" or ctype_low == "hilocover" or ctype_low == "hilo cover":
        if csize == "8514" or csize == "8511":
            print(f'{ctype_error}')
            return copy_type(csize, color, twosides)
        else:
            if color and twosides:
                ctype = "hltt"
                return copy_quantity_church(csize, ctype, color)
            elif color and not twosides:
                ctype = "hltf"
                return copy_quantity_church(csize, ctype, color)
            else:
                print(f'{ctype_error}')
                return copy_type(csize, color, twosides)

    else:
        print("Invalid paper type selected")
        return copy_type(csize, color, twosides)

def copy_quantity_church(csize: str, ctype: str, color: bool) -> None:
    cquantity: int = int(input('How many? '))
    copies_church: str = input("Does it have Church Discount? [y or n] ")

    if copies_church == "y":
        church = True
        return copy_calculation(csize, color, ctype, cquantity, church)

    else:
        church = False
        return copy_calculation(csize, color, ctype, cquantity, church)

def copy_sides(csize: str, color: bool) -> None:
    twosides: str = input("2 Sided? [y or n] ")
    twosides_low: str = twosides.lower()
    if twosides_low == "y" or twosides_low == "yes":
        twosides = True
        return copy_type(csize, color, twosides)
    else:
        twosides = False
        return copy_type(csize, color, twosides)

def copy_color_select(csize: str) -> None:
    copies_color: str = input("Color? [y or n] ")
    copies_color_lower: str = copies_color.lower()
    if copies_color.lower() == "y" or copies_color.lower() == "yes":
        color = True
        return copy_sides(csize, color)
    else:
        color = False
        return copy_sides(csize, color)

# Returns: csize
def copy_size_select() -> None:
    csize: str = input("What's the size? ")
    csize_lower: str = csize.lower()
    if csize == "8" or csize == "8.5x11" or csize == "8511" or csize_lower == "lt":
        csize = "8511"
        print("You have choosen: 8.5x11")
        return copy_color_select(csize)

    elif csize == "14" or csize == "8.5x14" or csize == "8514" or csize_lower == "lg":
        csize = "8514"
        print("You have choosen: 8.5x14")
        return copy_color_select(csize)

    elif csize == "17" or csize == "11x17" or csize == "1117":
        csize = "1117"
        print("You have choosen: 11x17")
        return copy_color_select(csize)

    elif csize == "12" or csize == "12x18" or csize == "1218":
        csize = "1218"
        print('You have choosen: 12x18')
        return copy_color_select(csize)

    else:
        print("Error! Restarting...")
        return menu()


# |-----------------------------------------|
#                ROTULACION
# |-----------------------------------------|
# DATABASE                 0 [-6] 1 [-5] 2 [-4] 3 [-3] 4 [-2]  5 [-1]
# REFERENCE                        16+    32+   60+    CH   DEALER

banner_price: List[float] = [2.75, 2.50, 2.45, 2.40, 2.35, 2.25]
vynil_price: List[float] = [3.75, 3.50, 3.25, 3.00, 2.75, 2.25]
dboard_price: List[float] = [4.25, 4.10, 4.00, 3.75, 3.25, 2.95]
pvc18_price: List[float] = [5.75, 5.50, 5.25, 4.75, 4.25, 3.25]
pvc14_price: List[float] = [7.75, 7.50, 7.00, 6.75, 6.25, 5.00]
pvc12_price: List[float] = [8.75, 8.50, 8.00, 7.75, 7.25, 6.00]
poster_price: List[float] = [3.25, 3.10, 3.00, 2.75, 2.55, 2.25]
vynil_corte_price: float = 0.15

def total(self: float, quantity=1) -> None:
    tax: float = 1.115
    total: float = self
    total_taxed: float = total * tax
    print(f'-------------------------------')
    print(f'---->   *   RESULTS   *   <----')
    print(f'-------------------------------\n')
    print(f'Your price for each: ${self:.2f}')
    print(f'Your taxed price for each: ${total_taxed:.2f}\n')

    if quantity > 1:
        total: float = total * quantity
        total_taxed: float = total * tax
        print(f'Your total price for {quantity} is: ${total:.2f}')
        print(f'Your taxed price for {quantity} is: ${total_taxed:.2f}\n')
    restart()

def restart() -> None:
    restart = input("-> Press Enter to restart <-\n")
    print(f'\n\n')
    return main()

def rotulo_price(rtype: str, pie_cuadrado: float, rcolumn: int, quantity: float) -> None:
    match rtype:
        case "b":
            rprice: float = pie_cuadrado * banner_price[rcolumn]
            return total(rprice, quantity)
        case "d":
            rprice: float = pie_cuadrado * dboard_price[rcolumn]
            return total(rprice, quantity)
        case "v":
            rprice: float = pie_cuadrado * vynil_price[rcolumn]
            return total(rprice, quantity)
        case "p18":
            rprice: float = pie_cuadrado * pvc18_price[rcolumn]
            return total(rprice, quantity)
        case "p14":
            rprice: float = pie_cuadrado * pvc14_price[rcolumn]
            return total(rprice, quantity)
        case "p12":
            rprice: float = pie_cuadrado * pvc12_price[rcolumn]
            return total(rprice, quantity)
        case "p":
            rprice: float = pie_cuadrado * poster_price[rcolumn]
            return total(rprice, quantity)
        case "vyc":
            print(f'{pie_cuadrado}')
            rprice: float = pie_cuadrado * vynil_corte_price
            return total(rprice)

def rotulo_type_selection() -> None:
    rotulo: str = input(f"What type of sign?: ")
    rotulo_low: str = rotulo.lower()

    if rotulo_low == "b" or rotulo_low == "banner" or rotulo_low == "bnr":
        rtype: str = "b"
        return rotulo_size_selection(rtype)
    elif rotulo_low == "d" or rotulo_low == "dboard" or rotulo_low == "db":
        rtype: str = "d"
        return rotulo_size_selection(rtype)
    elif rotulo_low == "v" or rotulo_low == "vy" or rotulo_low == "vynil":
        rtype: str = "v"
        return rotulo_size_selection(rtype)
    elif rotulo_low == "pvc18" or rotulo_low == "p18" or rotulo_low == "18":
        rtype: str = "p18"
        return rotulo_size_selection(rtype)
    elif rotulo_low == "pvc14" or rotulo_low == "p14" or rotulo_low == "14":
        rtype: str = "p14"
        return rotulo_size_selection(rtype)
    elif rotulo_low == "pvc12" or rotulo_low == "p12" or rotulo_low == "12":
        rtype: str = "p12"
        return rotulo_size_selection(rtype)
    elif rotulo_low == "p" or rotulo_low == "poster" or rotulo_low == "pos":
        rtype: str = "p"
        return rotulo_size_selection(rtype)
    elif rotulo_low == "vyc" or rotulo_low == "vynil de corte" or rotulo_low == "vynilcorte":
        rtype: str = "vyc"
        return rotulo_size_selection(rtype)
    else:
        print("Error when choosing your desired sign. Restarting Program....")
        return main()

def rotulo_discount(rtype: str, pie_cuadrado: float) -> float:
  rdiscount: str = input("Do you want a discount?   C for Church   D for Dealer   N for No Discount\nSelection: ")
  rdiscount_lower: str = rdiscount.lower()


  if rdiscount_lower == "c" or rdiscount_lower == "church":
        rdiscount = "c"
        return rotulo_quantity(rtype, pie_cuadrado, rdiscount)

  elif rdiscount_lower == "d" or rdiscount_lower == "dealer":
        rdiscount = "d"
        return rotulo_quantity(rtype, pie_cuadrado, rdiscount)
  else:
        rdiscount = "n"
        return rotulo_quantity(rtype, pie_cuadrado, rdiscount)

def rotulo_quantity(rtype: str, pie_cuadrado: float, rdiscount: str) -> None:
    quantity: float = float(input("How many? "))
    return rotulo_pc(rtype, pie_cuadrado, rdiscount, quantity)


def rotulo_pc(rtype: str, pie_cuadrado: float, rdiscount: str, quantity: float) -> None:

    if rtype == "vyc":
        rcolumn = 0
        return rotulo_price(rtype, pie_cuadrado, rcolumn, quantity)

    pie_cuadrado = math.ceil(pie_cuadrado * 10) / 10.0
    total_cuadrado = quantity * pie_cuadrado

    if rdiscount == "c":
        rcolumn = -2
        return rotulo_price(rtype, pie_cuadrado, rcolumn, quantity)


    elif rdiscount == "d":
        rcolumn = -1
        return rotulo_price(rtype, pie_cuadrado, rcolumn, quantity)

    elif total_cuadrado >= 0 and total_cuadrado <= 15:
        rcolumn = 0
        return rotulo_price(rtype, pie_cuadrado, rcolumn, quantity)

    elif total_cuadrado >= 16 and total_cuadrado <= 31:
        rcolumn = 1
        return rotulo_price(rtype, pie_cuadrado, rcolumn, quantity)

    elif total_cuadrado >= 32 and total_cuadrado <= 59:
        rcolumn = 2
        return rotulo_price(rtype, pie_cuadrado, rcolumn, quantity)

    elif total_cuadrado >= 60:
        rcolumn = 3
        return rotulo_price(rtype, pie_cuadrado, rcolumn, quantity)

    else:
        print("ERROR - Please use appropiate numbers")
        return main()

def rotulo_size_selection(rtype: str) -> None:
    rsize_1: float = float(input(f"What's the first measurement? "))
    rsize_2: float = float(input(f"What's the second measurement? "))

    if rtype == "vcy":
        pie_cuadrado: float = rsize_1 * rsize_2
        return rotulo_discount(rtype, pie_cuadrado)

    else:
        rt: float = rsize_1 * rsize_2
        pie_cuadrado: float = rt / 144
        return rotulo_discount(rtype, pie_cuadrado)

# ------------------------------------------|
# Start of Everything
def menu() -> None:
    selected: str = input("|-----------------------------------------|\n"
                          "    EZIMPRESS AUTOMATIC ESTIMATION 5000\n"
                          "|-----------------------------------------|\n"
                          "Select your quick estimation type: ")
    if selected == "fy" or selected == "f":
        return print("You have choosen: Flyers")

    elif selected == "r" or selected == "rotulo":
        print("You have choosen: Rotulos ")
        rotulo_type_selection()
        return

    elif selected == "b" or selected == "bc" or selected == "business cards":
        return print("You have choosen: Business Cards")

    elif selected == "copy" or selected == "c":
        print("You have choosen: Copies")
        copy_size_select()
        return

    elif selected == "ale" or selected == "Ale" or selected == "Alejandra":
        print("You're not funny, Ale...\nI'm restarting this shit")
        return menu()
    else:
        print("Error! Restarting...")
        return menu()
# ------------------------------------------|

def main() -> None:
    menu()

if __name__ == "__main__":
    main()