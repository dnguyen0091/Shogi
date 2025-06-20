# Shogi Game in Python with Pygame
# Improved UI/UX and game logic

import pygame
import sys

pygame.init()
WIDTH = 1200
HEIGHT = 1000
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Shogi - Japanese Chess')
font = pygame.font.Font('freesansbold.ttf', 16)
medium_font = pygame.font.Font('freesansbold.ttf', 24)
big_font = pygame.font.Font('freesansbold.ttf', 36)
small_font = pygame.font.Font('freesansbold.ttf', 14)
timer = pygame.time.Clock()
fps = 60

# Color scheme
BOARD_LIGHT = (240, 217, 181)
BOARD_DARK = (181, 136, 99)
BACKGROUND = (50, 50, 50)
UI_BACKGROUND = (70, 70, 70)
TEXT_COLOR = (255, 255, 255)
HIGHLIGHT_SELECTION = (255, 255, 0)
HIGHLIGHT_VALID = (0, 255, 0)
HIGHLIGHT_CHECK = (255, 0, 0)
# Shogi piece setup - corrected for proper Shogi rules
# Gote (Black) pieces - at top of board
black_pieces = ['lance', 'knight', 'silver', 'gold', 'king', 'gold', 'silver', 'knight', 'lance',
                'rook', 'bishop',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0),
                   (1, 1), (7, 1),
                   (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)]

# Sente (White) pieces - at bottom of board  
white_pieces = ['lance', 'knight', 'silver', 'gold', 'king', 'gold', 'silver', 'knight', 'lance',
                'rook', 'bishop',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8),
                   (1, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6)]

# Game state variables
captured_pieces_white = []
captured_pieces_black = []
promoted_pieces = []  # Track promoted pieces
turn_step = 0  # 0: white select, 1: white move, 2: black select, 3: black move
selection = 100
valid_moves = []
move_history = []
check_state = False
# load in game piece images (queen, king, rook, bishop, knight, pawn) x 2
top_gold = pygame.image.load('sprites/Top Board/GoldGeneral2.png')
top_gold = pygame.transform.scale(top_gold, (80, 80))
small_top_gold = pygame.transform.scale(top_gold, (45, 45))
top_lance = pygame.image.load('sprites/Top Board/Lance2.png')
top_lance = pygame.transform.scale(top_lance, (80, 80))
small_top_lance = pygame.transform.scale(top_lance, (45, 45))
top_silver = pygame.image.load('sprites/Top Board/SilverGeneral2.png')
top_silver = pygame.transform.scale(top_silver, (80, 80))
small_top_silver = pygame.transform.scale(top_silver, (45, 45))
top_king = pygame.image.load('sprites/Top Board/King2.png')
top_king = pygame.transform.scale(top_king, (80, 80))
small_top_king = pygame.transform.scale(top_king, (45, 45))
top_rook = pygame.image.load('sprites/Top Board/Rook2.png')
top_rook = pygame.transform.scale(top_rook, (80, 80))
small_top_rook = pygame.transform.scale(top_rook, (45, 45))
top_bishop = pygame.image.load('sprites/Top Board/Bishop2.png')
top_bishop = pygame.transform.scale(top_bishop, (80, 80))
small_top_bishop = pygame.transform.scale(top_bishop, (45, 45))
top_knight = pygame.image.load('sprites/Top Board/Knight2.png')
top_knight = pygame.transform.scale(top_knight, (80, 80))
small_top_knight = pygame.transform.scale(top_knight, (45, 45))
top_pawn = pygame.image.load('sprites/Top Board/pawn2.png')
top_pawn = pygame.transform.scale(top_pawn, (65, 65))
small_top_pawn = pygame.transform.scale(top_pawn, (45, 45))

