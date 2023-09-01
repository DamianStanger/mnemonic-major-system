import argparse
import itertools


numberToCharMap = {
    1: ['l'],
    2: ['n'],
    3: ['m'],
    4: ['r'],
    5: ['f', 'v'],
    6: ['b', 'p'],
    7: ['d', 't'],
    8: ['ch', 'sh', 'j'],
    9: ['g', 'q', 'k'],
    0: ['z', 's']
}

def main(stringToConvert, numberToConvert):
    print(f'The result is: {convertStringToNumber(stringToConvert)} or {numberToConvert}')

def convertStringToNumber(stringToConvert):
    removedDuplicateLetters = ''.join(char for char, _ in itertools.groupby(stringToConvert))

    result = ""
    for letter in removedDuplicateLetters:
        for number, letters in numberToCharMap.items():
            if letter in letters:
                result += str(number)
    return result

def convertNumberToString(numberToConvert):
    return str(numberToConvert)


if __name__ == '__main__':
    # get a string from the arguments passed to the script
    # if no arguments are passed, use the default string
    # use the package to get the arguments and generate help text

    parser = argparse.ArgumentParser("Convert a number to a string, or a string to a number")
    parser.add_argument('-n', '--number')
    parser.add_argument('-s', '--string')
    args = parser.parse_args()

    main(args.string, args.number)
