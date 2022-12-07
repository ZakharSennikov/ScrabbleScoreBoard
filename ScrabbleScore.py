# Zakhar Sennikov
from ScrabblePlayer import Player


def clear():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')


def print_scores(li):
    for player in range(len(li)):
        print(f"name: {li[player].get_name()}{' ' * (13 - len(li[player].get_name()))}", end='|')
    print()
    for index in range(len(li[0].get_li()[0])):
        for player in range(len(li)):
            print(f"{li[player].get_li()[0][index]}: {li[player].get_li()[1][index]}",
                  ' ' * (16 - len(li[player].get_li()[0][index]) - len(str(li[player].get_li()[1][index]))), end='|')
        print()


def find_value(word):
    letters = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3,
               'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 8, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
    score = 0
    multiplier = 1
    try:
        count = 0
        for index, letter in enumerate(word):
            if letter == '(' or letter == ')':
                multiplier = 3
                continue
            elif letter == '[' or letter == ']':
                multiplier = 2
                continue
            elif letter == '':
                return 0
            if letter == '3':
                score += 2 * letters[word[index + 1]]
            elif letter == '2':
                score += letters[word[index + 1]]
            else:
                score += letters[letter]
            count += 1
        if count >= 7:
            return [word, score * multiplier + 50]
        return [word, score * multiplier]
    except IndexError:
        print("Not a real word")
        word = input("what is your new word? ")
        word, value = find_value(word)
        return [word, value]
    except ValueError:
        print("Not a real word")
        word = input("what is your new word? ")
        word, value = find_value(word)
        return [word, value]
    except KeyError:
        print("Not a real word")
        word = input("what is your new word? ")
        word, value = find_value(word)
        return [word, value]


def change_word(word):
    if'(' in word or '[' in word or ')' in word or ']' in word or '2' in word or '3' in word:
        new_word = ''
        for letter in word:
            if '(' == letter or '[' == letter or ')' == letter or ']' == letter or '2' == letter or '3' == letter:
                pass
            else:
                new_word += letter
        return new_word
    return word


def main():
    player_list = []
    count = int(input("How many players will be playing? "))
    for num in range(count):
        name = input(f"Please put in name for player {num + 1}: ")
        player_list.append(Player(name))
    while True:
        clear()
        print_scores(player_list)
        for num in range(count):
            word = input(f'{player_list[num].get_name()}, what is your word? ')
            word, score = find_value(word.lower())
            word = change_word(word)
            if score == 0:
                player_list[num].add_word("skip", score)
            else:
                player_list[num].add_word(word, score)


if __name__ == "__main__":
    main()
