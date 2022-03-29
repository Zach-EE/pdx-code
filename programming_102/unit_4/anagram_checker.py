def anagram_check(string_1, string_2):
    # Converters and sorts string i/p by user into a sorted list of characters
    list_1 = list(string_1)
    list_2 = list(string_2)
    list_1.sort(reverse=True)
    list_2.sort(reverse=True)

    if len(string_1) != len(string_2):
        return False

    elif list_1 == list_2:
        return True

    else:
        return False


def main():
    string_1 = input('Enter the first word: ').lower().strip()
    string_2 = input('Enter the second word: ').lower().strip()

    if anagram_check(string_1, string_2):
        print(f"'{ string_1 }' and '{ string_2 }' ARE anagrams of eachother!!!")

    else:
        print(f"'{ string_1 }' and '{ string_2 }' are NOT anagrams of eachother!!!")


main()
