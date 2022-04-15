import pygame

# 초기화 (반드시 필요)
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Nado Game')

# 이벤트 루프
running = True # 게임 진행 변수
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 종료 이벤트
            running = False

# pygame 종료
pygame.quit()