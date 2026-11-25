"""

Asteroid orbit angles

"""
# ==================================================
# PLANET IMAGE GENERATOR
# ==================================================
def make_planet_image(size: number, radius: number, base_color: number, pattern_color: number, highlight_color: number, shadow_color: number, style: number):
    global planet_image, center
    planet_image = image.create(size, size)
    center = Math.idiv(size, 2)
    y = 0
    while y <= size - 1:
        x = 0
        while x <= size - 1:
            dx = x - center
            dy = y - center
            distance_squared = dx * dx + dy * dy
            if distance_squared <= radius * radius:
                color = base_color
                if style == 1:
                    # Ocean and land patterns
                    if (x * 7 + y * 3) % 37 < 11:
                        color = pattern_color
                elif style == 2:
                    # Gas giant bands
                    if y % 11 < 4:
                        color = pattern_color
                elif (x + y * 2) % 23 < 6:
                    color = pattern_color
                # Lit side
                if dx < 0 - Math.idiv(radius, 3) and dy < Math.idiv(radius, 3):
                    color = highlight_color
                elif dx > Math.idiv(radius, 3):
                    # Shadow side
                    color = shadow_color
                planet_image.set_pixel(x, y, color)
            x += 1
        y += 1
    return planet_image
# ==================================================
# ASTEROIDS
# ==================================================
def create_asteroid(variant: number):
    global asteroid
    if variant == 1:
        asteroidImage = img("""
            . . . 8 8 8 . . . . . . . . . . . .
            . . 8 7 7 7 8 8 . . . . . . . . . .
            . 8 7 7 8 7 7 7 8 . . . . . . . . .
            8 7 7 7 7 7 7 7 8 . . . . . . . . .
            8 7 8 7 7 8 7 7 7 8 . . . . . . . .
            . 8 7 7 7 7 7 7 8 . . . . . . . . .
            . . 8 8 7 7 8 8 . . . . . . . . . .
            . . . 8 8 8 8 . . . . . . . . . . .
            """)
    elif variant == 2:
        asteroidImage = img("""
            . . . . 8 8 8 . . . . . . . . .
            . . 8 8 7 7 7 8 8 . . . . . . .
            . 8 7 7 7 8 7 7 7 8 . . . . . .
            8 7 8 7 7 7 7 7 7 8 . . . . . .
            8 7 7 7 7 8 7 7 8 . . . . . . .
            . 8 7 7 7 7 7 7 8 . . . . . . .
            . . 8 8 7 7 8 8 . . . . . . . .
            . . . 8 8 8 8 . . . . . . . . .
            """)
    else:
        asteroidImage = img("""
            . . . . 8 8 . . . . . . . . . . .
            . . 8 8 7 7 8 8 . . . . . . . . .
            . 8 7 7 7 7 7 7 8 . . . . . . . .
            8 7 7 8 7 7 8 7 7 8 . . . . . . .
            8 7 7 7 7 7 7 7 7 8 . . . . . . .
            . 8 7 8 7 7 7 8 7 8 . . . . . . .
            . . 8 7 7 7 7 7 8 . . . . . . . .
            . . . 8 8 8 8 8 . . . . . . . . .
            """)
    asteroid = sprites.create(asteroidImage, SpriteKind.enemy)
    asteroid.z = 20
    return asteroid
# ==================================================
# HEALTH BAR
# ==================================================
def make_health_bar_image():
    global bar_image, bar_width
    bar_image = image.create(34, 6)
    bar_image.fill(15)
    bar_image.fill_rect(1, 1, 32, 4, 1)
    bar_width = Math.idiv(shipHP * 32, maxHP)
    if shipHP > 60:
        bar_color = 6
    elif shipHP > 30:
        bar_color = 14
    else:
        bar_color = 10
    if bar_width > 0:
        bar_image.fill_rect(1, 1, bar_width, 4, bar_color)
    return bar_image
# ==================================================
# SUN IMAGE
# ==================================================
def make_sun_image():
    global size22, center3, sun_image
    size22 = 128
    center3 = 64
    sun_image = image.create(size22, size22)
    y3 = 0
    while y3 <= size22 - 1:
        x3 = 0
        while x3 <= size22 - 1:
            dx3 = x3 - center3
            dy3 = y3 - center3
            distance_squared3 = dx3 * dx3 + dy3 * dy3
            if distance_squared3 <= 61 * 61:
                if distance_squared3 <= 25 * 25:
                    color3 = 5
                elif distance_squared3 <= 43 * 43:
                    color3 = 4
                else:
                    color3 = 2
                if dx3 < -12 and dy3 < -12 and distance_squared3 < 30 * 30:
                    color3 = 14
                if distance_squared3 > 44 * 44 and (x3 * 3 + y3) % 13 < 4:
                    color3 = 5
                sun_image.set_pixel(x3, y3, color3)
            x3 += 1
        y3 += 1
    return sun_image
