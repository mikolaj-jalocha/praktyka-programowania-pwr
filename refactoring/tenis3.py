class TennisGame3:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.p1_n = player1_name
        self.p2_n = player2_name
        self.p1 = 0
        self.p2 = 0

    # zmieniono nazwe parametru funkcji won_point z "n"
    def won_point(self, player_name):
        if player_name == "player1":
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self):
        if self.p1 == self.p2:
            return (
                self.SCORE_NAMES[self.p1] + "-All"
                if self.p1 < 3
                else "Deuce"
            )

        if self.p1 >= 4 or self.p2 >= 4:
            better_player = self.p1_n if self.p1 > self.p2 else self.p2_n
            diff = self.p1 - self.p2

            if abs(diff) == 1:
                return "Advantage " + better_player
            return "Win for " + better_player

        return f"{self.SCORE_NAMES[self.p1]}-{self.SCORE_NAMES[self.p2]}"

    def score2(self):
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if self.p1 == self.p2:
                return "Deuce"
            s = self.p1_n if self.p1 > self.p2 else self.p2_n
            return (
                "Advantage " + s
                if ((self.p1 - self.p2) * (self.p1 - self.p2) == 1)
                else "Win for " + s
            )
