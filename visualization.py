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

    # the thickness of the lines making up the grid in pixels.
    grid_thickness = 68

    # width of a box in the grid
    grid_box_width = screen_width / 3 - 2*grid_thickness/3

    # Height of a box in the grid.
    grid_box_height = screen_height / 3 - 2*grid_thickness/3

    # The diameter of the "circle" marker.
    circle_diameter = 250

    # defined by the diagonals.
    cross_length = 250

    # Defining RGB colors as tuples.
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (165, 18, 32)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    orange = (255, 128, 0)
    purple = (128, 0, 255)
    yellow = (255, 255, 0)
    pink = (255, 0, 128)
    teal = (0, 255, 255)
    text_color = white

    # Init method.
    def __init__(self):
        # Initialize pygame
        pg.init()

        # Initialize the pygame screen.
        self.screen = pg.display.set_mode(self.screen_size)

        # Set the caption for the pygame, that pops up on the screen.
        pg.display.set_caption('Tic-Tac-Toe')

        # Initialize the font
        self.game_font = pg.font.Font("fonts/StandingRoomOnlyNF.ttf", 46)
        self.title_font = pg.font.Font("fonts/ParkLaneNF.ttf", 80)

        # The game_state is a State object, which can be found in the file state_machine.py
        self.game_state = sm.State()

        # Initialize the state in which the game starts.
        self.game_state.state = self.game_state.menu_state

        # Initialize the buttons
        self.to_menu_button = None
        self.to_game_button = None
        self.to_credits_button = None
        self.to_how_to_play_button = None
        self.quit_button = None
        self.buttons = []

        # Set the cursor to an arrow.
        self.cursor = pg.cursors.arrow

        # Load all the images that are needed for the game.
        self.menu_background = pg.image.load("images/background_cropped.png")
        self.how_to_play_background = pg.image.load("images/background3_cropped.png")
        self.credits_background = pg.image.load("images/background4_cropped.png")
        self.game_over_background = pg.image.load("images/background2_cropped.png")
        self.game_background = pg.image.load("images/game_background.png")
        self.grid = pg.image.load("images/grid.png")
        self.cross = pg.image.load("images/marker2.png")
        self.circle = pg.image.load("images/marker1.png")

    def draw_cross(self, pos_x, pos_y):
        """
        Draws a cross which can be looked up at images/marker2.png. The coordinates to be entered, correspond to the
        center of the cross.
        :param pos_x: x coordinate of the center of the cross.
        :param pos_y: y coordinate of the center of the cross.
        :return: -
        """
        self.screen.blit(self.cross, (pos_x - self.cross_length/2, pos_y - self.cross_length/2))

    def draw_circle(self, pos_x, pos_y):
        """
        Draws a "circle" which can be looked up at images/marker1.png. The coordinates to be entered, correspond to the
        center of the "circle".
        :param pos_x: x coordinate of the center of the circle.
        :param pos_y: y coordinate of the center of the circle.
        :return:
        """
        self.screen.blit(self.circle, (pos_x - self.circle_diameter/2, pos_y - self.circle_diameter/2))

    def draw_and_return_button(self, button_text, color, pos_x, pos_y):
        """
        Draws a text that says "button_text" on the screen at position (pos_x, pos_y) with the color.
        The position is define in pixels. The position is defined by the upper left corner of the text.
        :param color: tuple, color of the button text represented by a tuple of RGB colors.
        :param button_text: str, Text displayed on the button.
        :param pos_x: Int, x-coordinate of the center of the button.
        :param pos_y: Int, y-coordinate of the center of the button.
        :return: -
        """
        button_graphic = self.game_font.render(button_text, True, color)
        (button_graphic_width, button_graphic_height) = button_graphic.get_size()
        return self.screen.blit(button_graphic, (round(pos_x - button_graphic_width / 2),
                                                 round(pos_y - button_graphic_height / 2)))

    def draw_string(self, string_to_draw, color, pos_x, pos_y):
        """

        :param color: tuple, color of the text entered as a RGB tuple.
        :param string_to_draw: str, text which is displayed on the screen.
        :param pos_x: Int, x-coordinate of the center of the string.
        :param pos_y: Int, y-coordinate of the center of the string.
        :return: -
        """
        string_graphic = self.game_font.render(string_to_draw, True, color)
        (string_graphic_width, string_graphic_height) = string_graphic.get_size()
        self.screen.blit(string_graphic, (round(pos_x - string_graphic_width / 2),
                                          round(pos_y - string_graphic_height / 2)))

    def convert_indices_to_drawing_position(self, row_index, column_index):
        """
        The function converts the indices of a state matrix into a position on the screen.
        The position on the screen is for the markers which drawn. So they correspond to the middle of a cell
        of the tic-tac-toe grid.
        :param row_index: row index of a state matrix. Possible values are 0,1 or 2
        :param column_index: column index of a state matrix. Possible values are 0,1 or 2
        :return: The according position on the screen
        """
        return ((self.grid_box_width + self.grid_thickness) * column_index + self.grid_box_width/2,
                (self.grid_box_height + self.grid_thickness) * row_index + self.grid_box_height/2)

    def on_click(self, pos_x, pos_y):
        """
        This method does a task when a click on the screen is done. The task depends on the position of the mouse and
        the current state of the game. In the main menu state you can start the game, go to the credits, read how
        to play the game or quit the game. In the gaming state it puts a marker at the tic-tac-toe grid.
        In one of the game over states you can click the buttons to restart etc.
        :param pos_x: Int, x-coordinate of the mouse when clicking on the screen.
        :param pos_y: Int, y-coordinate of the mouse when clicking on the screen.
        :return: -
        """
        # Convert the position of the mouse to an according position of the state matrix. The position of the state
        # matrix is given by the indices in the matrix.
        row_index = m.trunc(3 * pos_y / self.screen_width)
        column_index = m.trunc(3 * pos_x / self.screen_height)
        # Check in which state the game is in.
        current_state = self.game_state.state
        # Gaming state.
        if current_state == self.game_state.gaming_state:
            # Refresh the state and check whether a player has won or the game is s draw.
            self.game_state.add_new_marker(row_index, column_index)
            # Visualize the state matrix.
            self.visualize_matrix()
        # Game over states.
        elif current_state == self.game_state.player1_won_state or current_state == self.game_state.player2_won_state \
                or current_state == self.game_state.draw_state:
            # Check if the replay button was clicked
            if self.to_game_button.collidepoint((pos_x, pos_y)):
                # If it is clicked, go back to the game and newly initialize the gaming state.
                self.game_state.state = self.game_state.gaming_state
            elif self.to_menu_button.collidepoint((pos_x, pos_y)):
                # Clicking this button makes you go back to the main menu.
                self.game_state.state = self.game_state.menu_state
            elif self.quit_button.collidepoint((pos_x, pos_y)):
                # Quit the game.
                pg.quit()
                sys.exit()
        # Main menu state.
        elif current_state == self.game_state.menu_state:
            # Draw all the buttons in the main menu and change the game state accordingly if a button is clicked.
            if self.to_game_button.collidepoint((pos_x, pos_y)):
                self.game_state.state = self.game_state.gaming_state
            elif self.to_how_to_play_button.collidepoint((pos_x, pos_y)):
                self.game_state.state = self.game_state.how_to_play_state
            elif self.to_credits_button.collidepoint((pos_x, pos_y)):
                self.game_state.state = self.game_state.credits_state
            elif self.quit_button.collidepoint((pos_x, pos_y)):
                # Quit the game.
                pg.quit()
                sys.exit()
        # How to play state.
        elif current_state == self.game_state.how_to_play_state:
            if self.to_menu_button.collidepoint((pos_x, pos_y)):
                self.game_state.state = self.game_state.menu_state
        # Credit state.
        elif current_state == self.game_state.credits_state:
            if self.to_menu_button.collidepoint((pos_x, pos_y)):
                self.game_state.state = self.game_state.menu_state

    def visualize_matrix(self):
        """
        Iterators through the 3x3 state matrix of the game and puts a cross on the tic-tac-toe grid on screen where a 1
        is in the state matrix. A circle is put where a -1 is in the state matrix.
        :return: -
        """
        # SAve the current state matrix.
        state_matrix = self.game_state.get_state_matrix()
        # Iterate through the state matrix.
        for row_index in range(3):
            for column_index in range(3):
                # Converts the indices of the state_matrix to position on the tic-tac-toe grid on the screen to draw
                # the according markers.
                (x, y) = self.convert_indices_to_drawing_position(row_index, column_index)
                # Draw the markers.
                if state_matrix[row_index, column_index] == self.game_state.player1_marker:
                    self.draw_cross(x, y)
                elif state_matrix[row_index, column_index] == self.game_state.player2_marker:
                    self.draw_circle(x, y)

    def adjust_cursor(self):
        """
        Iterators through the list buttons and checks if the mouse is at one of these buttons. If this is the case,
        the cursor changes its image to a diamond.
        :return: -
        """
        # If the mouse is hovering over a clickable button the cursor is changed to a diamond.
        for b in self.buttons:
            # Check if the mouse is over a button.
            if b.collidepoint(pg.mouse.get_pos()):
                # Set the cursor and leave the loop.
                self.cursor = pg.cursors.diamond
                break
            else:
                # If the mouse is not over a button change it to an arrow.
                self.cursor = pg.cursors.arrow
        pg.mouse.set_cursor(self.cursor)

    def init_menu(self):
        """
        Initializes the the visuals for the main menu. The visuals consist of a background, a title and multiple
        buttons. The buttons are the game button taking you to the game, the how to play button explaining you how to
        play the game, the credits button which takes you to the credits and the quit button which quits the game.
        :return: -
        """
        # Draw the background for the menu.
        self.screen.blit(self.menu_background, (0, 0))
        # Draw the title.
        title = self.title_font.render("Tic-Tac-Toe", True, self.white)
        self.screen.blit(title, (220, 5))
        # The text_vertical_middle variable is used to vertically align the buttons on the screen.
        text_vertical_middle = 6 * self.screen_height / 11
        # Draw the buttons and add them to the buttons list.
        self.to_game_button = self.draw_and_return_button("Play game", self.text_color, self.screen_width / 2,
                                                          text_vertical_middle - self.vertical_text_distance)
        self.to_how_to_play_button = self.draw_and_return_button("How to play", self.text_color,
                                                                 self.screen_width / 2, text_vertical_middle)
        self.to_credits_button = self.draw_and_return_button("Credits",
                                                             self.text_color, self.screen_width / 2,
                                                             text_vertical_middle + self.vertical_text_distance)
        self.quit_button = self.draw_and_return_button("Quit", self.text_color, self.screen_width / 2,
                                                       text_vertical_middle + 2 * self.vertical_text_distance)
        self.buttons = [self.to_game_button, self.to_how_to_play_button, self.to_credits_button,
                        self.quit_button]

    def init_game(self):
        """
        Initializes the state matrix for the gaming state and the visuals by drawing the background and the grid.
        :return: -
        """
        self.game_state.init_gaming_state()
        # self.screen.fill((190, 190, 190))
        self.screen.fill(self.white)
        self.screen.blit(self.game_background, (0, 0))
        self.screen.blit(self.grid, (0, 0))

    def init_how_to_play(self):
        """
        Initializes the visuals for the screen describing how to play the game. The explanations are printed out
        individually and a button to go back to the main menu is added.
        :return: -
        """
        # Draw the button to go back to the menu and add it to the buttons list.
        self.screen.blit(self.how_to_play_background, (0, 0))
        self.to_menu_button = self.draw_and_return_button("Main menu",
                                                          self.text_color, 150, 40)
        self.buttons = [self.to_menu_button]

        # Print the explanations on how to play the game.
        # They are printed out individually since I don't know how to this better.
        # Change the font size.
        self.game_font = pg.font.Font("fonts/StandingRoomOnlyNF.ttf", 32)
        self.draw_string("The game is played by two players.",
                         self.text_color, self.screen_width / 2,
                         self.screen_height / 2 - 3 * self.vertical_text_distance)
        self.draw_string("Player 1 has the cross and player 2",
                         self.text_color, self.screen_width / 2,
                         self.screen_height / 2 - 2 * self.vertical_text_distance)
        self.draw_string("has the circles. To place a marker",
                         self.text_color, self.screen_width / 2,
                         self.screen_height / 2 - self.vertical_text_distance)
        self.draw_string("just click on the screen. Player 1",
                         self.text_color, self.screen_width / 2, self.screen_height / 2)
        self.draw_string("always has the first move in the game.",
                         self.text_color, self.screen_width / 2,
                         self.screen_height / 2 + self.vertical_text_distance)
        self.draw_string("Have fun :)",
                         self.text_color, self.screen_width / 2,
                         self.screen_height / 2 + 2 * self.vertical_text_distance)
        # Change the font size back.
        self.game_font = pg.font.Font("fonts/StandingRoomOnlyNF.ttf", 46)

    def init_credits(self):
        """
        Initialize the credit screen  and add a button to go back to the main menu and add it to the buttons list.
        :return: -
        """
        # Draw the main menu button and add it to the buttons list.
        self.screen.blit(self.credits_background, (0, 0))
        self.to_menu_button = self.draw_and_return_button("Main menu",
                                                          self.text_color, 150, 40)
        self.buttons = [self.to_menu_button]
        # Draw the credits.
        self.game_font = pg.font.Font("fonts/StandingRoomOnlyNF.ttf", 32)
        self.draw_string("Lead programmer - Tobias Liebmann",
                         self.text_color, self.screen_width / 2,
                         self.screen_height / 2 - 2 * self.vertical_text_distance)
        self.draw_string("Lead artist - Tobias Liebmann",
                         self.text_color, self.screen_width / 2,
                         self.screen_height / 2 - self.vertical_text_distance)
        self.draw_string("sound design - Tobias Liebmann",
                         self.text_color, self.screen_width / 2, self.screen_height / 2)
        self.draw_string("executive producer - Tobias Liebmann",
                         self.text_color, self.screen_width / 2,
                         self.screen_height / 2 + self.vertical_text_distance)
        self.draw_string("A Tobias Liebmann production",
                         self.text_color, self.screen_width / 2,
                         self.screen_height / 2 + 2 * self.vertical_text_distance)
        self.game_font = pg.font.Font("fonts/StandingRoomOnlyNF.ttf", 46)

    def init_game_over(self):
        """
        Initialize one of the game over states depending on the outcome of the tic-tac-toe game and reset the flags
        indicating which player won. The game over stets consist of a background image and three buttons which let you
        play a new game, go back to the main menu or quit the game. Further the outcome of the game is printed with a
        text on the middle of the screen.
        :return: -
        """
        # Add a little delay so that the change to the winning screen is not to abrupt.
        pg.time.delay(500)
        self.screen.blit(self.game_over_background, (0, 0))
        # Draw all the buttons.
        self.to_game_button = self.draw_and_return_button("New game", self.red, 150, 40)
        self.to_menu_button = self.draw_and_return_button("Main menu", self.red,
                                                          156, 40 + self.vertical_text_distance)
        self.quit_button = self.draw_and_return_button("Quit", self.red, 830, 40)
        # Add the buttons to the buttons list.
        self.buttons = [self.to_game_button, self.to_menu_button, self.quit_button]
        # Player 1 has won.
        if self.game_state.state == self.game_state.player1_won_state:
            self.draw_string("Player 1 has won.", self.text_color, self.screen_width / 2, self.screen_height / 2)
            # Toggle the according flag.
            self.game_state.player1_win_flag = False
        # Player 2 has won.
        elif self.game_state.state == self.game_state.player2_won_state:
            self.draw_string("Player 2 has won.", self.text_color, self.screen_width / 2, self.screen_height / 2)
            # Toggle the according flag.
            self.game_state.player2_win_flag = False
        # Game ended with a draw.
        elif self.game_state.state == self.game_state.draw_state:
            self.draw_string("Draw.", self.text_color, self.screen_width / 2, self.screen_height / 2)
            # Toggle the according flag.
            self.game_state.draw_flag = False

    def check_state(self):
        """
        This method changes the background according to the game state and only when the game state changes. Further
        the cursor is changed if it hovers over a button.
        :return: -
        """
        # Checks if the state has been changed.
        if self.game_state.get_state_changed_flag():
            self.buttons = []
            # Gaming state.
            if self.game_state.state == self.game_state.menu_state:
                self.init_menu()
            elif self.game_state.state == self.game_state.gaming_state:
                self.init_game()
            elif self.game_state.state == self.game_state.how_to_play_state:
                self.init_how_to_play()
            elif self.game_state.state == self.game_state.credits_state:
                self.init_credits()
            else:
                self.init_game_over()
            # Toggle the flag back to the previous value.
            self.game_state.state_changed_flag = False
        self.adjust_cursor()
