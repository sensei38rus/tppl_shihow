import sys
import os


class Type:
    IDENT = "IDENT"
    KEYWORD = "KEYWORD"
    INT = "INT"
    FLOAT = "FLOAT"
    STRING = "STRING"
    OP = "OP"
    SEP = "SEP"
    UNDEF = "UNDEF"


class Lexical(Exception):
     def __init__(self, message, line, col):
        super().__init__(message)
        self.message = message
        self.line = line
        self.col = col


def is_keyword(word: str) -> bool:
    keywords = ["if", "for", "def", "while", "else", "return"]
    return word in keywords


def is_operator(word: str) -> bool:
    operators = "+ - * / = < > == <= >="
    return word in operators


def is_sep(word: str) -> bool:
    seps = "( ) { } , ;"
    return word in seps


def is_float(word: str) -> bool:
    try:
        float(word)
        return True
    except ValueError:
        return False


def is_int(word: str) -> bool:
    try:
        int(word)
        return True
    except ValueError:
        return False


def is_string(word: str) -> bool:
    return word.startswith("\"") and word.endswith("\"")


def is_ident(word: str) -> bool:
    if word[0].isdigit():              # не должна начинаться с цифры
        return False
    return all(c.isalnum() or c == '_' for c in word)


def define(word: str) -> str:
    if is_keyword(word):
        return Type.KEYWORD
    elif is_operator(word):
        return Type.OP
    elif is_sep(word):
        return Type.SEP
    elif "." in word and is_float(word):
        return Type.FLOAT
    elif is_int(word):
        return Type.INT
    elif is_string(word):
        return Type.STRING
    elif is_ident(word):
        return Type.IDENT
    else:
        return Type.UNDEF


def tokenizer(text: str) -> list:
    res = []
    for i, line in enumerate(text.splitlines()):
        word = ""
        for j, chr_ in enumerate(line):
            if chr_ == "#":
                break
            if chr_.isspace() and word.startswith("\"") and not word.endswith("\""):
                word += chr_
            elif chr_.isspace():
                if word:
                    what = define(word)
                    if what == Type.UNDEF:
                        raise Lexical(f"unexpected token {word!r}", i+1, j-len(word)+1)
                    
                    res.append(f"({what}, {word}, {i+1}:{j - len(word) + 1})")
                    word = ""
            else:
                word += chr_
        if word:
            what = define(word)
            if what == Type.UNDEF:
                raise Lexical(f"unexpected token {word!r}", i+1, len(line) - len(word)+1)
            res.append(f"({what}, {word}, {i+1}:{len(line) - len(word) + 1})")
    return res


def main():
    args = sys.argv
    if len(args) < 2:
        print("No argument was passed", file=sys.stderr)
        sys.exit(1)
    path = args[1]
    if not os.path.exists(path):
        print("No such file", file=sys.stderr)
        sys.exit(1)
    with open(path, "r") as f:
        text = f.read()
    try:
        res = tokenizer(text)
    except Lexical as e:
        print(f"{path}:{e.line}:{e.col}: lexical: {e.message}", file=sys.stderr)
        sys.exit(1)
    for line in res:
        print(line)

if __name__ == "__main__":
    main()