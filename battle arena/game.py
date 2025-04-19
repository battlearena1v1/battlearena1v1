from browser import document, timer

canvas = document["gameCanvas"]
ctx = canvas.getContext("2d")

# Начальное положение квадрата
x = 10
y = 10
speed = 5

# Словарь для отслеживания нажатых клавиш
keys = {}

def key_down(ev):
    keys[ev.key] = True

def key_up(ev):
    keys[ev.key] = False

document.bind("keydown", key_down)
document.bind("keyup", key_up)

def update():
    global x, y
    if keys.get("ArrowRight"):
        x += speed
    if keys.get("ArrowLeft"):
        x -= speed
    if keys.get("ArrowUp"):
        y -= speed
    if keys.get("ArrowDown"):
        y += speed

    # Ограничение движения квадрата в пределах canvas
    if x < 0: 
        x = 0
    if y < 0: 
        y = 0
    if x > canvas.width - 50: 
        x = canvas.width - 50
    if y > canvas.height - 50: 
        y = canvas.height - 50

def draw():
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    ctx.fillStyle = "blue"
    ctx.fillRect(x, y, 50, 50)

def game_loop():
    update()
    draw()

timer.set_interval(game_loop, 30)