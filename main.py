def main(): 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        report = get_report(file_contents)
        print(report)
        
    
def get_wordcount(text):
    word_list = text.split()
    return len(word_list)

def get_charcount(text):
   letter_dict = {}
   lowered_text = text.lower()
   for char in lowered_text:
      letter_dict[char] = letter_dict.get(char, 0) + 1
   return letter_dict

def get_report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{get_wordcount(text)} words found in the document")
    print("")
    charcount = get_charcount(text)
    char_list = []
   
    for char, count in charcount.items():
        if char.isalpha():
            char_list.append({"character": char, "num": count})     

    char_list.sort(reverse=True, key=sort_on)  
    for char in char_list:
        print(f"The '{char["character"]}' character was found {char["num"]} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]
   
main()