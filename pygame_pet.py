import pygame
import sys
import os
from pet_logic import Dog, Cat, Hamster

# TODO:
# 1. Make significant changes to the code below
# 2. Add comments to explain what you did
#---------- Comments here ----------#
#
#
#
#-----------------------------------#
# 3. Have fun with your pet!


# --- Setup ---
pygame.init()
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.SysFont(None, 32)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Virtual Pet Game")
clock = pygame.time.Clock()

# --- Image Loader  ---
def load_image(name, size):
    path = os.path.join("assets", name)
    img = pygame.image.load(path)
    return pygame.transform.scale(img, size)


images = {
    "dog": load_image("dog.png", (200, 200)),
    "cat": load_image("cat.png", (200, 200)),
    "hamster": load_image("hamster.png", (150, 150)),
    "heart": load_image("heart.png", (32, 32)),
    "food": load_image("food.png", (32, 32)),
}

# --- Button Class ---
class Button:
    def __init__(self, text, x, y, callback):
        self.rect = pygame.Rect(x, y, 150, 40)
        self.text = text
        self.callback = callback

    def draw(self):
        pygame.draw.rect(screen, (200, 200, 255), self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        label = FONT.render(self.text, True, BLACK)
        screen.blit(label, (self.rect.x + 10, self.rect.y + 8))

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.callback()

pet = None
feedback = ""


# --- Game Actions ---
def feed_pet():
    global feedback
    pet.feed()
    feedback = f"You fed {pet.name}!"

def play_with_pet():
    global feedback
    pet.play()
    feedback = f"You played with {pet.name}!"

def wait_pet():
    global feedback
    pet.tick()
    feedback = f"Time passed for {pet.name}."

# --- UI Drawing ---
def draw_status():
    screen.blit(FONT.render(f"{pet.name} the {pet.species}", True, BLACK), (30, 30))
    screen.blit(images["food"], (30, 70))
    pygame.draw.rect(screen, (255, 100, 100), pygame.Rect(75, 75, pet.hunger * 20, 20))
    screen.blit(images["heart"], (30, 120))
    pygame.draw.rect(screen, (100, 200, 255), pygame.Rect(75, 125, pet.happiness * 20, 20))
    screen.blit(FONT.render(feedback, True, BLACK), (30, 170))

# --- Pet Selection ---
def choose_pet():
    global pet
    name = ""
    input_box = pygame.Rect(200, 200, 400, 40)
    color = pygame.Color("dodgerblue2")

    def set_dog():
        global pet
        pet = Dog(name)

    def set_cat():
        global pet
        pet = Cat(name)

    def set_hamster():
        global pet
        pet = Hamster(name)

    buttons = [
        Button("Dog", 150, 300, set_dog),
        Button("Cat", 325, 300, set_cat),
        Button("Hamster", 500, 300, set_hamster),
    ]

    active = True
    while pet is None:
        screen.fill(WHITE)
        screen.blit(FONT.render("Name your pet and choose its type:", True, BLACK), (200, 150))

        txt_surface = FONT.render(name, True, BLACK)
        input_box.w = max(200, txt_surface.get_width() + 10)
        pygame.draw.rect(screen, color, input_box, 2)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        for btn in buttons:
            btn.draw()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                for btn in buttons:
                    if name:
                        btn.check_click(event.pos)
            elif event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode

# --- Main Game Loop ---
def main():
    global pet
    choose_pet()

    buttons = [
        Button("Feed", 600, 100, feed_pet),
        Button("Play", 600, 160, play_with_pet),
        Button("Wait", 600, 220, wait_pet),
    ]

    while True:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for btn in buttons:
                    btn.check_click(event.pos)

        if pet:
            screen.blit(images[pet.species], (280, 230))
            draw_status()

        for btn in buttons:
            btn.draw()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
