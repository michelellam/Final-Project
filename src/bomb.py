import pygame

class Bomb(pygame.sprite.Sprite):

  def __init__(self, x, y, img, *grps):
    '''
    This function will set up the position and the image of the bomb picture. 
    args: self (self), x (int), y(int), img(file), *grps (pygame.sprite.group)
    return: none
    '''
    super().__init__(*grps)
    self.image = pygame.image.load(img)
    self.image = pygame.transform.scale(self.image, (70, 85))
    self.rect = self.image.get_rect()
    self.rect.move_ip 
    self.rect.x = x
    self.rect.y = y
    self.speed = 3
    self.msgFont = pygame.font.SysFont(None, 30)
    self.bombmsg = self.msgFont.render('SPEED DOWN!', False, (0, 0, 250))
    self.bomb_collide_msg = False
    self.bomb_collide_msg_time = 0
    self.clock = pygame.time.Clock()

  def bombFall(self):
    '''
    This function will make the bomb fall. 
    args: self(self)
    return:none
    '''
    self.rect.y += self.speed

  def update(self):
    '''
    This is the update function which will make the bomb seem like its falling by each frame. 
    args: self(self)
    return:none
    '''
    self.bombFall()

  def bomb_Message(self):
    '''
    This function will count the seconds of the bomb message, which will only display when the player and the bomb collides and will only display for 5 seconds, and when the 5 seconds are up, it will disappear. 
    args: (self)
    return: none
    '''
    if self.bomb_collide_msg_time:
      self.bomb_collide_msg_time -= self.clock.tick()
      if self.bomb_collide_msg_time <= 0:
        self.bomb_collide_msg_time = 0
        self.bomb_collide_msg = False
