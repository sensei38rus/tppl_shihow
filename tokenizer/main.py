from enum import Enum
import re

keywords = ["if","else","while","return","def","for"]


class Type(Enum):
    KEYWORD = "KEYWORD",
    IDENT = "IDENT",
    INT = "INT",
    FLOAT = "FLOAT",
    STRING = "STRING",
    OP = "OP",
    SEP = "SEP"



def process_type(obj: str) -> Type:
    if keywords.count(obj) > 0:
        return Type.KEYWORD


def tokenizer(input: str):


    for i, line in enumerate(input.splitlines()):
        for j, word in enumerate(re.split(r'(\s+)',line)):
            if word == " ":
                continue
            type = process_type(word).name
            print(f"({type}, {word}, {i}:{j})")





def main():
    with open("test.txt") as file:
        input = file.read()
    tokenizer(input)
   

if __name__ == "__main__":                                                      # pragma: no cover
    main()                                                                      # pragma: no cover
