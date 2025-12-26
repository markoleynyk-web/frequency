import sys

def main():
    text = read_file("text.txt")
    words = text.split()
    dict_count = count_words(words)
    sorted_list = sorted(dict_count.items(), key = lambda item: item[1], reverse=True)
    
    N = int(sys.argv[1])
    try:
        for i in range(N):
            word, count = sorted_list[i]
            print(f'{i + 1} - word "{word}" {count} times')
    except IndexError:
        print("The number entered is beyond the total words in the text file")


def read_file(file):
    with open(file, "r") as f:
        text = f.read()
    return text

def count_words(words):
    dict_count = {}
    for word in words:
        if word in dict_count:
            dict_count[word] += 1
        else:
            dict_count[word] = 1
    return dict_count

if __name__ == "__main__":
    main()