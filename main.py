
# =====================================
# SPACE TREASURE COLLECTOR
# =====================================

# Game variables
shipSpeed = 20

shipHP = 100
maxHP = 100

nextDamageTime = 0
lastDamageTime = 0

healthBarVisible = False
gameEnded = False


# =====================================
# CREATE SPACESHIP
# =====================================

mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . f f . . . . . . .
        . . . . . . f 6 6 f . . . . . .
        . . . . . . f b b f . . . . . .
        . . . . . f b b b b f . . . . .
        . . . . . f b b b b f . . . . .
        . . . . . f b b b b f . . . . .
        . . . . f b b b b b b f . . . .
        . . . . f b b f f b b f . . . .
        . . . . f b f 6 6 f b f . . . .
        . f f f b b f 9 9 f b b f f f .
        f b b b b f 6 9 9 9 f b b b b f
        f b b b b f 9 9 9 9 f b b b b f
        . f f f b b f f f f b b f f f .
        . . . . f b b b b b b f . . . .
        . . . . f f f f f f f f . . . .
        """), SpriteKind.player)


# =====================================
# CREATE TREASURE
# =====================================

treasure = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . f f f f f f f f f f f . .
        . . . f e e e e e e e e e f . .
        . . . f e e e e e e e e e f . .
        . . . f e e e e e e e e e f . .
        . . . f f f f 5 f 5 f f f f . .
        . . . f e e e 5 5 5 e e e f . .
        . . . f e e e e e e e e e f . .
        . . . f e e e e e e e e e f . .
        . . . f e e e e e e e e e f . .
        . . . f f f f f f f f f f f . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        """), SpriteKind.food)

treasure.set_position(randint(8, 152), randint(8, 112))


# =====================================
# HEALTH BAR IMAGE
# =====================================

def make_health_bar_image():
    bar_image = image.create(34, 6)

    bar_image.fill(15)
    bar_image.fill_rect(1, 1, 32, 4, 1)

    bar_width = shipHP * 32 // maxHP

    if shipHP > 60:
        bar_color = 6
    elif shipHP > 30:
        bar_color = 14
    else:
        bar_color = 10

    if bar_width > 0:
        bar_image.fill_rect(1, 1, bar_width, 4, bar_color)

    return bar_image


# =====================================
# CREATE HEALTH BAR SPRITE
# =====================================

health_bar = sprites.create(
    make_health_bar_image(),
    SpriteKind.projectile
)

health_bar.set_flag(SpriteFlag.Ghost, True)
health_bar.set_flag(SpriteFlag.Invisible, True)


# =====================================
# BUTTON CONTROLS
# =====================================

def on_up_pressed():
    if mySprite.vy > -60:
        mySprite.vy += 0 - shipSpeed

controller.up.on_event(
    ControllerButtonEvent.PRESSED,
    on_up_pressed
)


def on_left_pressed():
    if mySprite.vx > -60:
        mySprite.vx += 0 - shipSpeed

controller.left.on_event(
    ControllerButtonEvent.PRESSED,
    on_left_pressed
)


def on_right_pressed():
    if mySprite.vx < 60:
        mySprite.vx += shipSpeed

controller.right.on_event(
    ControllerButtonEvent.PRESSED,
    on_right_pressed
)


def on_down_pressed():
    if mySprite.vy < 60:
        mySprite.vy += shipSpeed

controller.down.on_event(
    ControllerButtonEvent.PRESSED,
    on_down_pressed
)


# =====================================
# TREASURE COLLECTION
# =====================================

def on_treasure_overlap(sprite, otherSprite):
    info.change_score_by(1)

    treasure.set_position(
        randint(8, 152),
        randint(8, 112)
    )

    while mySprite.overlaps_with(treasure):
        treasure.set_position(
            randint(8, 152),
            randint(8, 112)
        )

    music.play(
        music.melody_playable(music.power_up),
        music.PlaybackMode.UNTIL_DONE
    )

sprites.on_overlap(
    SpriteKind.player,
    SpriteKind.food,
    on_treasure_overlap
)


# =====================================
# ASTEROID CREATION
# =====================================

