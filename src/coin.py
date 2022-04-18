import pygame

class Coin(pygame.sprite.Sprite):

  def __init__(self, x, y, img, *grps):
    '''
    This function will set up the position and the image of the coin. 
    args: self (self), x(int), y(int), *grps (pygame.sprite.Group)
    return: none
    '''
    super().__init__(*grps)
    self.image = pygame.image.load(img)
    self.image = pygame.transform.scale(self.image, (70, 80))
    self.rect = self.image.get_rect()
    self.rect.move_ip 
    self.rect.x = x
    self.rect.y = y 
    self.speed = 3
    self.msgFont = pygame.font.SysFont(None, 30)
    self.coinmsg = self.msgFont.render('SPEED UP!', False, (250, 0, 0))
    self.coin_collide_msg = False
    self.coin_collide_msg_time = 0
    self.clock = pygame.time.Clock()

  def coinFall(self):
    '''
    This function makes the coin fall by
    args: self (self) 
    return: None
    '''
    self.rect.y += self.speed

  def update(self):
    '''
    This function updates coinFall function
    args: self(self)
    return: None
    '''
    self.coinFall()

  def coin_Message(self):
    '''
    This function will display a message when the player and the coin collides, and it will only last for 5 seconds. After 5 seconds, the message will be gone. 
    args: self (self)
    return: none
    '''
    if self.coin_collide_msg_time:
      self.coin_collide_msg_time -= self.clock.tick()
      if self.coin_collide_msg_time <= 0:
        self.coin_collide_msg_time = 0
        self.coin_collide_msg = False