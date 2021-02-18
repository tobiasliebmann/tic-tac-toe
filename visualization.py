import pygame as pg

import state_machine as sm

import math as m

import sys


class Graphics:
    # The distance between vertical texts in the game so that they don't overlap.
    vertical_text_distance = 60
    # Define the screen width as 900 pixels.
    screen_width = 900
    # Define the screen width as the screen height for a quadratic screen.
    screen_height = screen_width
    # Define a tuple consisting of width and height.
    screen_size = (screen_height, screen_width)

    # Define the length of an X graphic from the top corners to each other. This defines a square where X is then
    # defined by the diagonals.
    cross_length = 250

    # the thickness of the lines making up the grid in pixels.
    grid_thickness = 68

    # width of a box in the grid
    grid_box_width = screen_width / 3 - 2*grid_thickness/3

    # Height of a box in the grid.
    grid_box_height = screen_height / 3 - 2*grid_thickness/3

    # The inner and outer radii of the circles defining the o marker.
    outer_circle_radius = screen_width / 7
    inner_circle_radius = screen_width / 8

    circle_length = 250

    # Defining RGB colors as tuples.
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    orange = (255, 128, 0)
    purple = (128, 0, 255)
    yellow = (255, 255, 0)
    pink = (255, 0, 128)
    teal = (0, 255, 255)

    # Init method.
    def __init__(self):
        # Initialize pygame
        pg.init()
        # Initialize the pygame screen.
        self.screen = pg.display.set_mode(self.screen_size)
        # Initialize the font
        self.game_font = pg.font.Font("fonts/StandingRoomOnlyNF.ttf", 46)
        self.title_font = pg.font.Font("fonts/ParkLaneNF.ttf", 80)
        # The game_state is a State object, which can be found in the file state_machine.py
        self.game_state = sm.State()
        # Initialize the gaming state
        self.game_state.state = self.game_state.menu_state
        # The replay button is also not initialized since it is a graphic that will be added when needed.
        self.to_menu_button = None
        self.to_game_button = None
        self.to_credits_button = None
        self.to_how_to_play_button = None
        self.quit_button = None
        self.buttons = []
        self.cursor = pg.cursors.arrow
        self.menu_background = pg.image.load("images/background_cropped.png")
        self.grid = pg.image.load("images/grid.png")
        self.cross = pg.image.load("images/marker2.png")
        self.circle = pg.image.load("images/marker1.png")

    # todo: Add method to change the font size or add the font size to the draw string method.
    # todo: Make the on_click and check_visuals method more orderly. Add methods that draw the individual game states.

    def draw_grid(self):
        """

        :return:
        """
        self.screen.fill((190, 190, 190))
        self.screen.blit(self.grid, (0, 0))

    def draw_background(self):
        """
        Draws a black background and a "Tic-Tac_toe" caption on the screen.
        :return: -
        """
        pg.display.set_caption('Tic-Tac-Toe')
        self.screen.fill(self.black)

    def draw_menu_background(self):
        """
        """
        self.screen.blit(self.menu_background, (0, 0))

    def draw_cross(self, pos_x, pos_y):
        """
        Draws a green cross in X-form with the middle of the cross being at (pos_x, pos_y)
        :param pos_x: x coordinate of the middle of the cross.
        :param pos_y: y coordinate of the middle of the cross.
        :return: -
        """

        self.screen.blit(self.cross, (pos_x - self.cross_length/2, pos_y - self.cross_length/2))
        # Draw first line.
        # pg.draw.line(self.screen, self.green, (pos_x - self.cross_length / 2, pos_y - self.cross_length / 2),
        #             (pos_x + self.cross_length / 2, pos_y + self.cross_length / 2))
        # Draw first line.
        # pg.draw.line(self.screen, self.green, (pos_x + self.cross_length / 2, pos_y - self.cross_length / 2),
        #            (pos_x - self.cross_length / 2, pos_y + self.cross_length / 2))

    def draw_circle(self, pos_x, pos_y):
        """
        Draws two circle to make it look like a circle with a hole cut in the middle. The center of both circles is
        placed at (pos_x, pos_y). The outer circle is blue and a little bigger than the inner circle which has the
        background color (black).
        :param pos_x: x coordinate of the center of the circle.
        :param pos_y: y coordinate of the center of the circle.
        :return:
        """
        pg.draw.circle(self.screen, self.blue, (pos_x, pos_y), self.outer_circle_radius)
        pg.draw.circle(self.screen, self.black, (pos_x, pos_y), self.inner_circle_radius)

    def draw_and_return_button(self, button_text, color, pos_x, pos_y):
        """
        Draws a text that says "Click for new game" on the screen at position (pos_x, pos_y). The position is defined
        in pixels. The position is defined by the upper left corner of the text.
        :param color: tuple,
        :param button_text: str, Text displayed on the button.
        :param pos_x: Int, x-coordinate of the upper left corner of the replay button.
        :param pos_y: Int, y-coordinate of the upper left corner of the replay button.
        :return: -
        """
        button_graphic = self.game_font.render(button_text, True, color)
        (button_graphic_width, button_graphic_height) = button_graphic.get_size()
        return self.screen.blit(button_graphic, (round(pos_x - button_graphic_width / 2),
                                                 round(pos_y - button_graphic_height / 2)))

    def draw_string(self, string_to_draw, color, pos_x, pos_y):
        """

        :param color:
        :param string_to_draw:
        :param pos_x:
        :param pos_y:
        :return:
        """
        string_graphic = self.game_font.render(string_to_draw, True, color)
        (string_graphic_width, string_graphic_height) = string_graphic.get_size()
        self.screen.blit(string_graphic, (round(pos_x - string_graphic_width / 2),
                                          round(pos_y - string_graphic_height / 2)))

    def convert_indices_to_drawing_position(self, row_index, column_index):
        """
        The function converts the indices of a state matrix into a position on the screen.
        :param row_index: row index of a state matrix. Possible values are 0,1 or 2
        :param column_index: column index of a state matrix. Possible values are 0,1 or 2
        :return: The according position on the screen
        """
        return ((self.grid_box_width + self.grid_thickness) * column_index + self.grid_box_width/2,
                (self.grid_box_height + self.grid_thickness) * row_index + self.grid_box_height/2)

    def on_click(self, pos_x, pos_y):
        """
        This method does a task when a click on the screen is done. The task depends on the position of the mouse and
        the current game. In the gaming state it puts a marker at the tic-tac-toe grid. In one of the game over states.
        You can restart the game by clicking on the according text.
        :param pos_x: Int,
            x-coordinate of the mouse when clicking on the screen.
        :param pos_y: Int,
            y-coordinate of the mouse when clicking on the screen.
        :return: -
        """
        # Convert the position of the mouse to an according position oof the state matrix. The position of the state
        # matrix is given by the indices in the matrix.
        row_index = m.trunc(3 * pos_y / self.screen_width)
        column_index = m.trunc(3 * pos_x / self.screen_height)
        # Check in which state the game is in.
        current_state = self.game_state.state
        if current_state == self.game_state.gaming_state:
            # Refresh the state and check whether a player has won or the game is s draw.
            self.game_state.add_new_marker(row_index, column_index)
            # Visualize the state matrix.
            self.visualize_matrix()
        elif current_state == self.game_state.player1_won_state or current_state == self.game_state.player2_won_state \
                or current_state == self.game_state.draw_state:
            # Check if the replay button was clicked
            if self.to_game_button.collidepoint((pos_x, pos_y)):
                # If it is clicked, go back to the game and newly initialize the gaming state.
                self.game_state.state = self.game_state.gaming_state
                self.game_state.init_gaming_state()
            elif self.to_menu_button.collidepoint((pos_x, pos_y)):
                self.game_state.state = self.game_state.menu_state
            elif self.quit_button.collidepoint((pos_x, pos_y)):
                pg.quit()
                sys.exit()
        elif current_state == self.game_state.menu_state:
            self.draw_menu_background()
            if self.to_game_button.collidepoint((pos_x, pos_y)):
                self.game_state.state = self.game_state.gaming_state
                self.game_state.init_gaming_state()
            elif self.to_how_to_play_button.collidepoint((pos_x, pos_y)):
                self.game_state.state = self.game_state.how_to_play_state
            elif self.to_credits_button.collidepoint((pos_x, pos_y)):
                self.game_state.state = self.game_state.credits_state
            elif self.quit_button.collidepoint((pos_x, pos_y)):
                pg.quit()
                sys.exit()
        elif current_state == self.game_state.how_to_play_state:
            if self.to_menu_button.collidepoint((pos_x, pos_y)):
                self.game_state.state = self.game_state.menu_state
        elif current_state == self.game_state.credits_state:
            if self.to_menu_button.collidepoint((pos_x, pos_y)):
                self.game_state.state = self.game_state.menu_state

    def visualize_matrix(self):
        """
        Iterators through the state matrix of the game and puts a cross on the tic-tac-toe grid where a 1 is on the
        state matrix. A circle is put where a -1 is in the state matrix.
        :return: -
        """
        state_matrix = self.game_state.get_state_matrix()
        # Print the state matrix in the console.
        print(state_matrix)
        # Iterate through the state matrix.
        for row_index in range(3):
            for column_index in range(3):
                # Converts the indices of the state_matrix to position on the tic-tac-grid to draw the according
                # markers.
                (x, y) = self.convert_indices_to_drawing_position(row_index, column_index)
                # Draw the markers.
                if state_matrix[row_index, column_index] == self.game_state.player1_marker:
                    self.draw_cross(x, y)
                elif state_matrix[row_index, column_index] == self.game_state.player2_marker:
                    self.draw_circle(x, y)

    def adjust_cursor(self):
        """
        Iterators through the list buttons and check if the mouse is at one of these buttons. If this is the case,
        the cursor changes its image to a diamond.
        :return: -
        """
        # If the mouse is hovering over a clickable button the cursor is changed to a diamond.
        for b in self.buttons:
            if b.collidepoint(pg.mouse.get_pos()):
                self.cursor = pg.cursors.diamond
                break
            else:
                self.cursor = pg.cursors.arrow
        pg.mouse.set_cursor(self.cursor)

    def check_visuals(self):
        """
        This method changes the background according to the game state and only when the game state changes.
        :return: -
        """
        # Checks if the state has been changed.
        if self.game_state.get_state_changed_flag():
            self.buttons = []
            # Gaming state.
            if self.game_state.state == self.game_state.menu_state:
                self.draw_menu_background()
                title = self.title_font.render("Tic-Tac-Toe", True, self.white)
                self.screen.blit(title, (220, 5))
                text_vertical_middle = 6 * self.screen_height / 11
                self.to_game_button = self.draw_and_return_button("Play game", self.white, self.screen_width / 2,
                                                                  text_vertical_middle - self.vertical_text_distance)
                self.to_how_to_play_button = self.draw_and_return_button("How to play game", self.white,
                                                                         self.screen_width / 2, text_vertical_middle)
                self.to_credits_button = self.draw_and_return_button("Credits",
                                                                     self.white, self.screen_width / 2,
                                                                     text_vertical_middle + self.vertical_text_distance)
                self.quit_button = self.draw_and_return_button("Quit", self.white, self.screen_width / 2,
                                                               text_vertical_middle + 2 * self.vertical_text_distance)
                self.buttons = [self.to_game_button, self.to_how_to_play_button, self.to_credits_button,
                                self.quit_button]
            elif self.game_state.state == self.game_state.gaming_state:
                self.draw_background()
                self.draw_grid()
            elif self.game_state.state == self.game_state.how_to_play_state:
                self.draw_background()
                self.to_menu_button = self.draw_and_return_button("Main menu",
                                                                  self.red, 150, 40)
                self.buttons = [self.to_menu_button]
                self.game_font = pg.font.Font("fonts/StandingRoomOnlyNF.ttf", 32)
                self.draw_string("The game is played by two players.",
                                 self.white, self.screen_width / 2,
                                 self.screen_height / 2 - 3 * self.vertical_text_distance)
                self.draw_string("Player 1 has the cross and player 2",
                                 self.white, self.screen_width / 2,
                                 self.screen_height / 2 - 2 * self.vertical_text_distance)
                self.draw_string("has the circles. To place a marker",
                                 self.white, self.screen_width / 2,
                                 self.screen_height / 2 - self.vertical_text_distance)
                self.draw_string("just click on the screen. Player 1",
                                 self.white, self.screen_width / 2, self.screen_height / 2)
                self.draw_string("always has the first move in the game.",
                                 self.white, self.screen_width / 2,
                                 self.screen_height / 2 + self.vertical_text_distance)
                self.draw_string("Have fun :)",
                                 self.white, self.screen_width / 2,
                                 self.screen_height / 2 + 2 * self.vertical_text_distance)

                self.game_font = pg.font.Font("fonts/StandingRoomOnlyNF.ttf", 46)
            elif self.game_state.state == self.game_state.credits_state:
                self.draw_background()
                self.to_menu_button = self.draw_and_return_button("Main menu",
                                                                  self.red, 150, 40)
                self.buttons = [self.to_menu_button]
                self.game_font = pg.font.Font("fonts/StandingRoomOnlyNF.ttf", 32)
                self.draw_string("Lead programmer - Tobias Liebmann",
                                 self.white, self.screen_width / 2,
                                 self.screen_height / 2 - 2 * self.vertical_text_distance)
                self.draw_string("Lead artist - Tobias Liebmann",
                                 self.white, self.screen_width / 2,
                                 self.screen_height / 2 - self.vertical_text_distance)
                self.draw_string("sound design - Tobias Liebmann",
                                 self.white, self.screen_width / 2, self.screen_height / 2)
                self.draw_string("executive producer - Tobias Liebmann",
                                 self.white, self.screen_width / 2,
                                 self.screen_height / 2 + self.vertical_text_distance)
                self.draw_string("A Tobias Liebmann production",
                                 self.white, self.screen_width / 2,
                                 self.screen_height / 2 + 2 * self.vertical_text_distance)
                self.game_font = pg.font.Font("fonts/StandingRoomOnlyNF.ttf", 46)
            else:
                # Add a little delay so that the change to the winning screen is not to abrupt.
                pg.time.delay(500)
                self.draw_background()
                self.to_game_button = self.draw_and_return_button("New game", self.red, 150, 40)
                self.to_menu_button = self.draw_and_return_button("Main menu", self.red,
                                                                  156, 40 + self.vertical_text_distance)
                self.quit_button = self.draw_and_return_button("Quit", self.red, 830, 40)
                self.buttons = [self.to_game_button, self.to_menu_button, self.quit_button]
                # Player 1 has won.
                if self.game_state.state == self.game_state.player1_won_state:
                    self.draw_string("Player 1 has won.", self.white, self.screen_width / 2, self.screen_height / 2)
                    self.game_state.player1_win_flag = False
                # Player 2 has won.
                elif self.game_state.state == self.game_state.player2_won_state:
                    self.draw_string("Player 2 has won.", self.white, self.screen_width / 2, self.screen_height / 2)
                    self.game_state.player2_win_flag = False
                # Game ended with a draw.
                elif self.game_state.state == self.game_state.draw_state:
                    self.draw_string("Draw.", self.white, self.screen_width / 2, self.screen_height / 2)
                    self.game_state.draw_flag = False
            # Toggle the flag back to the previous value.
            self.game_state.state_changed_flag = False
        self.adjust_cursor()
