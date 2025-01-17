class Game:
    all =[]
    def __init__(self, title):
        self.title = title
        Game.all.append(self)   
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,title):
        if not hasattr(self,"_title") and isinstance(title,str) and len(title) > 0:
            self._title = title

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list({result.player for result in self.results() if result.game == self})

    def average_score(self, player):
        num_scored = [result.score for result in self.results() if result.player == player]
        return sum(num_scored)/len(num_scored) if len(num_scored) else 0 
class Player:
    all = []
    def __init__(self, username):
        self.username = username
        Player.all.append(self)
    
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self,username):
        if isinstance(username,str) and 2 <= len(username) <=16:
            self._username = username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list({result.game for result in self.results() if result.player == self})

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return sum(1 for result in self.results() if result.game == game)

class Result:
    all = []
    def __init__(self, player, game, score:int):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
    @property
    def game(self):
        return self._game
    @game.setter
    def game(self,game):
        if isinstance(game,Game):
            self._game = game
    
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,score):
        if isinstance(score,int) and 1 <= score <= 5000 and not hasattr(self,"_score"):
            self._score = score