# ==================================================
# UPDATE THE MINIMAP
# ==================================================
def update_minimap():
    global minimapImage, planet1WorldX, planet1WorldY, planet2WorldX, planet2WorldY, planet3WorldX, planet3WorldY, asteroid1WorldX, asteroid1WorldY, asteroid2WorldX, asteroid2WorldY, asteroid3WorldX, asteroid3WorldY
    minimapImage = image.create(MINIMAP_WIDTH, MINIMAP_HEIGHT)
    y4 = 2
    while y4 < 42:
        x4 = 2
        while x4 < 62:
            if (x4 + y4) % 2 == 0:
                minimapImage.set_pixel(x4, y4, 12)
            x4 += 1
        y4 += 1
    x4 = 0
    while x4 < MINIMAP_WIDTH:
        minimapImage.set_pixel(x4, 0, 6)
        minimapImage.set_pixel(x4, MINIMAP_HEIGHT - 1, 6)
        x4 += 1
    y4 = 0
    while y4 < MINIMAP_HEIGHT:
        minimapImage.set_pixel(0, y4, 6)
        minimapImage.set_pixel(MINIMAP_WIDTH - 1, y4, 6)
        y4 += 1
    # ----------------------------------------------
    # SUN MARKER
    # ----------------------------------------------
    draw_map_marker(minimapImage, starX, starY, 5, 2)
    # ----------------------------------------------
    # PLANET MARKERS
    # ----------------------------------------------
    planet1WorldX = starX + Math.cos(planetAngle1) * planetRadius1
    planet1WorldY = starY + Math.sin(planetAngle1) * planetRadius1
    planet2WorldX = starX + Math.cos(planetAngle2) * planetRadius2
    planet2WorldY = starY + Math.sin(planetAngle2) * planetRadius2
    planet3WorldX = starX + Math.cos(planetAngle3) * planetRadius3
    planet3WorldY = starY + Math.sin(planetAngle3) * planetRadius3
    draw_map_marker(minimapImage, planet1WorldX, planet1WorldY, 8, 1)
    draw_map_marker(minimapImage, planet2WorldX, planet2WorldY, 4, 1)
    draw_map_marker(minimapImage, planet3WorldX, planet3WorldY, 10, 1)
    # ----------------------------------------------
    # ASTEROID MARKERS
    # ----------------------------------------------
    asteroid1WorldX = starX + Math.cos(angle1) * radius1
    asteroid1WorldY = starY + Math.sin(angle1) * radius1
    asteroid2WorldX = starX + Math.cos(angle2) * radius2
    asteroid2WorldY = starY + Math.sin(angle2) * radius2
    asteroid3WorldX = starX + Math.cos(angle3) * radius3
    asteroid3WorldY = starY + Math.sin(angle3) * radius3
    draw_map_marker(minimapImage, asteroid1WorldX, asteroid1WorldY, 13, 0)
    draw_map_marker(minimapImage, asteroid2WorldX, asteroid2WorldY, 13, 0)
    draw_map_marker(minimapImage, asteroid3WorldX, asteroid3WorldY, 13, 0)
    # ----------------------------------------------
    # TREASURE CHEST MARKERS
    # ----------------------------------------------
    j = 0
    while j <= TREASURE_COUNT - 1:
        draw_map_marker(minimapImage, treasureWorldX[j], treasureWorldY[j], 7, 0)
        j += 1
    # ----------------------------------------------
    # PLAYER MARKER
    # ----------------------------------------------
    draw_map_marker(minimapImage, shipWorldX, shipWorldY, 9, 2)
    # Put the updated image on the minimap sprite.
    minimapSprite.set_image(minimapImage)
    minimapSprite.set_position(MINIMAP_SCREEN_X, MINIMAP_SCREEN_Y)
