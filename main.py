import random
 
def even(groups):
    # If any of our values are not within 1
    # of any other value, this test fails.
    for g0 in groups:
        for g1 in groups:
            if abs(g0-g1) > 1:
                return False
    return True
 
def distribution(total, size):
    groups = []
 
    while total >= size:
        total -= size
        groups.append(size)
 
    if total:
        groups.append(total)
 
    group = 0
    count = len(groups)
 
    # Start from the beginning of our allotted group
    # counts and steal one player from each group as
    # we move toward our target balance.
    while not even(groups):
        groups[-1] += 1
        groups[group] -= 1
 
        # If we're about to examine our last group,
        # stop and jump back to the beginning.
        if group >= count:
            group = 0
        else:
            group += 1
 
    # Should look like this when invoked
    # with f(4, 50):
    #   [3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3]
    return groups
 
def find_groups(players, size):
    attempt = 0
    attempts = 100
 
    total = len(players)
 
    while attempt < attempts:
        random.shuffle(players)
 
        offset = 0
        groups = []
 
        for i in distribution(total, size):
            members = players[offset:offset+i]
            games = find_games(members)
 
            if games:
                groups.append({
                    'members': members,
                    'games': games
                })
            else:
                attempt += 1
                break
 
            offset += i
 
        if offset == total:
            return groups
 
    raise Exception("Exhausted attempts")
 
def find_games(players):
    games = {}
 
    for player in players:
        for game in player.games:
            games[game] = games.get(game, 0) + 1
 
    return [game for game, count in games.items() if count >= len(players)]
 
class Player:
    def __init__(self, name=None, games=None):
        self.name = name
        self.games = games
 
    def __str__(self):
        return self.name
 
    def __repr__(self):
        return self.name
 
player0 = Player("Jason", ["dota2", "diablo3", "dungeondef", "wowtcg", "avalon", "titanquest", "firefly"])
player1 = Player("Yoni", ["csgo", "dota2", "payday2", "l4d2", "killingfloor", "dungeondef", "ut3", "wowtcg", "avalon", "titanquest", "bf3", "firefly", "nmrih", "brink", "tl2", "orion2"])
player2 = Player("Paul", ["csgo", "payday2", "l4d2", "killingfloor", "starcraft", "diablo3", "dungeondefenders", "ut3", "wowtcg", "avalon", "titanquest", "bf3", "firefly", "nmrih", "brink", "orion2", "CAH"])
player3 = Player("Arieh", ["csgo", "dota2", "payday2", "killingfloor", "starcraft", "ut3", "wowtcg", "bang", "avalon", "bf3", "firefly", "orion2"])
player4 = Player("Pat", ["payday2", "l4d2", "killingfloor", "starcraft", "wowtcg", "avalon", "firefly", "nmrih", "orion2"])
player5 = Player("John", ["csgo", "dota2", "l4d2", "killingfloor", "starcraft", "dungeondef", "ut3", "wowtcg", "bang", "avalon", "bf3", "firefly", "nmrih", "brink", "CAH"])
player6 = Player("Payton", ["csgo", "dota2", "payday2", "l4d2", "killingfloor", "starcraft", "dungeondef", "ut3", "wowtcg", "avalon", "firefly", "bf3", "nmrih", "orion2", "CAH"])
player7 = Player("Justin", ["csgo", "payday2", "l4d2", "killingfloor", "starcraft", "dungeondef", "ut3", "wowtcg", "bang", "avalon", "bf3", "firefly", "nmrih", "orion2", "CAH"])
player8 = Player("Cody", ["l4d2", "killingfloor"])
player9 = Player("Corey", ["dota2", "diablo3", "dungeondef", "wowtcg", "avalon", "titanquest", "firefly"])
 
players = [player0, player1, player2, player3, player4, player5, player6, player7, player8, player9]
 
for group in find_groups(players, 4):
    print group['members']
    print group['games']
    print
