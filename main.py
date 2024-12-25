import tkinter
from typing import List
from typing import Any
import math
from tkinter import *
import time
import threading

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

def copy_type(selected, gui_instance) -> None:
    gui_instance.update_top("What type of paper are you using? ")
    while len(selected) < 4:
        return

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

def copy_sides(selected, gui_instance) -> None:
    gui_instance.update_top("Will it be twosided? [y or n] ")
    while len(selected) > 4:
        return
    match selected[3]:
        case "y" | "yes":
            selected[3]: "t"
            gui_instance.update_bottom("You have choosen: Two Sided")
        case "n" | "no":
            selected[3]: "f"
            gui_instance.update_bottom("You have choosen: One Sided")
        case _:
            selected[3]: "f"
            gui_instance.update_bottom("You have choosen: One Sided")
    return copy_type(selected, gui_instance)

def copy_color_select(selected, gui_instance) -> None:
    copies_color: str = input("Color? [y or n] ")
    copies_color_lower: str = copies_color.lower()
    if copies_color.lower() == "y" or copies_color.lower() == "yes":
        color = True
        return copy_sides(csize, color)
    else:
        color = False
        return copy_sides(csize, color)
    gui_instance.update_top("Does it have color? [y or n] ")
    while len(selected) > 2:
        return
    match selected[2]:
        case "y" | "yes":
            selected[2]: "t"
            gui_instance.update_bottom("You have choosen: Color")
        case "n" | "no":
            selected[2]: "f"
            gui_instance.update_bottom("You have choosen: No Color")
        case _:
            selected[2]: "f"
            gui_instance.update_bottom("You have choosen: No Color")
    return copy_sides(selected, gui_instance)
# Returns: csize
def copy_size_select(selected, gui_instance) -> None:
    gui_instance.update_top("What's the size? ")
    while len(selected) > 2:
        return
    match selected[1]:
        case "8" | "8.5x11" | "8511" | "lt":
            selected[1]: "8511"
            gui_instance.update_bottom("You have choosen: 8.5x11")
        case "14" | "8.5x14" | "8514" | "lg":
            selected[1]: "8514"
            gui_instance.update_bottom("You have choosen: 8.5x14")
        case "17" | "11x17" | "1117":
            selected[1]: "1117"
            gui_instance.update_bottom("You have choosen: 11x17")
        case "12" | "12x18" | "1218":
            selected[1]: '1218'
            gui_instance.update_bottom('You have choosen: 12x18')
        case _:
            gui_instance.update_bottom("Error! Restarting...")
            return gui_instance.restart()
    return copy_color_select(selected, gui_instance)


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

def total(rprice, gui_instance, selected) -> None:
    tax: float = 1.115
    total_taxed: float = rprice * tax
    gui_instance.update_top(f'Your price: ${rprice:.2f}\nYour taxed price: ${total_taxed:.2f}')
    gui_instance.update_bottom(f'Click Restart')
    while len(selected) < 6:  # Loops until selected updates, extending its index by 1 using get_input()
        return
    return menu()

def rotulo_price(selected, pie_cuadrado, rcolumn, gui_instance) -> None:
    rprice = None
    match selected[1]:
        case "b":
            rprice: float = pie_cuadrado * banner_price[rcolumn]
        case "d":
            rprice: float = pie_cuadrado * dboard_price[rcolumn]
        case "v":
            rprice: float = pie_cuadrado * vynil_price[rcolumn]
        case "p18":
            rprice: float = pie_cuadrado * pvc18_price[rcolumn]
        case "p14":
            rprice: float = pie_cuadrado * pvc14_price[rcolumn]
        case "p12":
            rprice: float = pie_cuadrado * pvc12_price[rcolumn]
        case "p":
            rprice: float = pie_cuadrado * poster_price[rcolumn]
        case "vyc":
            rprice: float = pie_cuadrado * vynil_corte_price
    return total(rprice, gui_instance, selected)

# Selected[1] = Type
def rotulo_type_selection(selected, gui_instance) -> None:
    gui_instance.update_top("What type of sign?:")
    while len(selected) < 2:
        return
    match selected[1]:
        case "b" | "banner" | "bnr":
            selected[1] = "b"
            gui_instance.update_bottom(f'You have choosen: Banner')
        case "d" | "dboard" | "db":
            selected[1] = "d"
            gui_instance.update_bottom(f'You have choosen: Dboard')
        case "v" | "vy" | "vynil":
            selected[1] = "v"
            gui_instance.update_bottom(f'You have choosen: Vynil')
        case "pvc18" | "18" | "p18":
            selected[1] = "p18"
            gui_instance.update_bottom(f'You have choosen: PVC 1/8')
        case "pvc14" | "14" | "p14":
            selected[1] = "p14"
            gui_instance.update_bottom(f'You have choosen: PVC 1/4')
        case "pvc12" | "12" | "p12":
            selected[1] = "p12"
            gui_instance.update_bottom(f'You have choosen: PVC 1/2')
        case "p" | "poster" | "pos":
            selected[1] = "p"
            gui_instance.update_bottom(f'You have choosen: Poster')
        case _:
            gui_instance.update_bottom("Error when choosing your desired type\nRestarting Program")
            selected.clear()
            return gui_instance.restart()
    return rotulo_size_selection(selected, gui_instance)

# Selected[4] = Discount
def rotulo_discount(selected, gui_instance) -> float:
    # This input is Selected[5]
    gui_instance.update_top("Do you want a discount?\nC for Church\nD for Dealer\nN for No Discount\nSelection: ")
    while len(selected) < 5:
        return

    match selected[4]:
        case "c" | "church":
            selected[4] = "c"
        case "d" | "dealer":
            selected[4] = "d"
        case _:
            selected[4] = "n"
    return rotulo_pc(selected, gui_instance)