# ==================================================
# RESPAWN TREASURE CHESTS
# ==================================================
def respawn_chest(index: number):
    global candidateX, candidateY, validPosition, attempts
    while validPosition == False and attempts < 100:
        candidateX = randint(150, WORLD_WIDTH - 150)
        candidateY = randint(150, WORLD_HEIGHT - 150)
        validPosition = True
        # Keep the chest away from the ship.
        dxShip = candidateX - shipWorldX
        dyShip = candidateY - shipWorldY
        if dxShip * dxShip + dyShip * dyShip < 350 * 350:
            validPosition = False
        # Keep the chest away from the sun.
        dxSun = candidateX - starX
        dySun = candidateY - starY
        minimumSunDistance = STAR_DEATH_RADIUS + 300
        if dxSun * dxSun + dySun * dySun < minimumSunDistance * minimumSunDistance:
            validPosition = False
        # Keep treasure chests separated.
        k = 0
        while k <= TREASURE_COUNT - 1:
            if k != index:
                dxChest = candidateX - treasureWorldX[k]
                dyChest = candidateY - treasureWorldY[k]
                if dxChest * dxChest + dyChest * dyChest < 300 * 300:
                    validPosition = False
            k += 1
        attempts += 1
    if validPosition == False:
        candidateX = randint(150, WORLD_WIDTH - 150)
        candidateY = randint(150, WORLD_HEIGHT - 150)
    treasureWorldX[index] = candidateX
    treasureWorldY[index] = candidateY
    # Move the chest away immediately.
    treasureSprites[index].set_position(candidateX - shipWorldX + SCREEN_CENTER_X,
        candidateY - shipWorldY + SCREEN_CENTER_Y)
# ==================================================
# TREASURE COLLECTION
# ==================================================

def on_on_overlap(sprite, otherSprite):
    if gameEnded:
        return
    l = 0
    while l <= TREASURE_COUNT - 1:
        if treasureSprites[l] == otherSprite:
            # Award exactly one point.
            info.change_score_by(1)
            # Immediately move this chest elsewhere.
            respawn_chest(l)
            break
        l += 1
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

# ==================================================
# DRAW A MARKER ON THE MINIMAP
# ==================================================
def draw_map_marker(map_image: Image, world_x: number, world_y: number, color2: number, marker_radius: number):
    global map_x, map_y
    # Convert world coordinates into minimap pixels.
    map_x = 2 + Math.round(world_x * 59 / WORLD_WIDTH)
    map_y = 2 + Math.round(world_y * 39 / WORLD_HEIGHT)
    dx4 = 0 - marker_radius
    while dx4 < marker_radius + 1:
        dy4 = 0 - marker_radius
        while dy4 < marker_radius + 1:
            if dx4 * dx4 + dy4 * dy4 <= marker_radius * marker_radius:
                pixel_x = map_x + dx4
                pixel_y = map_y + dy4
                # Keep markers inside the map border.
                if pixel_x >= 1 and pixel_x <= 62:
                    if pixel_y >= 1 and pixel_y <= 42:
                        map_image.set_pixel(pixel_x, pixel_y, color2)
            dy4 += 1
        dx4 += 1
# ==================================================
# RINGED PLANET IMAGE
# ==================================================
def make_ringed_planet_image():
    global size2, center2, ring_image
    size2 = 120
    center2 = 60
    ring_image = image.create(size2, size2)
    y2 = 0
    while y2 < size2:
        x2 = 0
        while x2 < size2:
            dx2 = x2 - center2
            dy2 = y2 - center2
            ellipse = Math.idiv(dx2 * dx2 * 100, 54 * 54) + Math.idiv(dy2 * dy2 * 100, 19 * 19)
            if ellipse >= 80 and ellipse <= 120:
                if dx2 < 0:
                    ring_image.set_pixel(x2, y2, 13)
                else:
                    ring_image.set_pixel(x2, y2, 5)
            x2 += 1
        y2 += 1
    y2 = 0
    while y2 < size2:
        x2 = 0
        while x2 < size2:
            dx2 = x2 - center2
            dy2 = y2 - center2
            distance_squared2 = dx2 * dx2 + dy2 * dy2
            if distance_squared2 <= 34 * 34:
                color22 = 4
                if y2 % 9 < 3:
                    color22 = 5
                if dx2 < -10 and dy2 < 5:
                    color22 = 14
                elif dx2 > 10:
                    color22 = 13
                ring_image.set_pixel(x2, y2, color22)
            x2 += 1
        y2 += 1
    return ring_image
