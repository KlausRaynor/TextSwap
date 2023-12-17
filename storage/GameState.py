class State:
    def handle_input(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass


class GameplayState(State):
    def update(self):
        # game logic
        game_over = False
        pause_game = False
        if game_over:
            current_state = MainMenuState()
        if pause_game:
            current_state = PauseMenuState()


class MainMenuState(State):
    def handle_input(self, event):
        if event is "Start Game":
            current_state = GameplayState()


class PauseMenuState(State):
    def handle_input(self, event):
        if event is "Resume Game":
            current_state = GameplayState()