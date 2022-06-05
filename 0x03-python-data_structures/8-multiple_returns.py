#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    char_1 = sentence[0]
    return (str_len, char_1 if str_len > 0 else None)
