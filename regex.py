from itertools import zip_longest


def regex_matcher_only_dot(inp: str, regex: str) -> bool:
    for i, pat in zip_longest(inp, regex):
        if not i or not pat or pat != "." and i != pat:
            return False
    return True


def regex_matcher(inp: str, regex: str) -> bool:
    i, j = 0, 0


if __name__ == "__main__":
    assert regex_matcher_only_dot("ray", "ra.") is True
    assert regex_matcher_only_dot("raymond", "ra.") is False
    assert regex_matcher("chat", ".*at") is True
    assert regex_matcher("chats", ".*at") is False
