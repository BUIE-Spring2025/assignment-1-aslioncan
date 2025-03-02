def int_to_roman(num):
    if num >= 4000:
        return "Number cannot be greater than 4000!"

    roman_binler = ""
    roman_yüzler = ""
    roman_onlar = ""
    roman_birler = ""
# elif num<4000:

    bin_decimal = num // 1000  # bu mesela 2 demek
    roman_binler = "M" * bin_decimal
    binden_kalan = num % 1000  # 2437 için mesela 437  kısmı demek bu binden_kalan

    yüz_decimal = binden_kalan // 100  # 2437 için bin_decimal 2 demek, binden_kalan 437 demek, yüz decimal 4 demek yüzden kalan 37 demek vs.
    if yüz_decimal <= 3:
        roman_yüzler = "C" * yüz_decimal
    elif yüz_decimal == 4:
        roman_yüzler = "CD"
    elif 5 <= yüz_decimal < 9:
        roman_yüzler = "D" + "C" * (yüz_decimal - 5)
    elif yüz_decimal == 9:
        roman_yüzler = "CM"
    yüzden_kalan = binden_kalan % 100  # 2437 için mesela bu 37 demek bu yüzden_kalan
    on_decimal = yüzden_kalan // 10
    if on_decimal <= 3:
        roman_onlar = "X" * on_decimal
    elif on_decimal == 4:
        roman_onlar = "XL"
    elif 5 <= on_decimal < 9:
        roman_onlar = "L" + "X" * (on_decimal - 5)
    elif on_decimal == 9:
        roman_onlar = "XC" 
    bir_decimal = yüzden_kalan % 10
    if bir_decimal <= 3:
        roman_birler = "I" * bir_decimal
    elif bir_decimal == 4:
        roman_birler = "IV"
    elif 5 <= bir_decimal < 9:
        roman_birler = "V" + "I" * (bir_decimal - 5)
    elif bir_decimal == 9:
        roman_birler = "IX"

    return roman_binler + roman_yüzler + roman_onlar + roman_birler


print(int_to_roman(2437))  # MMCDXXXVII
print(int_to_roman(3999))  # MMMCMXCIX
print(int_to_roman(4))  # IV
print(int_to_roman(4000))




    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
