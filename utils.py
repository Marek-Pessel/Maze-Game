import pygame


def event_handler(gui):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left mouse button was clicked
                # get mouse position
                pos = pygame.mouse.get_pos()
                # check mouse was over a button
                for button in gui.buttons:
                    button.check_clicked(pos)
        


def check_finished(player_rect, treasure_rect) -> bool:

    if player_rect.colliderect(treasure_rect):
        return True
    else:
        return False
    
def cought_player(player_rect, enemies) -> bool:
    # are player pos and enemy pos the same?
    for enemy in enemies:
        if player_rect.colliderect(enemy.rect):
            return True
        
    return False