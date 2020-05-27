numInWords = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
              6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
              11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
              15: 'quarter', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
              19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two',
              23: 'twenty three', 24: 'twenty four', 25: 'twenty five',
              26: 'twenty six', 27: 'twenty seven', 28: 'twenty eight',
              29: 'twenty nine', 30: 'half', 0: 'clock'}
h = int(input())
m = int(input())
if 1 <= m <= 30:
    prefix = m
    suffix = h
    if m == 1:
        middle = "minute past"
    elif m == 15 or m == 30:
        middle = "past"
    else:
        middle = "minutes past"
elif 30 < m < 60:
    prefix = 60 - m
    suffix = h + 1
    if prefix == 1:
        middle = "minute to"
    elif prefix == 15:
        middle = "to"
    else:
        middle = "minutes to"
elif m == 0:
    prefix = h
    middle = "o'"
    suffix = 0

print(str(numInWords[prefix]) + " " + str(middle) + " " + str(numInWords[suffix]))


