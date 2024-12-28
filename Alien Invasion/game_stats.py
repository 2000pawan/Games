class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
        self.load_high_score()

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def check_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        
        # Reset high score to 0 if reaches 100000.
        if self.high_score >= 100000:
            self.high_score = 0

    def game_over(self):
        self.game_active = False
        self.reset_stats()

    def level_up(self):
        self.level += 1
        self.reset_stats()
    
    def load_high_score(self):
        '''Load the high score from the file'''
        try:
            with open('high_score.txt', 'r') as f:
                self.high_score = int(f.read())
        except FileNotFoundError:
            self.high_score=0
            
    def save_high_score(self):
        '''Save the high score to the file'''
        with open('high_score.txt', 'w') as f:
            f.write(str(self.high_score))
    
    def __str__(self):
        return f"Score: {self.score}, Level: {self.level}, Ships Left: {self.ships_left}, High Score: {self.high_score}"