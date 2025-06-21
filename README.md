# Shogi - Japanese Chess Game

A Python implementation of Shogi (Japanese Chess) using Pygame, featuring a complete game board, piece movement system, and intuitive user interface.

## Features

- **Complete Shogi Implementation**: Full 9x9 board with traditional Japanese chess pieces
- **Authentic Piece Movement**: Accurate movement patterns for all Shogi pieces
- **Visual Interface**: Clean, user-friendly GUI with piece sprites
- **Turn-based Gameplay**: Alternating turns between Sente (White) and Gote (Black)
- **Capture System**: Track captured pieces with visual display
- **Move Validation**: Legal move checking and highlighting
- **Check Detection**: Visual indicators when kings are in check
- **Game Over Handling**: Win condition detection and restart functionality

## Game Pieces

### Traditional Shogi Pieces:
- **King (王/玉)**: Moves one square in any direction
- **Gold General (金)**: Moves one square forward, backward, left, right, or diagonally forward
- **Silver General (銀)**: Moves one square diagonally or straight forward
- **Knight (桂)**: Moves in an L-shape, two squares forward and one square left or right
- **Lance (香)**: Moves any number of squares straight forward
- **Rook (飛)**: Moves any number of squares vertically or horizontally
- **Bishop (角)**: Moves any number of squares diagonally
- **Pawn (歩)**: Moves one square straight forward

## Requirements

- Python 3.x
- Pygame library

```bash
pip install pygame
```

## Installation & Setup

1. Clone or download this repository
2. Ensure you have the required `sprites/` folder with piece images:
   - `sprites/Top Board/` - Contains black piece sprites
   - `sprites/Bottom Board/` - Contains white piece sprites
3. Install Pygame: `pip install pygame`
4. Run the game: `python shogiMain.py`

## How to Play

1. **Starting the Game**: Run `shogiMain.py` to start
2. **Selecting Pieces**: Click on your pieces to select them (highlighted in yellow)
3. **Moving Pieces**: After selection, valid moves are shown as green circles - click on a valid square to move
4. **Turn System**: 
   - Sente (White) plays first from the bottom
   - Gote (Black) plays from the top
   - Turns alternate automatically
5. **Capturing**: Move to an opponent's square to capture their piece
6. **Winning**: Capture the opponent's King to win the game
7. **Forfeit**: Click the "FORFEIT" button to concede the game
8. **Restart**: Press ENTER after game over to start a new game

## Controls

- **Mouse Click**: Select pieces and make moves
- **ENTER**: Restart game after game over
- **Forfeit Button**: Surrender the current game

## File Structure

```
Shogi/
├── shogiMain.py          # Main game file with complete implementation
├── shogiDraft.txt        # Draft/development version
├── Readme.md            # This file
└── sprites/             # Game piece images
    ├── Top Board/       # Black piece sprites
    │   ├── King2.png
    │   ├── GoldGeneral2.png
    │   ├── SilverGeneral2.png
    │   ├── Knight2.png
    │   ├── Lance2.png
    │   ├── Rook2.png
    │   ├── Bishop2.png
    │   └── pawn2.png
    └── Bottom Board/    # White piece sprites
        ├── king.png
        ├── GoldGeneral.png
        ├── SilverGeneral.png
        ├── Knight.png
        ├── Lance.png
        ├── Rook.png
        ├── Bishop.png
        └── pawn.png
```

## Game Interface

- **Main Board**: 9x9 grid with alternating light and dark squares
- **Status Bar**: Shows current player and action (select piece/destination)
- **Captured Pieces Panel**: Displays pieces captured by each player
- **Visual Feedback**: 
  - Yellow highlight for selected pieces
  - Green circles for valid moves
  - Red flashing for kings in check

## Development Notes

The project includes two versions:
- **shogiMain.py**: Complete, polished version with full UI and game logic
- **shogiDraft.txt**: Development version with object-oriented piece classes

## Future Enhancements

- Piece promotion system
- Drop move functionality (placing captured pieces)
- AI opponent
- Move history and notation
- Save/load game functionality
- Sound effects
- Animation for piece movements

## Contributing

Feel free to fork this project and submit pull requests for improvements or bug fixes.

## License

This project is open source and available under the MIT License.
