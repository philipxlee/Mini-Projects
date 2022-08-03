
import pygame, sys, random

def ball_animation():
    # Moving the ball
    # Chosen to use global variables due to the small size of this program
    global ball_speed_horizontal, ball_speed_vertical, player_score, opponent_score, score_time
    ball.x += ball_speed_horizontal 
    ball.y += ball_speed_vertical

    # Ball collisions on the window's borders
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_vertical *= -1 

    if ball.left <= 0:
        if player_score == 9:
            sys.exit("Game Finished: Player has won with 10 points!")
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        if opponent_score == 9:
            sys.exit("Game Finshed: Opponent has won with 10 points!")
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    # Ball collisions on the player's rectangle
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_horizontal *= -1

def player_animation():
    # Moving the player
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    # Moving the opponent
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.top -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_horizontal, ball_speed_vertical, score_time
    ball.center = (screen_width/2, screen_height/2)
    current_time = pygame.time.get_ticks()

    if current_time - score_time < 700: 
        three_char = game_font.render("3", False, light_grey)
        screen.blit(three_char, (screen_width/2 - 5, screen_height/2 + 20))
    if 700 < current_time - score_time < 1400: 
        two_char = game_font.render("2", False, light_grey)
        screen.blit(two_char, (screen_width/2 - 5, screen_height/2 + 20))
    if 1400 < current_time - score_time < 2100:
        one_char = game_font.render("1", False, light_grey)
        screen.blit(one_char, (screen_width/2 - 5, screen_height/2 + 20))

    if current_time - score_time < 2100: 
        ball_speed_horizontal = 0
        ball_speed_vertical = 0
        opponent.center = (10, screen_height/2)
        player.center = (screen_width - 15, screen_height/2)
    else:
        ball_speed_horizontal = 7 * random.choice((1, -1))
        ball_speed_vertical = 7 * random.choice((1, -1))
        score_time = None


# Setup
pygame.init() 
clock = pygame.time.Clock() 

# Main window setup
screen_width = 1060 
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong") 

# Game Rectangles
ball = pygame.Rect((screen_width/2) - 10, (screen_height/2) - 10, 20, 20) 
player = pygame.Rect((screen_width - 20), (screen_height/2) - 70, 10, 120)
opponent = pygame.Rect(10, (screen_height/2) - 70, 10, 120)

# Drawing color: (r,g,b) or pygame.Color("name")
background_color = pygame.Color("grey12")
light_grey = (200, 200, 200) 

# Defining speed variables to move the bball
ball_speed_horizontal = 7 * random.choice((1, -1))
ball_speed_vertical = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

# Score initalization
player_score = 0
opponent_score = 0
score_time = True

# Font creation for score tab
game_font = pygame.font.Font("freesansbold.ttf", 20)

while True:
    # Handling input
    for event in pygame.event.get():
        # If user clicks the X button, then close the pygame module and close the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Handling player moving their rectangle
        if event.type == pygame.KEYDOWN: # Checks any button is pressed
            if event.key == pygame.K_DOWN: #K_DOWN = down arrow key (Make sure logic follows the desired arrow key)
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP: # Checks any button is pressed
            if event.key == pygame.K_DOWN: #K_DOWN = down arrow key (Make sure logic follows the desired arrow key)
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7



    # Call function to implement ball logic each iteration of loop
    ball_animation()
    player_animation()
    opponent_animation()

    # Visuals: 
    screen.fill(background_color)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height)) 
    pygame.draw.ellipse(screen, (255, 51, 51), ball)  
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)

    # Controlling ball restart
    if score_time: 
        ball_restart()

    # Text Visual for Scoreboard and Timer
    player_text = game_font.render(str(player_score), False, light_grey)
    screen.blit(player_text, (540, 10))
    opponent_text = game_font.render(str(opponent_score), False, light_grey)
    screen.blit(opponent_text, (510, 10))

    # Updating the window
    pygame.display.flip() 
    clock.tick(60) 