def create_asteroid():
    asteroid = sprites.create(img("""
        . . . . 8 8 8 . . . . . . . .
        . . 8 8 7 7 7 8 . . . . . . .
        . 8 7 7 8 7 7 7 8 . . . . . .
        8 7 7 7 7 7 8 7 7 8 . . . . .
        8 7 8 7 7 7 7 7 7 8 . . . . .
        8 7 7 7 8 7 7 8 7 7 8 . . . .
        . 8 7 7 7 7 7 7 7 8 . . . . .
        . . 8 8 7 7 8 8 8 . . . . . .
        . . . 8 7 7 7 8 . . . . . . .
        . . 8 7 7 8 7 7 8 . . . . . .
        . 8 7 7 7 7 7 7 7 8 . . . . .
        . . 8 8 8 7 8 8 8 . . . . . .
        . . . . 8 8 8 . . . . . . . .
        . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . .
        """), SpriteKind.enemy)

    asteroid.set_position(
        randint(15, 145),
        randint(15, 105)
    )

    asteroid.vx = randint(-35, 35)
    asteroid.vy = randint(-35, 35)

    if asteroid.vx == 0:
        asteroid.vx = 20

    if asteroid.vy == 0:
        asteroid.vy = -20

    asteroid.set_flag(SpriteFlag.BounceOnWall, True)

    return asteroid


# =====================================
# ASTEROID COLLISION AND DAMAGE
# =====================================

def on_asteroid_overlap(sprite, otherSprite):
    global shipHP
    global nextDamageTime
    global lastDamageTime
    global healthBarVisible
    global gameEnded

    if gameEnded == False and game.runtime() >= nextDamageTime:

        shipHP -= 20

        if shipHP < 0:
            shipHP = 0

        lastDamageTime = game.runtime()
        nextDamageTime = lastDamageTime + 1000

        health_bar.set_image(make_health_bar_image())
        health_bar.set_flag(SpriteFlag.Invisible, False)

        healthBarVisible = True

        otherSprite.set_position(
            randint(8, 152),
            randint(8, 112)
        )

        if shipHP <= 0:
            gameEnded = True

            mySprite.vx = 0
            mySprite.vy = 0

            mySprite.start_effect(effects.disintegrate, 500)

            pause(500)

            game.set_game_over_message(
                False,
                "GAME OVER - PRESS A TO RETRY"
            )

            game.game_over(False)


sprites.on_overlap(
    SpriteKind.player,
    SpriteKind.enemy,
    on_asteroid_overlap
)


# =====================================
# CREATE ASTEROIDS
# =====================================

asteroid1 = create_asteroid()
asteroid2 = create_asteroid()
asteroid3 = create_asteroid()


# =====================================
# INITIAL SETTINGS
# =====================================

scene.set_background_color(15)

mySprite.set_stay_in_screen(False)

info.set_score(0)


# =====================================
# MAIN GAME UPDATE
# =====================================

def on_forever():
    global healthBarVisible

    if controller.right.is_pressed():
        mySprite.rotation_degrees = 90
    elif controller.left.is_pressed():
        mySprite.rotation_degrees = -90
    elif controller.down.is_pressed():
        mySprite.rotation_degrees = 180
    elif controller.up.is_pressed():
        mySprite.rotation_degrees = 0

    # Screen wrapping
    if mySprite.x < 0:
        mySprite.x = 160
    elif mySprite.x > 160:
        mySprite.x = 0

    if mySprite.y < 0:
        mySprite.y = 120
    elif mySprite.y > 120:
        mySprite.y = 0

    # Health bar follows spaceship
    health_bar.x = mySprite.x
    health_bar.y = mySprite.y - 15

    # Hide health bar after 3 seconds
    if healthBarVisible:
        if game.runtime() - lastDamageTime >= 3000:
            health_bar.set_flag(SpriteFlag.Invisible, True)
            healthBarVisible = False


game.on_update(on_forever)


# =====================================
# GRADUALLY INCREASE ACCELERATION
# =====================================

def on_forever2():
    global shipSpeed

    if shipSpeed < 60:
        shipSpeed += 1

    pause(500)

forever(on_forever2)
