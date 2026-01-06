import pygame
import math

pygame.init()

WIDTH, HEIGHT = 900, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multi-Vector Tool")

clock = pygame.time.Clock()

# ---------------------------------------
# Vector Class
# ---------------------------------------
class VectorObject:
    def __init__(self, origin, vector, color):
        self.origin = origin
        self.vector = vector
        self.color = color
        self.dragging_vector = False
        self.dragging_arrow = False
        self.offset = pygame.Vector2(0, 0)

    def screen_endpoint(self):
        return pygame.Vector2(
            self.origin.x + self.vector.x,
            self.origin.y - self.vector.y
        )

    def draw_arrowhead(self, start, end, size=12):
        direction = (end - start).normalize()
        left = direction.rotate(30) * size
        right = direction.rotate(-30) * size
        pygame.draw.polygon(screen, self.color, [end, end - left, end - right])

    def point_near_line(self, pt, threshold=8):
        start = self.origin
        end = self.screen_endpoint()
        line_vec = end - start
        pt_vec = pt - start
        length = line_vec.length()

        if length == 0:
            return False

        proj = pt_vec.dot(line_vec.normalize())
        if proj < 0 or proj > length:
            return False

        closest = start + line_vec.normalize() * proj
        return pt.distance_to(closest) < threshold

    def point_near_arrow(self, pt, threshold=16):
        return pt.distance_to(self.screen_endpoint()) < threshold

    def update_drag(self, mouse_pos):
        if self.dragging_vector:
            self.origin = mouse_pos - self.offset

        if self.dragging_arrow:
            self.vector.x = mouse_pos.x - self.origin.x
            self.vector.y = self.origin.y - mouse_pos.y  # invert y for math coords

    def draw(self):
        endpoint = self.screen_endpoint()
        pygame.draw.line(screen, self.color, self.origin, endpoint, 4)
        self.draw_arrowhead(self.origin, endpoint)


# ---------------------------------------
# Buttons
# ---------------------------------------
button_add = pygame.Rect(20, 20, 160, 40)
button_add_typed = pygame.Rect(200, 20, 200, 40)

def draw_buttons():
    pygame.draw.rect(screen, (80, 80, 80), button_add)
    pygame.draw.rect(screen, (200, 200, 200), button_add, 2)
    pygame.draw.rect(screen, (80, 80, 80), button_add_typed)
    pygame.draw.rect(screen, (200, 200, 200), button_add_typed, 2)

    font = pygame.font.SysFont(None, 28)
    screen.blit(font.render("Add Vector", True, (255, 255, 255)), (button_add.x + 20, button_add.y + 8))
    screen.blit(font.render("Add Typed Vector", True, (255, 255, 255)), (button_add_typed.x + 10, button_add_typed.y + 8))


# ---------------------------------------
# Vector List + Colors
# ---------------------------------------
color_cycle = [
    (0, 200, 255),
    (255, 120, 120),
    (120, 255, 120),
    (255, 255, 120),
    (255, 150, 255),
    (255, 180, 80)
]

vectors = []
color_index = 0

def add_vector():
    global color_index
    origin = pygame.Vector2(WIDTH // 2, HEIGHT // 2)
    vector = pygame.Vector2(150, 80)
    color = color_cycle[color_index % len(color_cycle)]
    color_index += 1
    vectors.append(VectorObject(origin, vector, color))

def add_vector_typed(x, y):
    global color_index
    origin = pygame.Vector2(WIDTH // 2, HEIGHT // 2)

    # Scale typed values ×10 so display matches input
    vector = pygame.Vector2(x * 10, y * 10)

    color = color_cycle[color_index % len(color_cycle)]
    color_index += 1
    vectors.append(VectorObject(origin, vector, color))


# Start with one vector
add_vector()


# ---------------------------------------
# Text Input Mode
# ---------------------------------------
typing_mode = False
typed_text = ""

def draw_typing_box():
    pygame.draw.rect(screen, (50, 50, 50), (20, HEIGHT - 60, 400, 40))
    pygame.draw.rect(screen, (200, 200, 200), (20, HEIGHT - 60, 400, 40), 2)

    font = pygame.font.SysFont(None, 28)
    screen.blit(font.render("Enter x,y: " + typed_text, True, (255, 255, 255)), (30, HEIGHT - 52))


# ---------------------------------------
# Draw vector info in top-right
# ---------------------------------------
def draw_vector_info():
    font = pygame.font.SysFont(None, 26)
    x = WIDTH - 260
    y = 20

    for v in vectors:
        scaled_x = v.vector.x / 10
        scaled_y = v.vector.y / 10
        scaled_mag = v.vector.length() / 10

        text = font.render(
            f"({scaled_x:.1f}, {scaled_y:.1f}) | {scaled_mag:.1f}",
            True,
            v.color
        )
        screen.blit(text, (x, y))
        y += 28


# ---------------------------------------
# Main Loop
# ---------------------------------------
running = True
while running:
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle typing mode
        if typing_mode:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        x_str, y_str = typed_text.split(",")
                        add_vector_typed(float(x_str), float(y_str))
                    except:
                        pass
                    typed_text = ""
                    typing_mode = False

                elif event.key == pygame.K_BACKSPACE:
                    typed_text = typed_text[:-1]
                else:
                    typed_text += event.unicode
            continue

        # Button clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_add.collidepoint(event.pos):
                add_vector()
                continue

            if button_add_typed.collidepoint(event.pos):
                typing_mode = True
                typed_text = ""
                continue

            # Check vectors (topmost first)
            for v in reversed(vectors):
                if v.point_near_arrow(mouse_pos):
                    v.dragging_arrow = True
                    break
                elif v.point_near_line(mouse_pos):
                    v.dragging_vector = True
                    v.offset = mouse_pos - v.origin
                    break

        if event.type == pygame.MOUSEBUTTONUP:
            for v in vectors:
                v.dragging_vector = False
                v.dragging_arrow = False

    # Update dragging
    for v in vectors:
        v.update_drag(mouse_pos)

    # ---------------------------------------
    # Drawing
    # ---------------------------------------
    screen.fill((30, 30, 30))

    draw_buttons()

    for v in vectors:
        v.draw()

    draw_vector_info()

    if typing_mode:
        draw_typing_box()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