# ==================================================
# ASTEROID DAMAGE
# ==================================================

def on_on_overlap2(sprite2, otherSprite2):
    global shipHP, lastDamageTime, nextDamageTime, healthBarVisible, gameEnded, shipVX, shipVY
    if gameEnded == False and game.runtime() >= nextDamageTime:
        shipHP += 0 - 20
        if shipHP < 0:
            shipHP = 0
        lastDamageTime = game.runtime()
        nextDamageTime = lastDamageTime + 1000
        health_bar.set_image(make_health_bar_image())
        health_bar.set_flag(SpriteFlag.INVISIBLE, False)
        healthBarVisible = True
        if shipHP <= 0:
            gameEnded = True
            shipVX = 0
            shipVY = 0
            mySprite.start_effect(effects.disintegrate, 500)
            pause(500)
            game.set_game_over_message(False, "SHIP DESTROYED!")
            game.game_over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

sunDistance = 0
acceleration = 0
shipVY = 0
shipVX = 0
healthBarVisible = False
lastDamageTime = 0
nextDamageTime = 0
ring_image: Image = None
center2 = 0
size2 = 0
map_y = 0
map_x = 0
gameEnded = False
candidateY = 0
candidateX = 0
attempts = 0
validPosition = False
asteroid3WorldY = 0
asteroid3WorldX = 0
asteroid2WorldY = 0
asteroid2WorldX = 0
asteroid1WorldY = 0
angle1 = 0
asteroid1WorldX = 0
planet3WorldY = 0
planet3WorldX = 0
planet2WorldY = 0
planet2WorldX = 0
planet1WorldY = 0
planet1WorldX = 0
minimapImage: Image = None
sun_image: Image = None
center3 = 0
size22 = 0
bar_width = 0
bar_image: Image = None
asteroid: Sprite = None
center = 0
planet_image: Image = None
minimapSprite: Sprite = None
MINIMAP_SCREEN_Y = 0
MINIMAP_SCREEN_X = 0
MINIMAP_HEIGHT = 0
MINIMAP_WIDTH = 0
health_bar: Sprite = None
TREASURE_COUNT = 0
mySprite: Sprite = None
radius3 = 0
radius2 = 0
radius1 = 0
angle3 = 0
angle2 = 0
planetRadius3 = 0
planetRadius2 = 0
planetRadius1 = 0
planetAngle3 = 0
planetAngle2 = 0
planetAngle1 = 0
STAR_DEATH_RADIUS = 0
starY = 0
starX = 0
shipWorldY = 0
shipWorldX = 0
maxHP = 0
shipHP = 0
SCREEN_CENTER_Y = 0
SCREEN_CENTER_X = 0
WORLD_HEIGHT = 0
WORLD_WIDTH = 0
treasureWorldY: List[number] = []
treasureWorldX: List[number] = []
treasureSprites: List[Sprite] = []
# ==================================================
# SPACE TREASURE COLLECTOR
# EXPANDED SOLAR SYSTEM + LIVE MINIMAP
# ==================================================
# WORLD SETTINGS
WORLD_WIDTH = 7000
WORLD_HEIGHT = 5000
SCREEN_CENTER_X = 80
SCREEN_CENTER_Y = 60
# ==================================================
# GAME VARIABLES
# ==================================================
shipSpeed = 20
shipHP = 100
maxHP = 100
shipWorldX = 1330
shipWorldY = 1550
MAX_SHIP_VELOCITY = 3
# ==================================================
# CINEMATIC ENDING VARIABLES
# ==================================================

mothershipSprite: Sprite = None
chargeBarSprite: Sprite = None

endingState = 0
endingTimer = 0
explosionIndex = 0
redLevel = 0
starCharge = 0
collapseFrame = 0
bWasDown = False
restartArmed = False
# Ending states
ENDING_NORMAL = 0
ENDING_MOTHERSHIP_FALL = 1
ENDING_BOSS_EXPLOSION = 2
ENDING_STAR_CHARGE = 3
ENDING_STAR_COLLAPSE = 4
ENDING_BLACK_HOLE = 5
ENDING_DARKNESS_CHOICE = 6
ENDING_STAY_IN_DARKNESS = 7
# ==================================================
# SOLAR SYSTEM
# ==================================================
starX = 3500
starY = 2500
STAR_DEATH_RADIUS = 100
# Planet orbit angles
planetAngle1 = 0.8
planetAngle2 = 5.2
planetAngle3 = 3.55
# Planet orbit speeds
planetSpeed1 = 0.002
planetSpeed2 = 0.0013
planetSpeed3 = 0.0008
# Planet orbit distances
planetRadius1 = 750
planetRadius2 = 1450
planetRadius3 = 2300
angle2 = 2.8
angle3 = 4.8
# Asteroid orbit speeds
orbitSpeed1 = 0.015
orbitSpeed2 = 0.011
orbitSpeed3 = 0.008
# Asteroid orbit distances
radius1 = 160
radius2 = 280
radius3 = 400
# ==================================================
# BACKGROUND
# ==================================================
# Completely black background.
# No white dots or background star sprites.
scene.set_background_color(15)
# ==================================================
# RED GRADIENT BACKGROUND
# ==================================================

