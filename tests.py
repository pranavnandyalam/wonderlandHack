import matplotlib.pyplot as plt

# Function to create a chessboard
def create_chess_board(size=8, tile_size=1):
    """
    Creates a chess board with given size and tile size.

    :param size: int - the size of the chess board (number of tiles per row and column)
    :param tile_size: float - the size of each tile
    :return: matplotlib figure and axis objects
    """
    # Create the chess board pattern
    board = [[((i+j) % 2) for j in range(size)] for i in range(size)]

    # Create a figure and axis to plot the board
    fig, ax = plt.subplots(figsize=(size*tile_size/2, size*tile_size/2))
    ax.imshow(board, cmap='binary', interpolation='nearest')

    # Remove the axes for visual appeal
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis('off')

    return fig, ax

# Create an 8x8 chessboard
fig, ax = create_chess_board()

# Save the chess board to a file
file_path = '/mnt/data/chess_board.png'
plt.savefig(file_path, bbox_inches='tight', pad_inches=0)
plt.close()

file_path
