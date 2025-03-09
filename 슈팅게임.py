import pygame
import random

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("space 슈팅 게임")

# 색상
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# 폰트 설정
font = pygame.font.Font(None, 36)

# 플레이어 설정
player_size = (50, 50)
player = pygame.Rect(WIDTH//2, HEIGHT - 80, *player_size)
player_speed = 5

# 총알 설정
bullet_size = (5, 10)
bullets = []
bullet_speed = 7

# 적 설정
enemy_size = (50, 50)
enemies = []
enemy_speed = 3
enemy_spawn_time = 30
enemy_timer = 0

# 점수 시스템
score = 0
score_threshold = 10  # 난이도 증가 기준 점수
level = 1

# 게임 루프
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - player_size[0]:
        player.x += player_speed
    if keys[pygame.K_SPACE]:
        bullets.append(pygame.Rect(player.x + player_size[0]//2, player.y, *bullet_size))
    
    # 총알 이동
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)
    
    # 적 생성
    enemy_timer += 1
    if enemy_timer >= enemy_spawn_time:
        enemies.append(pygame.Rect(random.randint(0, WIDTH - enemy_size[0]), 0, *enemy_size))
        enemy_timer = 0
    
    # 적 이동
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemies.remove(enemy)
    
    # 충돌 감지
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1  # 점수 증가
                if score % score_threshold == 0:  # 난이도 증가 조건
                    level += 1
                    enemy_speed += 1  # 적 속도 증가
                    enemy_spawn_time = max(10, enemy_spawn_time - 5)  # 적 생성 속도 증가
                break
    
    # 점수 표시
    score_text = font.render(f"Score: {score}  Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    # 객체 그리기
    pygame.draw.rect(screen, BLUE, player)
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
