# two player chess in python with Pygame!
# part one, set up variables images and game loop

import pygame

pygame.init()
WIDTH = 1100
HEIGHT = 1000
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Two-Player Pygame Chess!')
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60
white_pieces = ['lance', 'knight', 'silver','gold', 'king', 'gold', 'silver', 'knight', 'lance',
                'bishop','rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn','pawn']
white_locations = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                (1,1),(7,1),
                (0,2),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(8,2)]
black_pieces = ['lance', 'knight', 'silver','gold', 'king', 'gold', 'silver', 'knight', 'lance',
                'bishop','rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn','pawn']
black_locations = [(0,8),(1,8),(2,8),(3,8),(4,8),(5,8),(6,8),(7,8),(8,8),
                (1,7),(7,7),
                (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6),(8,6)]

captured_pieces_white = []
captured_pieces_black = []
# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
turn_step = 0
selection = 100
valid_moves = []
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
small_top_pawn = pygame.transform.scale(top_bishop, (45, 45))
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
small_bottom_knight = pygame.transform.scale(bottom_knight, (80, 80))
small_bottom_bishop = pygame.transform.scale(bottom_knight, (45, 45))
bottom_pawn = pygame.image.load('sprites/Bottom Board/pawn.png')
bottom_pawn = pygame.transform.scale(bottom_pawn, (65, 65))
small_bottom_pawn = pygame.transform.scale(bottom_pawn, (45, 45))

white_images = [bottom_gold, bottom_silver, bottom_king, bottom_knight, bottom_rook, bottom_bishop,bottom_lance,bottom_pawn]
small_white_images = [small_bottom_gold, small_bottom_silver, small_bottom_king, small_bottom_knight,]
black_images = [top_gold, top_silver, top_king, top_knight, top_rook, top_bishop,top_lance,top_pawn]
small_black_images = [small_top_gold, small_top_silver, small_top_king, small_top_knight,small_top_lance,small_top_pawn]
piece_list = ['pawn', 'gold', 'king', 'knight', 'rook', 'bishop','lance','silver']
#piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
# check variables/ flashing counter
counter = 0
winner = ''
game_over = False


# draw main game board
def draw_board():
    for i in range(81):  # Adjusted for a 9x9 board
        column = i % 9
        row = i // 9
        color = 'light gray' if (row + column) % 2 == 0 else 'gray'
        pygame.draw.rect(screen, color, [column * 100, row * 100, 100, 100])

    # Draw the border and status text
    pygame.draw.rect(screen, 'gray', [0, 900, WIDTH, 100])  # Adjusted for a 9x9 board
    pygame.draw.rect(screen, 'gold', [0, 900, WIDTH, 100], 5)  # Adjusted for a 9x9 board
    pygame.draw.rect(screen, 'gold', [900, 0, 200, HEIGHT], 5)  # Adjusted for a 9x9 board
    status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                'Black: Select a Piece to Move!', 'Black: Select a Destination!']
    screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, 920))  # Adjusted for a 9x9 board
    for i in range(11):  # Adjusted for a 9x9 board
        pygame.draw.line(screen, 'black', (0, 100 * i), (900, 100 * i), 2)  # Adjusted for a 9x9 board
        pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 900), 2)  # Adjusted for a 9x9 board
        screen.blit(medium_font.render('FORFEIT', True, 'black'), (910, 930))  # Adjusted for a 9x9 board


# draw pieces onto board
def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(bottom_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1,
                                                 100, 100], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(top_pawn, (black_locations[i][0] * 100 + 22, black_locations[i][1] * 100 + 30))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1,
                                                  100, 100], 2)


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


# check queen valid moves
def check_gold(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
        targets = [(-1, 0), (1, 0), (-1, 1), (1, 1), (0, -1), (0, 1), (-1, 1)]
    else:
        #bottom gold
        friends_list = black_locations
        enemies_list = white_locations
        targets = [(1, 0), (1, -1), (-1, 0), (0, 1), (0, -1), (-1, -1)]
    
    for i in range(6):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <=8  and 0 <= target[1] <= 8:
            moves_list.append(target)
    return moves_list

#lance moves fix error with moving lance and pre move check
def check_lance(position, color):
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

def check_silver(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
        targets = [(-1, 1), (1, 1), (-1, -1), (0, 1), (1, -1)]
    else:
        friends_list = black_locations
        enemies_list = white_locations
        targets = [(1, -1), (-1, -1), (1, 1), (0, -1), (-1, 1)]
    for i in range(5):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 8 and 0 <= target[1] <= 8:
            moves_list.append(target)
    return moves_list
# check valid pawn moves
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
        targets=[(0,1)]
    else:
        friends_list = black_locations
        enemies_list = white_locations
        targets=[(0,-1)]
    target=(position[0]+targets[0][0],position[1]+targets[0][1])
    if target not in friends_list and 0 <= target[0] <= 8 and 0 <= target[1] <= 8:
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


# draw valid moves on screen
def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)


# draw captured pieces on side of screen
def draw_captured():
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (925, 5 + 50 * i))
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (1025, 5 + 50 * i))


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
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))


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
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    draw_captured()
    draw_check()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords == (9, 9) or click_coords == (10, 9):
                    winner = 'black'
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] = click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coords == (9, 9) or click_coords == (10, 9):
                    winner = 'white'
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_locations[selection] = click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                winner = ''
                white_pieces = ['lance', 'knight', 'silver','gold', 'king', 'gold', 'silver', 'knight', 'lance',
                                'bishop','rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn','pawn']
                white_locations = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (1,1),(7,1),
                                    (0,2),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(8,2)]
                black_pieces = ['lance', 'knight', 'silver','gold', 'king', 'gold', 'silver', 'knight', 'lance',
                                'bishop','rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn','pawn']
                black_locations = [(0,8),(1,8),(2,8),(3,8),(4,8),(5,8),(6,8),(7,8),(8,8),
                                    (1,7),(7,7),
                                    (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6),(8,6)]
                captured_pieces_white = []
                captured_pieces_black = []
                turn_step = 0
                selection = 100
                valid_moves = []
                black_options = check_options(black_pieces, black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white')

    if winner != '':
        game_over = True
        draw_game_over()

    pygame.display.flip()
pygame.quit()