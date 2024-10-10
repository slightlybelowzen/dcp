def count_losses(matches: list[list[int]]) -> list[list[int]]:
    losers = set()
    lost_once = set()
    players = set()
    for match in matches:
        winner, loser = match
        players.add(winner)
        players.add(loser)
        if loser not in lost_once and loser not in losers:
            lost_once.add(loser)
        elif loser in lost_once:
            losers.add(loser)
            lost_once.remove(loser)
    return [list(sorted(players - losers - lost_once)), list(sorted(lost_once))]


if __name__ == "__main__":
    assert count_losses(
        [
            [1, 3],
            [2, 3],
            [3, 6],
            [5, 6],
            [5, 7],
            [4, 5],
            [4, 8],
            [4, 9],
            [10, 4],
            [10, 9],
        ]
    ) == [[1, 2, 10], [4, 5, 7, 8]]
    assert count_losses([[2, 3], [1, 3], [5, 4], [6, 4]]) == [[1, 2, 5, 6], []]
    assert count_losses(
        [[1, 5], [2, 5], [2, 8], [2, 9], [3, 8], [4, 7], [4, 9], [5, 7], [6, 8]]
    ) == [[1, 2, 3, 4, 6], []]
