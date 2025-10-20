# Fun fact: Do you know that HTML is HyperText Marker Language?
import pygame
import sys

pygame.init()

# Extended color
COLOR_MAP = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "orange": (255, 165, 0),
    "lime": (0, 255, 128),
    "violet": (128, 0, 255),
    "gray": (128, 128, 128),
    "grey": (128, 128, 128),
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "brown": (139, 69, 19),
    "pink": (255, 105, 180),
    "purple": (160, 32, 240),
    "dark gray": (100, 100, 100),
    "dark grey": (100, 100, 100),
}


def parse_color(value):
    """Chuyển chuỗi màu hoặc mã hex thành RGB"""
    value = value.strip().lower()
    if value.startswith("#") and len(value) == 7:
        try:
            r = int(value[1:3], 16)
            g = int(value[3:5], 16)
            b = int(value[5:7], 16)
            return (r, g, b)
        except:
            return (255, 255, 255)
    return COLOR_MAP.get(value, (255, 255, 255))  # mặc định là trắng

#HTML font
def draw_text(screen, text, tag, color=(255, 255, 255), y_offset=0):
    """Vẽ text với kiểu h1, h2, h3"""
    if tag == "h1":
        font = pygame.font.SysFont("arial", 64, bold=True)
    elif tag == "h2":
        font = pygame.font.SysFont("arial", 48, bold=True)
    elif tag == "h3":
        font = pygame.font.SysFont("arial", 36)
    else:
        font = pygame.font.SysFont("arial", 28)

    render = font.render(text, True, color)
    rect = render.get_rect(center=(screen.get_width() // 2, y_offset))
    screen.blit(render, rect)

# main interpreter
def start(input_interpreter):
    """Chạy nội dung webx"""
    lines = input_interpreter.strip().split("\n")

    bg_color = (255, 255, 255)
    texts = []

    for line in lines:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip().lower()
        value = value.strip()

        if key == "bg":
            bg_color = parse_color(value)
        elif key in ("h1", "h2", "h3"):
            texts.append((key, value))

    # Create window
    WIDTH, HEIGHT = 1600, 900
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("WebX Interpreter")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                print(f"Window size: {event.w}x{event.h}")

        screen.fill(bg_color)

        # Vẽ từng đoạn text theo thứ tự
        y = 150
        for tag, content in texts:
            draw_text(screen, content, tag, (255, 255, 255), y_offset=y)
            y += 150

        pygame.display.flip()

    pygame.quit()
    sys.exit()
