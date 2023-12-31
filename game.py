import pygame


class Game(object):
    def __init__(self, screen, states, start_state):
        self.done = False  # when true game over and exit app
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.states = states
        self.state_name = start_state
        self.state = self.states[self.state_name]

    # handles key presses, etc. in a given state
    def event_loop(self):
        for event in pygame.event.get():
            self.state.get_event(event)

    # if state is marked as being done, this function triggers
    # persistent = any persistent values to carry between states
    def change_state(self):
        current_state = self.state_name
        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        persistent = self.state.persist
        self.state = self.states[self.state_name]
        self.state.startup(persistent)

    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.change_state()
        self.state.update(dt)

    def draw(self):
        self.state.draw(self.screen)

    # main game loop function
    def run(self):
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw()
            pygame.display.update()
