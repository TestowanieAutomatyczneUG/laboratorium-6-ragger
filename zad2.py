

def roman(num):
    arabic = [1000, 900, 500, 400, 100, 90, 50,  40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman = ''
    i = 0
    while num > 0:
        for _ in range(num // arabic[i]):
            roman += syb[i]
            num -= arabic[i]
        i += 1
    return roman


