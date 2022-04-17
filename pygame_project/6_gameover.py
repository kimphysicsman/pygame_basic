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

character_to_x = 0
character_speed = 0.7

# 무기
weapon = pygame.image.load(os.path.join(images_path, 'weapon.png'))
weapon_size = character.get_rect().size
weapon_width = character_size[0]

weapons = []
weapon_speed = 1

# 공
ball_images = [
    pygame.image.load(os.path.join(images_path, 'ballon1.png')),
    pygame.image.load(os.path.join(images_path, 'ballon2.png')),
    pygame.image.load(os.path.join(images_path, 'ballon3.png')),
    pygame.image.load(os.path.join(images_path, 'ballon4.png'))]

ball_speed_y = [-18, -15, -12, -9]
balls = []

# 최초 시작 공
balls.append({
    'pos_x': 50,
    'pos_y': 50,
    'img_idx': 0,
    'to_x': 1.5,
    'to_y': -6,
    'init_spd_y': ball_speed_y[0]
})

weapon_to_remove = -1
ball_to_remove = -1

# 폰트
game_font = pygame.font.Font(None, 40)
total_time = 100
start_ticks = pygame.time.get_ticks()

# 게임 종료 메시지 - Time out, Game over, Mission complete.
game_result = 'Game over'

# 이벤트 루프
running = True   # 게임 진행 변수
while running:
    dt = clock.tick(60) # 초당 프레임수

    # 2. 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # 종료 이벤트
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed * dt
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed * dt
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = (character_x_pos + character_width / 2 - weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0


    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
         character_x_pos = screen_width - character_width

    weapons = [[w[0], w[1] - weapon_speed * dt] for w in weapons]
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    for ball_idx, ball_val in enumerate(balls):
        ball_x_pos = ball_val['pos_x']
        ball_y_pos = ball_val['pos_y']
        ball_img_idx = ball_val['img_idx']

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        if ball_x_pos <= 0 or ball_x_pos > screen_width - ball_width:
            ball_val['to_x'] = ball_val['to_x'] * -1
        if ball_y_pos >= screen_height - stage_height - ball_height:
            ball_val['to_y'] = ball_val['init_spd_y']
        else:
            ball_val['to_y'] += 0.02 * dt
        ball_val['pos_x'] += ball_val['to_x']
        ball_val['pos_y'] += ball_val['to_y']

    # 4. 충돌 처리

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for idx, val in enumerate(balls):
        ball_x_pos = val['pos_x']
        ball_y_pos = val['pos_y']
        ball_img_idx = val['img_idx']

        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_x_pos
        ball_rect.top = ball_y_pos

        if character_rect.colliderect(ball_rect):
            running = False
            break

        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx
                ball_to_remove = idx

                if ball_img_idx < 3:
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    balls.append({
                        'pos_x': ball_x_pos + ball_width / 2 - small_ball_width / 2,
                        'pos_y': ball_y_pos + ball_height / 2 - small_ball_height / 2,
                        'img_idx': ball_img_idx + 1,
                        'to_x': -1.5,
                        'to_y': -6,
                        'init_spd_y': ball_speed_y[ball_img_idx + 1]
                    })

                    balls.append({
                        'pos_x': ball_x_pos + ball_width / 2 - small_ball_width / 2,
                        'pos_y': ball_y_pos + ball_height / 2 - small_ball_height / 2,
                        'img_idx': ball_img_idx + 1,
                        'to_x': 1.5,
                        'to_y': -6,
                        'init_spd_y': ball_speed_y[ball_img_idx + 1]
                    })
                break
        else:
            continue
        break

    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # 모든 공을 없앤 경우
    if len(balls) == 0:
        game_result = 'Mission complete'
        running = False
        break

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    for idx, val in enumerate(balls):
        ball_x_pos = val['pos_x']
        ball_y_pos = val['pos_y']
        ball_img_idx = val['img_idx']
        screen.blit(ball_images[ball_img_idx], (ball_x_pos, ball_y_pos))


    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    # 타이머
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render('Time : {}'.format(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        game_result = 'Time out'
        running = False

    pygame.display.update() # 게임 화면 업데이트

# 게임 결과 출력
msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect = msg.get_rect(center=(int(screen_width/2), int(screen_height/2)))
screen.blit(msg, msg_rect)
pygame.display.update()

# 종료시 2초 대기후 종료
pygame.time.delay(2000)

# pygame 종료
pygame.quit()
