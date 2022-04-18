import pygame 

class Player(pygame.sprite.Sprite):

  def __init__(self, x, y, sz, img, *grps):
    '''
    This function will set up the position and the image of our player. 
    args: self (self), x(int), y(int), sz(int), img (file), *grps (pygame.sprite.Group)
    return: none
    '''
    super().__init__(*grps)
    self.image = pygame.image.load(img)
    self.image = pygame.transform.scale(self.image, (sz, sz))
    self.rect = self.image.get_rect()
    self.rect.move_ip
    self.rect.x = x - (sz / 2)
    self.rect.y = y
    self.speed = 5
    self.orgSpeed = self.speed
    self.changeSpeed = 3

  def moveLeft(self):
    '''
    Makes player move left
    args: self (self)
    return: none
    '''
    self.rect.x -= self.speed

  def moveRight(self):
    '''
    Makes player move right
    args: self (self)
    return: none
    '''
    self.rect.x += self.speed

  def speedUp(self):
    '''
    Increases the speed of the player
    args: self (self)
    return: none
    '''
    self.speed += self.changeSpeed

  def speedDown(self):
    '''
    Decreases the speed of the player
    args: self (self)
    return: none
    '''
    self.speed -= self.changeSpeed