bottom_gold = pygame.image.load('sprites/Bottom Board/GoldGeneral.png')
bottom_gold = pygame.transform.scale(bottom_gold, (80, 80))
small_bottom_gold = pygame.transform.scale(bottom_gold, (45, 45))
bottom_silver = pygame.image.load('sprites/Bottom Board/SilverGeneral.png')
bottom_silver = pygame.transform.scale(bottom_silver, (80, 80))
small_bottom_silver = pygame.transform.scale(bottom_silver, (45, 45))
bottom_lance = pygame.image.load('sprites/Bottom Board/Lance.png')
bottom_lance = pygame.transform.scale(bottom_lance, (80, 80))
small_bottom_lance = pygame.transform.scale(bottom_lance, (45, 45))
bottom_king = pygame.image.load('sprites/Bottom Board/king.png')
bottom_king = pygame.transform.scale(bottom_king, (80, 80))
small_bottom_king = pygame.transform.scale(bottom_king, (45, 45))
bottom_rook = pygame.image.load('sprites/Bottom Board/Rook.png')
bottom_rook = pygame.transform.scale(bottom_rook, (80, 80))
small_bottom_rook = pygame.transform.scale(bottom_rook, (45, 45))
bottom_bishop = pygame.image.load('sprites/Bottom Board/Bishop.png')
bottom_bishop = pygame.transform.scale(bottom_bishop, (80, 80))
small_bottom_bishop = pygame.transform.scale(bottom_bishop, (45, 45))
bottom_knight = pygame.image.load('sprites/Bottom Board/Knight.png')
bottom_knight = pygame.transform.scale(bottom_knight, (80, 80))
small_bottom_knight = pygame.transform.scale(bottom_knight, (45, 45))
bottom_pawn = pygame.image.load('sprites/Bottom Board/pawn.png')
bottom_pawn = pygame.transform.scale(bottom_pawn, (65, 65))
small_bottom_pawn = pygame.transform.scale(bottom_pawn, (45, 45))

# Image arrays - must match piece_list order: ['pawn', 'gold', 'king', 'knight', 'rook', 'bishop', 'lance', 'silver']
white_images = [bottom_pawn, bottom_gold, bottom_king, bottom_knight, bottom_rook, bottom_bishop, bottom_lance, bottom_silver]
small_white_images = [small_bottom_pawn, small_bottom_gold, small_bottom_king, small_bottom_knight, small_bottom_rook, small_bottom_bishop, small_bottom_lance, small_bottom_silver]
black_images = [top_pawn, top_gold, top_king, top_knight, top_rook, top_bishop, top_lance, top_silver]
small_black_images = [small_top_pawn, small_top_gold, small_top_king, small_top_knight, small_top_rook, small_top_bishop, small_top_lance, small_top_silver]
piece_list = ['pawn', 'gold', 'king', 'knight', 'rook', 'bishop', 'lance', 'silver']
#piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
# check variables/ flashing counter
counter = 0
winner = ''
game_over = False


# Improved board drawing with better UI
def draw_board():
    # Fill background
    screen.fill(BACKGROUND)
    
    # Draw game board area
    board_rect = pygame.Rect(50, 50, 900, 900)
    pygame.draw.rect(screen, UI_BACKGROUND, board_rect, 3)
    
    # Draw checkered board
    for row in range(9):
        for col in range(9):
            x = 50 + col * 100
            y = 50 + row * 100
            color = BOARD_LIGHT if (row + col) % 2 == 0 else BOARD_DARK
            pygame.draw.rect(screen, color, [x, y, 100, 100])
            
    # Draw grid lines
    for i in range(10):
        # Vertical lines
        pygame.draw.line(screen, (0, 0, 0), (50 + i * 100, 50), (50 + i * 100, 950), 2)
        # Horizontal lines  
        pygame.draw.line(screen, (0, 0, 0), (50, 50 + i * 100), (950, 50 + i * 100), 2)
    
    # Draw UI panels
    # Right panel for captured pieces and game info
    pygame.draw.rect(screen, UI_BACKGROUND, [970, 50, 220, 900])
    pygame.draw.rect(screen, (0, 0, 0), [970, 50, 220, 900], 2)
    
    # Status area
    pygame.draw.rect(screen, UI_BACKGROUND, [50, 970, 900, 25])
    
    # Turn indicator
    current_player = "Sente (White)" if turn_step < 2 else "Gote (Black)"
    action = "Select piece" if turn_step % 2 == 0 else "Select destination"
    status_text = f"{current_player}: {action}"
    screen.blit(medium_font.render(status_text, True, TEXT_COLOR), (60, 972))
    
    # Game info panel
    screen.blit(font.render("SHOGI", True, TEXT_COLOR), (980, 60))
    
    # Forfeit button with proper positioning
    forfeit_rect = pygame.Rect(980, 900, 100, 40)
    pygame.draw.rect(screen, (150, 50, 50), forfeit_rect)
    pygame.draw.rect(screen, (0, 0, 0), forfeit_rect, 2)
    screen.blit(font.render("FORFEIT", True, TEXT_COLOR), (990, 915))
    
    return forfeit_rect  # Return for click detection