def rotulo_pc(selected, gui_instance) -> None:
    pie_cuadrado = float(selected[2]) * float(selected[3])
    pie_cuadrado = pie_cuadrado / 144
    pie_cuadrado = math.ceil(pie_cuadrado * 10) / 10.0

    if selected[4] == "c":
        rcolumn = -2
        return rotulo_price(selected, pie_cuadrado, rcolumn, gui_instance)

    elif selected[4] == "d":
        rcolumn = -1
        return rotulo_price(selected, pie_cuadrado, rcolumn, gui_instance)

    else:
        if pie_cuadrado >= 0 and pie_cuadrado <= 15:
            rcolumn = 0
        elif pie_cuadrado >= 16 and pie_cuadrado <= 31:
            rcolumn = 1
        elif pie_cuadrado >= 32 and pie_cuadrado <= 59:
            rcolumn = 2
        elif pie_cuadrado >= 60:
            rcolumn = 3
        else:
            gui_instance.update_bottom("ERROR - Please use appropiate numbers in Size Selection")
    return rotulo_price(selected, pie_cuadrado, rcolumn, gui_instance)

# Selected[2] x Selected[3] = Pie Cuadrado
def rotulo_size_selection(selected, gui_instance) -> None:
    print(f'This is the inputs transfered from rotulo_type: {selected}')
    gui_instance.update_top("What's the first measurement?")
    while len(selected) < 3: # Loops until selected updates, extending its index by 1 using get_input()
        return
    try:
        if float(selected[2]):
            gui_instance.update_bottom(f'Size selected: {selected[2]} x ...')
    except ValueError:
        gui_instance.update_bottom(f'You must type a size in numbers')
        return gui_instance.restart()

    gui_instance.update_top("What's the second measurement?")
    while len(selected) < 4: # Loops until selected updates, extending its index by 1 using get_input()
        return

    try:
        if float(selected[3]):
            gui_instance.update_bottom(f'Size selected: {selected[2]} x {selected[3]}')
    except ValueError:
        gui_instance.update_bottom(f'You must type a size in numbers')
        return gui_instance.restart()

    return rotulo_discount(selected, gui_instance)

# ------------------------------------------|
# Start of Everything
def menu(selected, gui_instance) -> None:
    gui_instance.update_top("Please enter your estimation type")
    gui_instance.update_bottom("Write your awnser in the entrybox and Press Enter to confirm")

    match selected[0]:
        case "fy"| "f" | "flyers":
            gui_instance.update_bottom("You have selected: Flyers")
            return

        case "r" | "rotulo":
            gui_instance.update_bottom("You have selected: Rotulos")
            return rotulo_type_selection(selected, gui_instance)

        case "b" | "business cards" | "bc":
            gui_instance.update_bottom("You have selected: Rotulos")

        case "copy" | "c":
            gui_instance.update_bottom("You have selected: Copies")
            return copy_size_select(selected, gui_instance)

        case "ale" | "alejandra":
            selected.clear()
            gui_instance.update_bottom("You're not funny, Ale...\nI'm restarting this shit")

        case _:
            selected.clear()
            gui_instance.update_bottom("Error, Please notify Baethal if you get this message")

# --------------------------------------------------------
#                  APPLICATION MODULES
# --------------------------------------------------------
class GUI:

    def __init__(self):
        self.root = Tk()
        self.root.resizable(False, False)

        self.root.title('Estimation Calculator')


        self.main_canvas = tkinter.Canvas(master=self.root, background="snow3", width=400, height=300)
        self.main_canvas.pack()

        self.logo_image = tkinter.PhotoImage(master=self.main_canvas, file="Logo EZ Impress.png")
        self.title_label = tkinter.Label(master=self.main_canvas, image=self.logo_image, height=200, width=450, background="snow3")
        self.title_label.pack()

        self.text_top = tkinter.Label(master=self.main_canvas, background="snow3", text="Select your quick estimation type: ",
                             font=('Consolas', 15), width=50, height=10, wraplength=400)
        self.text_top.pack(pady=5,padx=20)

        self.text_bot = tkinter.Label(master=self.main_canvas, background="snow3", text="Write your awnser in the entrybox and Press Enter to confirm",
                             font=('Consolas', 15), width=50, height=10, wraplength=400)
        self.text_bot.pack(pady=5, padx=20)

        self.entry_line = tkinter.Entry(master=self.main_canvas, background="snow3", width=50)
        self.entry_line.bind("<Return>", self.get_input)
        self.entry_line.pack(pady=2, padx=20)

        self.button_1 = tkinter.Button(master=self.main_canvas, text=" Restart ", font=('Consolas', 15), bg="white", anchor="w",
                              command=self.restart)
        self.button_1.pack(padx=20, pady=3)

        self.selected = []
        self.root.mainloop()

    def restart(self):
        self.selected.clear()
        self.update_top("Select your quick estimation type:")
        return self.get_input(self)

    def get_input(self, event) -> None:
        if self.entry_line.get() == "":
          return

        self.selected.append(self.entry_line.get().lower().strip())
        if self.selected:
            print(f'{self.selected}')
        self.entry_line.delete(0, tkinter.END)
        return menu(self.selected, self)

    def update_bottom(self, bottom) -> None:
        self.bottom = bottom
        self.text_bot.config(text=f'{self.bottom}')

    def update_top(self, top) -> None:
        self.top = top
        self.text_top.config(text=f'{self.top}')


# ------------------------------------------|
def main() -> None:
    GUI()

if __name__ == '__main__':
    main()