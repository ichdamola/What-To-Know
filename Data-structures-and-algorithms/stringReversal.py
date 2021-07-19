def string_reversal(str_):
    if len(str_) == 0:
        return ""

    statement = str_.split(' ')
    reversed_statement = statement[::-1]

    return " ".join(reversed_statement)

if __name__ == "__main__":
    assert string_reversal("This is the best") == "best the is This", "Failed test case."