# Improved piece drawing with better positioning
def draw_pieces():
    for i in range(len(white_pieces)):
        piece = white_pieces[i]
        location = white_locations[i]
        x = 50 + location[0] * 100 + 10
        y = 50 + location[1] * 100 + 10
        
        # Get piece image using consistent indexing
        try:
            index = piece_list.index(piece)
            if is_promoted(i, 'white'):
                image = get_promoted_image(piece, 'white')
            else:
                image = white_images[index] if index < len(white_images) else white_images[0]  # fallback to pawn
        except (ValueError, IndexError):
            image = white_images[0]  # fallback to pawn
            
        screen.blit(image, (x, y))
        
        # Highlight selected piece
        if turn_step < 2 and selection == i:
            pygame.draw.rect(screen, HIGHLIGHT_SELECTION, 
                           [50 + location[0] * 100, 50 + location[1] * 100, 100, 100], 3)

    for i in range(len(black_pieces)):
        piece = black_pieces[i]
        location = black_locations[i]
        x = 50 + location[0] * 100 + 10
        y = 50 + location[1] * 100 + 10
        
        # Get piece image using consistent indexing
        try:
            index = piece_list.index(piece)
            if is_promoted(i, 'black'):
                image = get_promoted_image(piece, 'black')
            else:
                image = black_images[index] if index < len(black_images) else black_images[0]  # fallback to pawn
        except (ValueError, IndexError):
            image = black_images[0]  # fallback to pawn
            
        screen.blit(image, (x, y))
        
        # Highlight selected piece
        if turn_step >= 2 and selection == i:
            pygame.draw.rect(screen, HIGHLIGHT_SELECTION,
                           [50 + location[0] * 100, 50 + location[1] * 100, 100, 100], 3)

def is_promoted(piece_index, color):
    """Check if a piece is promoted"""
    return (piece_index, color) in promoted_pieces

def get_promoted_image(piece, color):
    """Get the promoted version of a piece image"""
    # For now, return the regular image - you can add promoted piece sprites later
    if color == 'white':
        return white_images[0] if white_images else bottom_pawn
    else:
        return black_images[0] if black_images else top_pawn


# function to check all pieces valid options on board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'gold':
            moves_list = check_gold(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        elif piece == 'lance':
            moves_list = check_lance(location, turn)
        elif piece == 'silver':
            moves_list = check_silver(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list


# check king valid moves
def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 8 and 0 <= target[1] <= 8:
            moves_list.append(target)
    return moves_list


# Corrected Gold General movement for Shogi
def check_gold(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
        # Gold General moves: forward, backward, left, right, diagonally forward
        targets = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1)]
    else:
        friends_list = black_locations
        enemies_list = white_locations
        # Gold General moves: forward, backward, left, right, diagonally forward
        targets = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)]
    
    for target_offset in targets:
        target = (position[0] + target_offset[0], position[1] + target_offset[1])
        if target not in friends_list and 0 <= target[0] <= 8 and 0 <= target[1] <= 8:
            moves_list.append(target)
    return moves_list

