import pytest

from main import (
    is_keyword, is_operator, is_sep, is_float, is_int,
    is_string, is_ident, define, tokenizer,
    Type, Lexical,
)


def test_is_keyword():
    keywords = ["if", "for", "def", "while", "else", "return"]
    for keyword in keywords:
        assert is_keyword(keyword)
    not_keyword = "some"
    assert not is_keyword(not_keyword)


def test_define_keyword():
    res = define("for")
    assert res == Type.KEYWORD


def test_tokenizer_keyword():
    text = "if"
    res = tokenizer(text)
    assert res == ["(KEYWORD, if, 1:1)"]


def test_is_operator():
    assert is_operator("+")
    assert not is_operator("d")


def test_define_operator():
    res = define("==")
    assert res == Type.OP


def test_tokenizer_operator():
    text = "+"
    res = tokenizer(text)
    assert res == ["(OP, +, 1:1)"]


def test_is_sep():
    assert is_sep("(")
    assert not is_sep("+")


def test_define_sep():
    res = define(";")
    assert res == Type.SEP


def test_tokenizer_sep():
    res = tokenizer(";")
    assert res == ["(SEP, ;, 1:1)"]


def test_is_float():
    assert is_float("3.14")
    assert not is_float("vasya")


def test_define_float():
    res = define("2.28")
    assert res == Type.FLOAT


def test_tokenizer_float():
    res = tokenizer("12.2")
    assert res == ["(FLOAT, 12.2, 1:1)"]


def test_is_int():
    assert is_int("10")
    assert not is_int("vasya")


def test_define_int():
    res = define("38")
    assert res == Type.INT


def test_tokenizer_int():
    res = tokenizer("10")
    assert res == ["(INT, 10, 1:1)"]


def test_is_string():
    assert is_string("\"vasya\"")
    assert not is_string("some")


def test_define_string():
    res = define("\"some\"")
    assert res == Type.STRING


def test_tokenizer_string():
    res = tokenizer("\"some text\"")
    assert res == ["(STRING, \"some text\", 1:1)"]


def test_is_ident():
    assert is_ident("some")
    assert not is_ident("1some")
    assert not is_ident("s$me")


def test_define_ident():
    res = define("word")
    assert res == Type.IDENT

def test_tokenizer_ident():
    res = tokenizer("var")
    assert res == ["(IDENT, var, 1:1)"]

def test_tokenizer_invalid():
    with pytest.raises(Lexical):
        tokenizer("invalid t@xt")
