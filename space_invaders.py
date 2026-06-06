import pygame
import random
import sys
import math

# 1. Initialisatie
pygame.init()

# Scherminstellingen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders Clustered")

# Kleuren
BLACK = (10, 10, 15)
WHITE = (255, 255, 255)
GREEN = (50, 220, 90)
RED = (255, 60, 60)
YELLOW = (255, 220, 0)
PURPLE = (155, 50, 255)

# Klok & FPS
clock = pygame.time.Clock()
FPS = 60

# --- DRAW FUNCTIES VOOR MOOIE SPRITES ---
def draw_player(surface, x, y):
    # Ruimteschip van de speler (Groen, futuristisch)
    pygame.draw.rect(surface, GREEN, (x + 18, y, 14, 10)) # Loop
    pygame.draw.rect(surface, GREEN, (x + 5, y + 10, 40, 15), border_radius=4) # Body
    pygame.draw.rect(surface, GREEN, (x, y + 20, 50, 15), border_radius=4) # Vleugels
    pygame.draw.rect(surface, RED, (x + 10, y + 22, 6, 6)) # Lichten
    pygame.draw.rect(surface, RED, (x + 34, y + 22, 6, 6))

def draw_alien(surface, x, y, alien_type):
    # Verschillende soorten aliens op basis van hun rij
    if alien_type == 0: # Top rij: Paarse "Crab"
        pygame.draw.rect(surface, PURPLE, (x + 10, y, 20, 25), border_radius=5)
        pygame.draw.rect(surface, PURPLE, (x, y + 8, 40, 10))
        pygame.draw.rect(surface, WHITE, (x + 8, y + 6, 6, 6)) # Ogen
        pygame.draw.rect(surface, WHITE, (x + 26, y + 6, 6, 6))
    elif alien_type == 1: # Middelste rij: Rode "Octopus"
        pygame.draw.circle(surface, RED, (x + 20, y + 15), 18)
        pygame.draw.rect(surface, RED, (x + 5, y + 15, 30, 15))
        pygame.draw.rect(surface, WHITE, (x + 10, y + 10, 6, 6))
        pygame.draw.rect(surface, WHITE, (x + 24, y + 10, 6, 6))
    else: # Onderste rij: Gele "Squid"
        pygame.draw.polygon(surface, YELLOW, [(x+20, y), (x, y+25), (x+40, y+25)])
        pygame.draw.rect(surface, WHITE, (x + 12, y + 14, 5, 5))
        pygame.draw.rect(surface, WHITE, (x + 23, y + 14, 5, 5))

# 2. Spelklassen
class Laser:
    def __init__(self, x, y, direction, speed, color):
        self.rect = pygame.Rect(x, y, 4, 15)
        self.direction = direction # -1 voor omhoog (speler), 1 voor omlaag (alien)
        self.speed = speed
        self.color = color

    def move(self):
        self.rect.y += self.direction * self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=2)

class Alien:
    def __init__(self, x, y, alien_type):
        self.rect = pygame.Rect(x, y, 40, 30)
        self.alien_type = alien_type

    def draw(self, surface):
        draw_alien(surface, self.rect.x, self.rect.y, self.alien_type)

# 3. Spel Initialisatie / Reset Functie
def reset_game():
    global player_x, player_y, player_speed, lasers, alien_lasers, aliens, alien_direction, alien_speed, alien_drop, score, lives, game_over
    player_x = SCREEN_WIDTH // 2 - 25
    player_y = SCREEN_HEIGHT - 60
    player_speed = 6
    
    lasers = []
    alien_lasers = []
    aliens = []
    
    # Maak het grid van aliens (5 rijen, 10 kolommen)
    for row in range(5):
        for col in range(10):
            alien_type = 0 if row == 0 else (1 if row < 3 else 2)
            x = 80 + col * 60
            y = 80 + row * 45
            aliens.append(Alien(x, y, alien_type))
            
    alien_direction = 1 # 1 = Rechts, -1 = Links
    alien_speed = 1.5
    alien_drop = 15
    
    score = 0
    lives = 3
    game_over = False

