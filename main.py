


def count_characters(text:list) -> dict[str:int]:
    corrected = " ".join(text)
    return {letter:corrected.count(letter) for letter in corrected}

def create_dicts(text:list):
    characters = count_characters(text=text)
    character_list = []
    for letter,count in characters.items():
        character_list.append({"letter":letter, "count":count})
    return sorted(character_list, key=lambda x: x["count"], reverse=True)
    

def main(book_path:str):
    with open(book_path) as f:
        file_contents = f.read()
        split_file = file_contents.lower().split()
        count = len(split_file)
        count_char = create_dicts(split_file)

        print(f"--- Begin report of {book_path} ---")
        print(f"{count} words found in document")
        for item in count_char:
            print(f"The '{item.get('letter')}' character was found {item.get('count')} times.")
        print("--- End of Report ---")
        

if __name__ == "__main__":
    book_path = "books/frankenstein.txt"
    main(book_path)