def set_red_gradient(level: number):
    backgroundImage = image.create(160, 120)

    y = 0
    while y < 120:
        rowLevel = Math.idiv(y * 100, 120)

        if rowLevel < level:
            if rowLevel < 30:
                colour = 14
            elif rowLevel < 70:
                colour = 2
            else:
                colour = 4
        else:
            colour = 15

        backgroundImage.fill_rect(0, y, 160, 1, colour)
        y += 1

    scene.set_background_image(backgroundImage)


# ==================================================
# STAR AND BLACK HOLE IMAGES
# ==================================================

def make_ending_core_image(radius: number, blackHole: bool):
    size = radius * 2 + 2
    centre = radius + 1
    coreImage = image.create(size, size)

    y = 0
    while y < size:
        x = 0
        while x < size:
            dx = x - centre
            dy = y - centre
            distanceSquared = dx * dx + dy * dy

            if distanceSquared <= radius * radius:
                if blackHole:
                    if distanceSquared > (radius - 5) * (radius - 5):
                        colour = 10
                    elif distanceSquared > 9 * 9:
                        colour = 11
                    else:
                        colour = 15
                else:
                    if distanceSquared > (radius - 6) * (radius - 6):
                        colour = 5
                    elif distanceSquared > (radius // 2) * (radius // 2):
                        colour = 4
                    else:
                        colour = 2

                coreImage.set_pixel(x, y, colour)

            x += 1
        y += 1

    return coreImage


# ==================================================
# EXPLOSION IMAGE
# ==================================================

def make_ending_explosion(radius: number):
    size = radius * 2 + 1
    centre = radius
    explosionImage = image.create(size, size)

    y = 0
    while y < size:
        x = 0
        while x < size:
            dx = x - centre
            dy = y - centre

            if dx * dx + dy * dy <= radius * radius:
                colour = 4

                if abs(dx) <= 1 or abs(dy) <= 1:
                    colour = 5
                elif abs(dx - dy) <= 1 or abs(dx + dy) <= 1:
                    colour = 5

                explosionImage.set_pixel(x, y, colour)

            x += 1
        y += 1

    return explosionImage


def create_ending_explosion(x: number, y: number, radius: number):
    flash = sprites.create(make_ending_explosion(radius),
        SpriteKind.projectile)
    flash.set_position(x, y)
    flash.z = 220
    flash.lifespan = 350
    flash.start_effect(effects.fire, 250)
# ==================================================
# SPACESHIP
# ==================================================
mySprite = sprites.create(assets.image("""
    ship
    """), SpriteKind.player)
mySprite.set_position(SCREEN_CENTER_X, SCREEN_CENTER_Y)
# Ship is above planets and asteroids.
mySprite.z = 100
# ==================================================
# TREASURE CHEST IMAGE
# ==================================================
treasureImage = img("""
    . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . .
    . . . f f f f f f f f f f f . . .
    . . . f e e e e e e e e e f . . .
    . . . f e e e e e e e e e f . . .
    . . . f e e e e e e e e e f . . .
    . . . f f f f 5 f 5 f f f f . . .
    . . . f e e e 5 5 5 e e e f . . .
    . . . f e e e e e e e e e f . . .
    . . . f e e e e e e e e e f . . .
    . . . f e e e e e e e e e f . . .
    . . . f f f f f f f f f f f . . .
    . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . .
    """)
# ==================================================
# TEN TREASURE CHESTS
# ==================================================
TREASURE_COUNT = 10
initialTreasureX = [1270, 400, 2100, 3400, 6500, 6500, 4600, 1600, 300, 3600]
initialTreasureY = [1560, 400, 450, 300, 800, 4400, 4600, 4400, 2800, 3700]
i = 0
while i < TREASURE_COUNT:
    chest = sprites.create(treasureImage, SpriteKind.food)
    chest.z = 40
    treasureSprites.append(chest)
    treasureWorldX.append(initialTreasureX[i])
    treasureWorldY.append(initialTreasureY[i])
    chest.set_position(initialTreasureX[i] - shipWorldX + SCREEN_CENTER_X,
        initialTreasureY[i] - shipWorldY + SCREEN_CENTER_Y)
    i += 1
health_bar = sprites.create(make_health_bar_image(), SpriteKind.projectile)
health_bar.set_flag(SpriteFlag.GHOST, True)
health_bar.set_flag(SpriteFlag.INVISIBLE, True)
health_bar.z = 200
def start_victory_sequence():
    global gameEnded, endingState, endingTimer
    global explosionIndex, shipVX, shipVY
    global redLevel, starCharge

    if endingState != ENDING_NORMAL:
        return

    gameEnded = True
    shipVX = 0
    shipVY = 0

    endingState = ENDING_MOTHERSHIP_FALL
    endingTimer = 0
    explosionIndex = 0
    redLevel = 0
    starCharge = 0
# ==================================================
# PLANETS
# ==================================================
planet1 = sprites.create(make_planet_image(96, 44, 8, 7, 1, 12, 1),
    SpriteKind.projectile)
planet2 = sprites.create(make_ringed_planet_image(), SpriteKind.projectile)
planet3 = sprites.create(make_planet_image(100, 46, 10, 9, 1, 12, 3),
    SpriteKind.projectile)
planet1.set_flag(SpriteFlag.GHOST, True)
planet2.set_flag(SpriteFlag.GHOST, True)
planet3.set_flag(SpriteFlag.GHOST, True)
planet1.z = 10
planet2.z = 10
planet3.z = 10
# ==================================================
# CENTRAL SUN
# ==================================================
centralStar = sprites.create(make_sun_image(), SpriteKind.projectile)
centralStar.set_flag(SpriteFlag.GHOST, True)
centralStar.z = 0
asteroid1 = create_asteroid(1)
asteroid2 = create_asteroid(2)
asteroid3 = create_asteroid(3)
# ==================================================
# MINIMAP SETTINGS
# ==================================================
MINIMAP_WIDTH = 64
MINIMAP_HEIGHT = 44
MINIMAP_SCREEN_X = 124
MINIMAP_SCREEN_Y = 96
# Create the minimap display sprite.
minimapSprite = sprites.create(image.create(MINIMAP_WIDTH, MINIMAP_HEIGHT),
    SpriteKind.projectile)
minimapSprite.set_flag(SpriteFlag.GHOST, True)
# Keep the minimap fixed on the screen.
minimapSprite.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
minimapSprite.set_position(MINIMAP_SCREEN_X, MINIMAP_SCREEN_Y)
# Draw it above the game world and health bar.
minimapSprite.z = 250
game.on_update_interval(500, update_minimap)
# Draw the first map immediately.
update_minimap()
# ==================================================
# START GAME
# ==================================================
info.set_score(0)
# ==================================================
# WORLD UPDATE AND CAMERA
# ==================================================

def on_on_update():
    global acceleration, shipVX, shipVY, shipWorldX, shipWorldY, planetAngle1, planetAngle2, planetAngle3, angle1, angle2, angle3, sunDistance, gameEnded, healthBarVisible
    if gameEnded:
        return
    # ----------------------------------------------
    # SHIP DIRECTION
    # ----------------------------------------------
    if controller.right.is_pressed() and not (controller.left.is_pressed()):
        mySprite.rotation_degrees = 90
    elif controller.left.is_pressed() and not (controller.right.is_pressed()):
        mySprite.rotation_degrees = -90
    elif controller.down.is_pressed() and not (controller.up.is_pressed()):
        mySprite.rotation_degrees = 180
    elif controller.up.is_pressed() and not (controller.down.is_pressed()):
        mySprite.rotation_degrees = 0
    # ----------------------------------------------
    # SHIP ACCELERATION
    # ----------------------------------------------
    acceleration = shipSpeed / 200
    if controller.left.is_pressed() and not (controller.right.is_pressed()):
        shipVX += 0 - acceleration
        if shipVX < 0 - MAX_SHIP_VELOCITY:
            shipVX = 0 - MAX_SHIP_VELOCITY
    elif controller.right.is_pressed() and not (controller.left.is_pressed()):
        shipVX += acceleration
        if shipVX > MAX_SHIP_VELOCITY:
            shipVX = MAX_SHIP_VELOCITY
    else:
        shipVX = shipVX * 0.94
    if controller.up.is_pressed() and not (controller.down.is_pressed()):
        shipVY += 0 - acceleration
        if shipVY < 0 - MAX_SHIP_VELOCITY:
            shipVY = 0 - MAX_SHIP_VELOCITY
    elif controller.down.is_pressed() and not (controller.up.is_pressed()):
        shipVY += acceleration
        if shipVY > MAX_SHIP_VELOCITY:
            shipVY = MAX_SHIP_VELOCITY
    else:
        shipVY = shipVY * 0.94
    # ----------------------------------------------
    # MOVE THROUGH THE WORLD
    # ----------------------------------------------
    shipWorldX += shipVX
    shipWorldY += shipVY
    if shipWorldX < 10:
        shipWorldX = 10
        shipVX = 0
    if shipWorldX > WORLD_WIDTH - 10:
        shipWorldX = WORLD_WIDTH - 10
        shipVX = 0
    if shipWorldY < 10:
        shipWorldY = 10
        shipVY = 0
    if shipWorldY > WORLD_HEIGHT - 10:
        shipWorldY = WORLD_HEIGHT - 10
        shipVY = 0
    # ----------------------------------------------
    # KEEP THE SHIP CENTRED
    # ----------------------------------------------
    mySprite.set_position(SCREEN_CENTER_X, SCREEN_CENTER_Y)
    # ----------------------------------------------
    # MOVE THE SUN
    # ----------------------------------------------
    centralStar.set_position(starX - shipWorldX + SCREEN_CENTER_X,
        starY - shipWorldY + SCREEN_CENTER_Y)
    # ----------------------------------------------
    # PLANET ORBITS
    # ----------------------------------------------
    planetAngle1 += planetSpeed1
    planetAngle2 += planetSpeed2
    planetAngle3 += planetSpeed3
    spriteutils.place_angle_from(planet1, planetAngle1, planetRadius1, centralStar)
    spriteutils.place_angle_from(planet2, planetAngle2, planetRadius2, centralStar)
    spriteutils.place_angle_from(planet3, planetAngle3, planetRadius3, centralStar)
    # ----------------------------------------------
    # ASTEROID ORBITS
    # ----------------------------------------------
    angle1 += orbitSpeed1
    angle2 += orbitSpeed2
    angle3 += orbitSpeed3
    spriteutils.place_angle_from(asteroid1, angle1, radius1, centralStar)
    spriteutils.place_angle_from(asteroid2, angle2, radius2, centralStar)
    spriteutils.place_angle_from(asteroid3, angle3, radius3, centralStar)
    # ----------------------------------------------
    # TREASURE CHEST POSITIONS
    # ----------------------------------------------
    m = 0
    while m <= TREASURE_COUNT - 1:
        treasureSprites[m].set_position(treasureWorldX[m] - shipWorldX + SCREEN_CENTER_X,
            treasureWorldY[m] - shipWorldY + SCREEN_CENTER_Y)
        m += 1
    # ----------------------------------------------
    # SUN DANGER ZONE
    # ----------------------------------------------
    sunDistance = spriteutils.distance_between(mySprite, centralStar)
    if sunDistance <= STAR_DEATH_RADIUS:
        gameEnded = True
        shipVX = 0
        shipVY = 0
        mySprite.start_effect(effects.fire, 400)
        pause(250)
        game.set_game_over_message(False, "BURNED BY THE SUN!")
        game.game_over(False)
        return
    # ----------------------------------------------
    # HEALTH BAR
    # ----------------------------------------------
    health_bar.set_position(SCREEN_CENTER_X, SCREEN_CENTER_Y - 15)
    if healthBarVisible:
        if game.runtime() - lastDamageTime >= 3000:
            health_bar.set_flag(SpriteFlag.INVISIBLE, True)
            healthBarVisible = False
game.on_update(on_on_update)

# ==================================================
# GRADUALLY INCREASE SHIP SPEED
# ==================================================

def on_forever():
    global shipSpeed
    if not (gameEnded) and shipSpeed < 60:
        shipSpeed += 1
    pause(500)
forever(on_forever)