# Corrected Lance movement - moves only forward in straight line
def check_lance(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
        direction = -1  # White lances move toward row 0
    else:
        friends_list = black_locations
        enemies_list = white_locations
        direction = 1   # Black lances move toward row 8
    
    # Lance moves straight forward until blocked
    chain = 1
    while True:
        target = (position[0], position[1] + (chain * direction))
        if 0 <= target[0] <= 8 and 0 <= target[1] <= 8:
            if target not in friends_list:
                moves_list.append(target)
                if target in enemies_list:
                    break  # Stop after capturing
                chain += 1
            else:
                break  # Blocked by friendly piece
        else:
            break  # Out of bounds
    return moves_list

# check bishop moves
def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 8 and 0 <= position[1] + (chain * y) <= 8:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# check rook moves
def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 8 and 0 <= position[1] + (chain * y) <= 8:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

# Corrected Silver General movement for Shogi
def check_silver(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
        # Silver moves: forward, diagonally forward, diagonally backward
        targets = [(0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    else:
        friends_list = black_locations
        enemies_list = white_locations
        # Silver moves: forward, diagonally forward, diagonally backward  
        targets = [(0, 1), (-1, 1), (1, 1), (-1, -1), (1, -1)]
    
    for target_offset in targets:
        target = (position[0] + target_offset[0], position[1] + target_offset[1])
        if target not in friends_list and 0 <= target[0] <= 8 and 0 <= target[1] <= 8:
            moves_list.append(target)
    return moves_list
# Corrected Pawn movement for Shogi
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
        # White pawns move forward (toward row 0)
        target = (position[0], position[1] - 1)
    else:
        friends_list = black_locations
        enemies_list = white_locations
        # Black pawns move forward (toward row 8)
        target = (position[0], position[1] + 1)
    
    # Pawn can only move forward one square if not blocked
    if (target not in friends_list and target not in enemies_list and 
        0 <= target[0] <= 8 and 0 <= target[1] <= 8):
        moves_list.append(target)
    # Pawn can capture diagonally forward (in Shogi, pawns capture forward only)
    elif target in enemies_list and 0 <= target[0] <= 8 and 0 <= target[1] <= 8:
        moves_list.append(target)
        
    return moves_list


# check valid knight moves
def check_knight(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
        targets = [(-1, 2), (1, 2)]  # Moves for a white knight
    else:
        friends_list = black_locations
        enemies_list = white_locations
        targets = [(-1, -2), (1, -2)]  # Moves for a black knight

    for i in range(2):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 8 and 0 <= target[1] <= 8:  # Adjusted for a 9x9 board
            moves_list.append(target)
    return moves_list


# check for valid moves for just selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options


# Improved valid moves display
def draw_valid(moves):
    for move in moves:
        x = 50 + move[0] * 100 + 50
        y = 50 + move[1] * 100 + 50
        pygame.draw.circle(screen, HIGHLIGHT_VALID, (x, y), 15)
        pygame.draw.circle(screen, (0, 0, 0), (x, y), 15, 2)


# Improved captured pieces display
def draw_captured():
    # White captured pieces (black pieces captured by white) - display on right side
    screen.blit(small_font.render("White captured:", True, TEXT_COLOR), (980, 80))
    y_offset = 110
    for i, piece in enumerate(captured_pieces_white):
        if i < 12:  # Limit display to prevent overflow
            try:
                index = piece_list.index(piece)
                if index < len(small_black_images):
                    screen.blit(small_black_images[index], (980, y_offset + i * 25))
                screen.blit(small_font.render(piece[:4], True, TEXT_COLOR), (1030, y_offset + i * 25 + 5))
            except (ValueError, IndexError):
                screen.blit(small_font.render(piece[:4], True, TEXT_COLOR), (980, y_offset + i * 25 + 5))
    
    # Black captured pieces (white pieces captured by black) - display on right side  
    screen.blit(small_font.render("Black captured:", True, TEXT_COLOR), (980, 430))
    y_offset = 460
    for i, piece in enumerate(captured_pieces_black):
        if i < 12:  # Limit display to prevent overflow
            try:
                index = piece_list.index(piece)
                if index < len(small_white_images):
                    screen.blit(small_white_images[index], (980, y_offset + i * 25))
                screen.blit(small_font.render(piece[:4], True, TEXT_COLOR), (1030, y_offset + i * 25 + 5))
            except (ValueError, IndexError):
                screen.blit(small_font.render(piece[:4], True, TEXT_COLOR), (980, y_offset + i * 25 + 5))


# draw a flashing square around king if in check
def draw_check():
    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [white_locations[king_index][0] * 100 + 1,
                                                              white_locations[king_index][1] * 100 + 1, 100, 100], 5)
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark blue', [black_locations[king_index][0] * 100 + 1,
                                                               black_locations[king_index][1] * 100 + 1, 100, 100], 5)


def draw_game_over():
    # Draw semi-transparent overlay
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(128)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))
    
    # Draw game over box
    game_over_rect = pygame.Rect(200, 300, 600, 200)
    pygame.draw.rect(screen, UI_BACKGROUND, game_over_rect)
    pygame.draw.rect(screen, (0, 0, 0), game_over_rect, 3)
    
    # Draw text
    winner_text = big_font.render(f'{winner} Wins!', True, TEXT_COLOR)
    restart_text = medium_font.render('Press ENTER to restart', True, TEXT_COLOR)
    
    # Center the text
    winner_rect = winner_text.get_rect(center=(500, 350))
    restart_rect = restart_text.get_rect(center=(500, 420))
    
    screen.blit(winner_text, winner_rect)
    screen.blit(restart_text, restart_rect)