# Start het spel voor de eerste keer
reset_game()
font = pygame.font.SysFont("Impact", 24)
large_font = pygame.font.SysFont("Impact", 50)

# Sterrenhemel op de achtergrond genereren
stars = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(50)]

# 4. Main Game Loop
running = True
while running:
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN and not game_over:
            # Schieten met Spatbalk (maximaal 3 lasers tegelijk op het scherm)
            if event.key == pygame.K_SPACE and len(lasers) < 3:
                lasers.append(Laser(player_x + 23, player_y, -1, 8, GREEN))

    if not game_over:
        # Besturing Speler
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 10:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - 60:
            player_x += player_speed

        # --- LASERS BEWEGEN ---
        for laser in lasers[:]:
            laser.move()
            if laser.rect.y < 0:
                lasers.remove(laser)

        for a_laser in alien_lasers[:]:
            a_laser.move()
            if a_laser.rect.y > SCREEN_HEIGHT:
                alien_lasers.remove(a_laser)

        # --- ALIENS BEWEGEN ---
        move_down = False
        for alien in aliens:
            alien.rect.x += alien_direction * alien_speed
            # Check of de rand wordt geraakt
            if alien.rect.right >= SCREEN_WIDTH - 10 or alien.rect.left <= 10:
                move_down = True

        if move_down:
            alien_direction *= -1
            for alien in aliens:
                alien.rect.y += alien_drop
                # Als een alien de grond raakt -> Game Over
                if alien.rect.bottom >= player_y:
                    game_over = True

        # --- ALIEN SCHIETEN ---
        # Willekeurige alien schiet soms een laser af
        if aliens and random.random() < 0.02 and len(alien_lasers) < 4:
            shooting_alien = random.choice(aliens)
            alien_lasers.append(Laser(shooting_alien.rect.x + 20, shooting_alien.rect.bottom, 1, 5, RED))

        # --- COLLISION DETECTION (BOTSINGEN) ---
        # Speler laser raakt Alien
        for laser in lasers[:]:
            for alien in aliens[:]:
                if laser.rect.colliderect(alien.rect):
                    if laser in lasers:
                        lasers.remove(laser)
                    aliens.remove(alien)
                    score += 10 * (alien.alien_type + 1) # Meer punten voor hogere aliens
                    break

        # Alien laser raakt Speler
        player_rect = pygame.Rect(player_x, player_y, 50, 35)
        for a_laser in alien_lasers[:]:
            if a_laser.rect.colliderect(player_rect):
                alien_lasers.remove(a_laser)
                lives -= 1
                if lives <= 0:
                    game_over = True

        # Check of alle aliens dood zijn (Winst!)
        if not aliens:
            # Spawn een nieuwe, snellere wave
            reset_game()
            alien_speed += 0.5 

    # 5. TEKENEN
    screen.fill(BLACK)
    
    # Teken sterrenhemel background
    for star in stars:
        pygame.draw.circle(screen, (100, 100, 100), star, 1)

    if not game_over:
        # Teken Speler
        draw_player(screen, player_x, player_y)

        # Teken Aliens
        for alien in aliens:
            alien.draw(screen)

        # Teken Lasers
        for laser in lasers:
            laser.draw(screen)
        for a_laser in alien_lasers:
            a_laser.draw(screen)

        # UI: Score en Levens
        score_text = font.render(f"SCORE: {score}", True, WHITE)
        screen.blit(score_text, (20, 20))
        
        for i in range(lives):
            draw_player(screen, SCREEN_WIDTH - 180 + (i * 55), 15)
    else:
        # Game Over Scherm
        go_text = large_font.render("GAME OVER", True, RED)
        score_txt = font.render(f"Eindscore: {score}", True, WHITE)
        restart_txt = font.render("Druk op SPATIE om opnieuw te starten", True, GREEN)
        
        screen.blit(go_text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 - 60))
        screen.blit(score_txt, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 10))
        screen.blit(restart_txt, (SCREEN_WIDTH // 2 - 160, SCREEN_HEIGHT // 2 + 50))

        # Herstart logica
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            reset_game()

    pygame.display.flip()
    clock.tick(FPS)