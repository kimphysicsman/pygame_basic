import pygame

##########################################################
# 초기화 (반드시 필요)
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Nado Game')

# FPS
clock = pygame.time.Clock()
##########################################################

# 1. 사용자 게임 초기화

# 이벤트 루프
running = True   # 게임 진행 변수
while running:
    dt = clock.tick(60) # 초당 프레임수

    # 2. 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # 종료 이벤트
            running = False

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기

    pygame.display.update() # 게임 화면 업데이트

# 종료시 2초 대기후 종료
pygame.time.delay(2000)

# pygame 종료
pygame.quit()
