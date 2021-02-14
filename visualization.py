import pygame as pg

import state_machine as sm

import math as m


class Graphics:

    # Define the screen width as 900 pixels.
    screen_width = 900
    # Define the screen width as the screen height for a quadratic screen.
    screen_height = screen_width
    # Define a tuple consisting of width and height.
    screen_size = (screen_height, screen_width)

    # Define the length of an X graphic from the top corners to each other. This defines a square where X is then
    # defined by the diagonals.
    cross_length = screen_width / 3

    # The inner and outer radii of the circles defining the o marker.
    outer_circle_radius = screen_width / 7
    inner_circle_radius = screen_width / 8

    # Defining RGB colors as tuples.
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    # Init method.
    def __init__(self):
        # Initialize pygame
        pg.init()
        # Initialize the pygame screen.
        self.screen = pg.display.set_mode(self.screen_size)
        # Initialize the font
        self.game_font = pg.font.SysFont("Comic Sans MS", 30)
        # The game_state is a State object, which can be found in the file state_machine.py
        self.game_state = sm.State()
        # Initialize the gaming state
        self.game_state.state = self.game_state.menu_state
        # The replay button is also not initialized since it is a graphic that will be added when needed.
        self.to_menu_button = None
        self.to_game_button = None

    def draw_background(self):
        """
        Draws a black background and a "Tic-Tac_toe" caption on the screen.
        :return: -
        """
        pg.display.set_caption('Tic-Tac-Toe')
        self.screen.fill(self.black)

    def draw_grid(self):
        """
        Draws a white grid dividing the screen into nine equally large parts.
        :return: -
        """
        # Draw 3x3-grid for tic-tac-toe
        pg.draw.line(self.screen, self.white, (0, self.screen_height / 3), (self.screen_width, self.screen_height / 3))
        pg.draw.line(self.screen, self.white, (0, 2 * self.screen_height / 3),
                     (self.screen_width, 2 * self.screen_height / 3))
        pg.draw.line(self.screen, self.white, (self.screen_width / 3, 0), (self.screen_width / 3, self.screen_height))
        pg.draw.line(self.screen, self.white, (2 * self.screen_width / 3, 0),
                     (2 * self.screen_width / 3, self.screen_height))

    def draw_cross(self, pos_x, pos_y):
        """
        Draws a green cross in X-form with the middle of the cross being at (pos_x, pos_y)
        :param pos_x: x coordinate of the middle of the cross.
        :param pos_y: y coordinate of the middle of the cross.
        :return: -
        """
        # Draw first line.
        pg.draw.line(self.screen, self.green, (pos_x - self.cross_length / 2, pos_y - self.cross_length / 2),
                     (pos_x + self.cross_length / 2, pos_y + self.cross_length / 2))
        # Draw first line.
        pg.draw.line(self.screen, self.green, (pos_x + self.cross_length / 2, pos_y - self.cross_length / 2),
                     (pos_x - self.cross_length / 2, pos_y + self.cross_length / 2))

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

    def draw_button(self, button_text, color, pos_x, pos_y):
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
        return self.screen.blit(button_graphic, (round(pos_x - button_graphic_width/2), round(pos_y - button_graphic_height/2)))

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
        self.screen.blit(string_graphic, (round(pos_x - string_graphic_width/2),
                                          round(pos_y - string_graphic_height/2)))

    def convert_indices_to_drawing_position(self, row_index, column_index):
        """
        The function converts the indices of a state matrix into a position on the screen.
        :param row_index: row index of a state matrix. Possible values are 0,1 or 2
        :param column_index: column index of a state matrix. Possible values are 0,1 or 2
        :return: The according position on the screen
        """
        return (self.screen_width * column_index / 3 + self.screen_width / 6,
                self.screen_height * row_index / 3 + self.screen_height / 6)

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
        current_state = self.game_state.get_state()
        if current_state == self.game_state.gaming_state:
            # Refresh the state and check whether a player has won or the game is s draw.
            self.game_state.add_new_marker(row_index, column_index)
            # Visualize the state matrix.
            self.visualize_matrix()
        elif current_state == self.game_state.player1_won_state or current_state == self.game_state.player2_won_state or current_state == self.game_state.draw_state:
            # Check if the replay button was clicked
            if self.to_game_button.collidepoint((pos_x, pos_y)):
                # If it is clicked, go back to the game and newly initialize the gaming state.
                self.game_state.state = self.game_state.gaming_state
                self.game_state.init_gaming_state()
                self.game_state.state_changed_flag = True
            elif self.to_menu_button.collidepoint((pos_x, pos_y)):
                self.game_state.state = self.game_state.menu_state
                self.game_state.state_changed_flag = True
        elif current_state == self.game_state.menu_state:
            if self.to_game_button.collidepoint((pos_x, pos_y)):
                self.game_state.state = self.game_state.gaming_state
                self.game_state.init_gaming_state()
                self.game_state.state_changed_flag = True

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

    def check_visuals(self):
        """
        This method changes the background according to the game state and only when the game state changes.
        :return: -
        """
        # Checks if the state has been changed.
        if self.game_state.get_state_changed_flag():
            # Gaming state.
            if self.game_state.get_state() == self.game_state.menu_state:
                self.draw_background()
                self.to_game_button = self.draw_button("Play game", self.white, self.screen_width/2, self.screen_height/2)
            elif self.game_state.get_state() == self.game_state.gaming_state:
                print("Initialize gaming state.")
                self.draw_background()
                self.draw_grid()
            else:
                self.draw_background()
                self.to_game_button = self.draw_button("Click here to play a new game.", self.red, 167, 30)
                self.to_menu_button = self.draw_button("Click here to go back to main menu", self.red, 190, 60)
                # Player 1 has won.
                if self.game_state.get_state() == self.game_state.player1_won_state:
                    self.draw_string("Player 1 has won.", self.white, self.screen_width/2, self.screen_height/2)
                # Player 2 has won.
                elif self.game_state.get_state() == self.game_state.player2_won_state:
                    self.draw_string("Player 2 has won.", self.white, self.screen_width/2, self.screen_height/2)
                # Game ended with a draw.
                elif self.game_state.get_state() == self.game_state.draw_state:
                    self.draw_string("Draw.", self.white, self.screen_width/2, self.screen_height/2)
            # Toggle the flag back to the previous value.
            self.game_state.state_changed_flag = False
