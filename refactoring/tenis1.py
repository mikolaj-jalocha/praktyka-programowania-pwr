class TennisGame1:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    # nazwy score_names są teraz wyekstraktowane jako zmienna klasy
    # kod relatywnie dlugiej metody scores zostal podzielony na dwie mniejsze
    # uproszczono kalkulację wyniku

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1points += 1
        else:
            self.p2points += 1

    def _equal_score(self, points):
        if points < 3:
            return self.SCORE_NAMES[points] + "-All"
        return "Deuce"

    def _end_game_score(self, p1, p2):
        advantage = "Advantage "
        win_for = "Win for "
        difference = p1 - p2

        if difference == -1:
            return advantage + "player2"
        if difference == 1:
            return advantage + "player1"
        if difference >= 2:
            return win_for + "player1"

        return win_for + "player2"

    def score(self):
        p1, p2 = self.p1points, self.p2points

        if p1 == p2:
            return self._equal_score(p1)
        if p1 >= 4 or p2 >= 4:
            return self._end_game_score(p1, p2)

        return f"{self.SCORE_NAMES[p1]}-{self.SCORE_NAMES[p2]}"

    def scor2e(self):
        result = ""
        temp_score = 0
        if self.p1points == self.p2points:
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.p1points, "Deuce")
        elif self.p1points >= 4 or self.p2points >= 4:
            minus_result = self.p1points - self.p2points
            if minus_result == 1:
                result = "Advantage player1"
            elif minus_result == -1:
                result = "Advantage player2"
            elif minus_result >= 2:
                result = "Win for player1"
            else:
                result = "Win for player2"
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.p1points
                else:
                    result += "-"
                    temp_score = self.p2points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[temp_score]
        return result


