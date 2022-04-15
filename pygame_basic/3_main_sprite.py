import pygame

# 초기화 (반드시 필요)
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Nado Game')

# 배경 이미지 불러오기
background = pygame.image.load('C:/Users/Dongwoo Kim/Desktop/내일배움캠프/사전과제/오락실게임/background.png')

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load('C:/Users/Dongwoo Kim/Desktop/내일배움캠프/사전과제/오락실게임/character.png')
character_size = character.get_rect().size # 이미지 크기 가져오기
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

# 이벤트 루프
running = True # 게임 진행 변수
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # 종료 이벤트
            running = False

    screen.blit(background, (0, 0))  # 배경 그리기
    # screen.fill((0, 0, 255))

    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기

    pygame.display.update() # 게임 화면 업데이트

# pygame 종료
pygame.quit()