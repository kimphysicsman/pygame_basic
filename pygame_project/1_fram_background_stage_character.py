import pygame
import os

##########################################################
# 초기화 (반드시 필요)
pygame.init()

# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Nado Pang')

# FPS
clock = pygame.time.Clock()
##########################################################

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__)    # 현재 파일 위치 반환
images_path = os.path.join(current_path, 'images')

# 배경
background = pygame.image.load(os.path.join(images_path, 'background.png'))

# 스페이지
stage = pygame.image.load(os.path.join(images_path, 'stage.png'))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터
character = pygame.image.load(os.path.join(images_path, 'character.png'))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height - stage_height




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
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 게임 화면 업데이트

# 종료시 2초 대기후 종료
pygame.time.delay(2000)

# pygame 종료
pygame.quit()
