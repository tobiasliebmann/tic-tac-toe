# Tic-tac-toe
Simple game of tic tac toe I made using the [pygame library](https://www.pygame.org/docs/). Additionally the game has a main menu, a how play section, a credit screen and a nice game over screen. I tried to make the in the Art Deco style of the 20s.

## How the game works

The state of the game is represented by a 3x3 matrix which is hidden in the background. The markers of the tic tac toe grid are represented by a 1, 1 or 0 in the matrix. The marker 1 corresponds to player 1 and -1 corresponds to player 2. An empty cell in the grid is represented by a 0. This is illustrated in the image below. 

![Infor for the image](/images/github_image.png)


## Sources

The sources for this game including the python modules and images can be found below.

### Image sources

These are the sources for the images used in the game.<br>
- [Main menu background](https://wallpapercave.com/wp/wp2468562.jpg), accessed: 19.02.21, 15:00 o'clock <br>
- [How to play background](https://www.amazon.co.uk/Bilderwelten-Non-woven-wallpaper-Landscape-Format/dp/B0842NGV5N), accessed: 19.02.21, 15:03 o'clock <br>
- [Game over background](https://www.miltonandking.com/product/leopard-wallpaper/), accessed: 19.02.21, 15:05 o'clock <br>
- [Credits backgrund](https://www.photomural.com/artdeco.html#/), accessed: 19.02.21, 15:06 o'clock <br>

### Libary sources

These are the sources for the python libraries I used in the game.<br>
- [Pygame](https://github.com/pygame/pygame) <br>
- [Numpy](https://github.com/numpy/numpy) <br>
- [Functools](https://github.com/python/cpython/blob/master/Lib/functools.py)

These modules are submodules in the Git diretory. It is advised to install them via [pip](https://pypi.org/project/pip/) and not as submodules via Git. Further I also use the math module but as far I know this is included in Python and does not have to be downlaoded. The functools module is part of [CPython](https://github.com/python/cpython/).

