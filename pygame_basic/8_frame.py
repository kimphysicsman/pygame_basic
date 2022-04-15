import pygame

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

# 배경 이미지 불러오기
background = pygame.image.load('C:/Users/Dongwoo Kim/Desktop/내일배움캠프/사전과제/오락실게임/background.png')

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load('C:/Users/Dongwoo Kim/Desktop/내일배움캠프/사전과제/오락실게임/character.png')
character_size = character.get_rect().size   # 이미지 크기 가져오기
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적
# 캐릭터(스프라이트) 불러오기
enemy = pygame.image.load('C:/Users/Dongwoo Kim/Desktop/내일배움캠프/사전과제/오락실게임/enemy.png')
enemy_size = enemy.get_rect().size   # 이미지 크기 가져오기
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = screen_width / 2 - enemy_width / 2
enemy_y_pos = screen_height / 2 - enemy_height / 2

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 10

# 시작 시간 정보
start_ticks = pygame.time.get_ticks()


# 이벤트 루프
running = True   # 게임 진행 변수
while running:
    dt = clock.tick(60) # 초당 프레임수

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # 종료 이벤트
            running = False

        if event.type == pygame.KEYDOWN: # key 눌린 이벤트
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # charactoer의 위치
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # screen 안에 character 가두기
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 확인
    if character_rect.colliderect(enemy_rect):
        print('충돌!!')
        running = False


    # screen.fill((0, 0, 255))
    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 그리기

    # 타이머
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))
    if total_time - elapsed_time <= 0:
        print("시간 초과!!")
        running = False


    pygame.display.update() # 게임 화면 업데이트

# 종료시 2초 대기후 종료
pygame.time.delay(2000)

# pygame 종료
pygame.quit()
