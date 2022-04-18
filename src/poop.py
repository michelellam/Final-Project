import pygame

class Poops(pygame.sprite.Sprite):

  def __init__(self, x, y, img, *grps):
    '''
    This function will set up the starting position and the image of the poop. 
    args: self (self), x(int), y(int), img(file), *grps (pygame.sprite.Sprite)
    return: none
    '''
    super().__init__(*grps)
    self.image = pygame.image.load(img)
    self.image = pygame.transform.scale(self.image, (70, 70))
    self.rect = self.image.get_rect()
    self.rect.move_ip
    self.rect.x = x
    self.rect.y = y 
    self.speed = 3

  def poopFall(self):
    '''
    This function will make the poop fall. 
    args: self (self)
    return: none
    '''
    self.rect.y += self.speed

  def update(self):
    '''
    This function will make the poop fall every frame. 
    args: self (self)
    return:none
    '''
    self.poopFall()