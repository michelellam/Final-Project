import pygame
import sys
import random
from src import player
from src import poop
from src import coin
from src import bomb

class Controller:
  def __init__(self):

    '''
    This function sets up the background,sets up the 'state' of the program and initalizes the sprite groups, bomb, player, coin, and poop. 
    args: self (self)
    return:none
    '''

    ################### BACKGROUND ######################
    
    pygame.init()
    pygame.font.init()
    pygame.key.set_repeat(1, 50)
    
    self.window_width = 400
    self.window_height = 600
    self.size = (self.window_width, self.window_height)
    self.screen = pygame.display.set_mode(self.size)
    self.title = pygame.display.set_caption("Welcome to Poop Game")

    self.background = pygame.image.load('assets/background.png')
    self.bgImage = self.background.get_rect()
    self.bgImage = pygame.transform.scale(self.background, (self.window_width, self.window_height))
    self.surface = pygame.display.set_mode((self.size))

    self.state = 'GAME ON'
    self.FPS = 60
    self.fpsclock = pygame.time.Clock() 
    self.score = 0
    self.elist = []
    
    #################### SPRITE GROUP ##########################
    self.sprite = pygame.sprite.Group()
    self.poopGroup = pygame.sprite.Group()
    self.playerGroup = pygame.sprite.Group()
    self.coinGroup = pygame.sprite.Group()
    self.bombGroup = pygame.sprite.Group()

    #################### PLAYER ####################
    self.player = player.Player((self.window_width / 2), 530, 70, 'assets/player.png', self.playerGroup)

    #################### POOP ################################
    self.poop = poop.Poops(random.randint(0, 331), 0,'assets/poop.png', self.poopGroup)

    #################### COIN #################################
    self.coin = coin.Coin(random.randint(0, 331), -80, 'assets/coin.png', self.sprite)

    #################### BOMB ##############################
    self.bomb = bomb.Bomb(random.randint(0,331), -80, 'assets/bomb.png', self.sprite)

  def mainLoop(self):
    '''
    This loops all the events of the game and constantly updating the frames. 
    args: self (self)
    return: none
    '''
    while True:
      if(self.state == 'GAME ON'):
        self.gameLoop()
      elif(self.state == 'GAMEOVER'):
        self.gameOver()
    
  def gameLoop(self):
    '''
    This function basically loops everything that is happening the game, until the player collides with the poop. It holds on the user-events, key events, the falling events,displaying the score, and it updates the screen. It will keep looping until the player collides with the poop object, which will go to the gameOver function. 
    args: self (self)
    return: none
    '''
    
    ####################### USEREVENT ###########################
    coin_fall = pygame.USEREVENT
    pygame.time.set_timer(coin_fall, 15000)
    
    bomb_fall = pygame.USEREVENT + 1
    pygame.time.set_timer(bomb_fall, 12000)

    score_increase = pygame.USEREVENT + 2
    pygame.time.set_timer(score_increase, 1000)

    while (self.state == 'GAME ON'):
    
      ###################### POOP FALLS ########################
      self.poop.poopFall()
      if self.poop.rect.y > self.window_height:
        self.poop.rect.y = 0
        self.poop.rect.x = random.randint(0, 330)
      self.poop.update()

      ###################### KEY ##############################
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.quit
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
            if self.player.rect.x <= 0:
              self.player.rect.x == 0
            else:
              self.player.moveLeft()
          if event.key == pygame.K_RIGHT:
            if self.player.rect.x >= self.window_width - 70:
              self.player.rect.x == self.window_width - 70
            else:
              self.player.moveRight()
              
        ########################## SCORE #########################
        if event.type == score_increase:
            self.score += 1
            self.elist.append(self.score)
              
        ###################### COIN FALLS ########################
        if event.type == coin_fall:
          self.coin.coinFall()
          self.coinGroup.add(coin.Coin(random.randint(0, 331), 80, 'assets/coin.png', self.sprite))

        ###################### BOMB FALLS ########################
        if event.type == bomb_fall:
          self.bomb.bombFall()
          self.bombGroup.add(bomb.Bomb(random.randint(0, 331), 70, 'assets/bomb.png', self.sprite))

      ###################### COIN FALLS ##########################
      for i in self.coinGroup:
        if self.coin.rect.y > self.window_height: 
          i.kill()
      self.coinGroup.update()

      ###################### BOMB FALLS ##########################
      for a in self.bombGroup:
        if self.bomb.rect.y > self.window_height:
          a.kill()
      self.bombGroup.update()
      
      ###################### COLLISION ###########################
      collides_poop = pygame.sprite.spritecollide(self.player, self.poopGroup, True)

      collides_coin = pygame.sprite.spritecollide(self.player, self.coinGroup, True)

      collides_bomb = pygame.sprite.spritecollide(self.player, self.bombGroup, True )

      #################### COLLISION W POOP ######################
      if collides_poop:
        self.state = 'GAMEOVER' 

      #################### COLLIDES W COIN #######################
      self.coin.coin_Message()
          
      if collides_coin:
        self.player.speedUp()
        self.coin.clock.tick()
        self.coin.coin_collide_msg_time = 5000
        self.coin.coin_collide_msg = True

      ################### COLLIDES W BOMB #########################
      self.bomb.bomb_Message()

      if collides_bomb:
        self.player.speedDown()
        self.bomb.clock.tick()
        self.bomb.bomb_collide_msg_time = 5000
        self.bomb.bomb_collide_msg = True

      #################### CANCELS MESSAGE ########################
      if self.bomb.bomb_collide_msg == True and self.coin.coin_collide_msg == True:
        self.bomb.bomb_collide_msg = False
        self.coin.coin_collide_msg = False

      ###################### REDUCE SPEED ########################
      if self.player.speed > self.player.orgSpeed:
        if len(self.elist) % 15 == 10: 
          self.player.speedDown()

      elif self.player.speed < self.player.orgSpeed:
        if len(self.elist) % 12 == 10:
          self.player.speedUp()

      ########################## SCREEN UPDATE ###################
      self.surface.blit(self.bgImage, (0, 0))
      if self.coin.coin_collide_msg == True:
        self.screen.blit(self.coin.coinmsg, (self.window_width/2, self.window_height/2))

      if self.bomb.bomb_collide_msg:
        self.screen.blit(self.bomb.bombmsg, (self.window_width/2, self.window_height/2))
      
      score_font = pygame.font.SysFont(None, 30)
      self.score_message = score_font.render('Score: '+ str(self.score), False, (0, 0, 0))
      self.screen.blit(self.score_message, (10, 100))
  
      self.poopGroup.draw(self.screen)
      self.playerGroup.draw(self.screen)
      self.coinGroup.draw(self.screen)
      self.bombGroup.draw(self.screen)
      pygame.display.update()
      self.fpsclock.tick(self.FPS)

  def gameOver(self):
    '''
    This function will only occur once the player collides the poop object. This will display a black screen saying 'GAME OVER' and also displays the score.
    args: self (self)
    return: none
    '''
    self.screen.fill((0, 0, 0))
    self.player.kill()

    myfont = pygame.font.SysFont(None, 60)
    text = myfont.render('Game Over', False, (250, 0, 0))
    text_rect = text.get_rect(center = (self.window_width/2, self.window_height/2))
    self.screen.blit(text, text_rect)

    score_display = pygame.font.SysFont(None,30)
    score_board = score_display.render('Score: '+ str(self.score),  False, (250, 250, 250))
    
    score_board_rect = score_board.get_rect(center =(self.window_width/2, self.window_height/3))
    self.screen.blit(score_board, score_board_rect)
    pygame.display.update()

    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()