# main game loop
black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')
run = True

while run:
    timer.tick(fps)
    if counter < 30:
        counter += 1
    else:
        counter = 0
    
    # Draw everything
    forfeit_rect = draw_board()  # Get forfeit button rect for click detection
    draw_pieces()
    draw_captured()
    draw_check()
    
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            mouse_x, mouse_y = event.pos
            
            # Check forfeit button click
            if forfeit_rect.collidepoint(mouse_x, mouse_y):
                winner = 'Gote (Black)' if turn_step < 2 else 'Sente (White)'
                game_over = True
                continue
            
            # Convert to board coordinates (accounting for 50px offset)
            if 50 <= mouse_x <= 950 and 50 <= mouse_y <= 950:
                x_coord = (mouse_x - 50) // 100
                y_coord = (mouse_y - 50) // 100
                click_coords = (x_coord, y_coord)
                
                if turn_step <= 1:  # White's turn
                    if click_coords in white_locations:
                        selection = white_locations.index(click_coords)
                        if turn_step == 0:
                            turn_step = 1
                    elif click_coords in valid_moves and selection != 100:
                        # Move piece
                        white_locations[selection] = click_coords
                        if click_coords in black_locations:
                            black_piece = black_locations.index(click_coords)
                            captured_pieces_white.append(black_pieces[black_piece])
                            if black_pieces[black_piece] == 'king':
                                winner = 'Sente (White)'
                                game_over = True
                            black_pieces.pop(black_piece)
                            black_locations.pop(black_piece)
                        
                        # Update game state
                        black_options = check_options(black_pieces, black_locations, 'black')
                        white_options = check_options(white_pieces, white_locations, 'white')
                        turn_step = 2
                        selection = 100
                        valid_moves = []
                        
                elif turn_step > 1:  # Black's turn
                    if click_coords in black_locations:
                        selection = black_locations.index(click_coords)
                        if turn_step == 2:
                            turn_step = 3
                    elif click_coords in valid_moves and selection != 100:
                        # Move piece
                        black_locations[selection] = click_coords
                        if click_coords in white_locations:
                            white_piece = white_locations.index(click_coords)
                            captured_pieces_black.append(white_pieces[white_piece])
                            if white_pieces[white_piece] == 'king':
                                winner = 'Gote (Black)'
                                game_over = True
                            white_pieces.pop(white_piece)
                            white_locations.pop(white_piece)
                        
                        # Update game state
                        black_options = check_options(black_pieces, black_locations, 'black')
                        white_options = check_options(white_pieces, white_locations, 'white')
                        turn_step = 0
                        selection = 100
                        valid_moves = []
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                # Reset game state
                game_over = False
                winner = ''
                # Reset to proper Shogi starting positions
                black_pieces = ['lance', 'knight', 'silver', 'gold', 'king', 'gold', 'silver', 'knight', 'lance',
                               'rook', 'bishop',
                               'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                black_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0),
                                  (1, 1), (7, 1),
                                  (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)]
                
                white_pieces = ['lance', 'knight', 'silver', 'gold', 'king', 'gold', 'silver', 'knight', 'lance',
                               'rook', 'bishop',
                               'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                white_locations = [(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8),
                                  (1, 7), (7, 7),
                                  (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6)]
                
                captured_pieces_white = []
                captured_pieces_black = []
                promoted_pieces = []
                turn_step = 0
                selection = 100
                valid_moves = []
                move_history = []
                black_options = check_options(black_pieces, black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white')

    if winner != '':
        game_over = True
        draw_game_over()

    pygame.display.flip()

pygame.quit()
sys.exit()