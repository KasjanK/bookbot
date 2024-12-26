def main(): 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        wordcount = get_wordcount(file_contents)
        print(wordcount)
    
def get_wordcount(text):
    word_list = text.split()
    return len(word_list)

main()