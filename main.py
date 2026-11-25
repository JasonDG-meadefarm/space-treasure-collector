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
    # Reset these for EVERY respawn. Without this, later respawns can
    # reuse an old position because validPosition stays True.
    validPosition = False
    attempts = 0
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
ufoSprites: List[Sprite] = []
ufoDisabledUntil = [0, 0, 0]
# A: tap = 3-second boost; hold 0.45 seconds and release = 1000-pixel hyperjump.
# Both A abilities share a 15-second cooldown.
boostUntil = 0
boostCooldownUntil = 0
aPressStart = 0
aPressAllowed = False
aHolding = False
warpFlashUntil = 0

# B: hold to charge a capped orb; release = non-damaging UFO-disabling pulse.
# The pulse has a 0.5-second cooldown.
attackCharging = False
attackChargeStart = 0
attackChargeLevel = 0
attackCooldownUntil = 0
attackPulseUntil = 0
attackPulseRange = 0

# Visual ability sprites and images
chargeOrbImages: List[Image] = []
pulseImages: List[Image] = []
warpImages: List[Image] = []
chargeOrbSprite: Sprite = None
pulseSprite: Sprite = None
warpSprite: Sprite = None
hudImage: Image = None
hudSprite: Sprite = None
# ==================================================
# ABILITY VISUALS AND HUD FONT
# ==================================================
def make_charge_orb_image(radius: number):
    size = radius * 2 + 1
    centre = radius
    orbImage = image.create(size, size)
    y = 0
    while y < size:
        x = 0
        while x < size:
            dx = x - centre
            dy = y - centre
            distanceSquared = dx * dx + dy * dy
            if distanceSquared <= radius * radius:
                if distanceSquared <= (radius - 2) * (radius - 2):
                    orbColor = 1
                elif distanceSquared <= (radius - 1) * (radius - 1):
                    orbColor = 9
                else:
                    orbColor = 13
                orbImage.set_pixel(x, y, orbColor)
            x += 1
        y += 1
    return orbImage

def make_pulse_image(radius: number):
    size = radius * 2 + 1
    centre = radius
    pulseImage = image.create(size, size)
    y = 0
    while y < size:
        x = 0
        while x < size:
            dx = x - centre
            dy = y - centre
            distanceSquared = dx * dx + dy * dy
            if distanceSquared <= radius * radius and distanceSquared >= (radius - 2) * (radius - 2):
                pulseImage.set_pixel(x, y, 9)
            elif distanceSquared <= (radius - 6) * (radius - 6) and distanceSquared >= (radius - 8) * (radius - 8):
                pulseImage.set_pixel(x, y, 12)
            x += 1
        y += 1
    return pulseImage

def make_warp_image(frame: number):
    size = 49
    centre = 24
    warpImage = image.create(size, size)
    y = 0
    while y < size:
        x = 0
        while x < size:
            dx = x - centre
            dy = y - centre
            distanceSquared = dx * dx + dy * dy
            if distanceSquared >= 11 * 11 and distanceSquared <= 22 * 22:
                pattern = (x * 2 + y * 3 + frame * 5) % 13
                if pattern < 4:
                    warpImage.set_pixel(x, y, 9)
                elif pattern < 7:
                    warpImage.set_pixel(x, y, 13)
            elif distanceSquared >= 7 * 7 and distanceSquared <= 9 * 9:
                warpImage.set_pixel(x, y, 1)
            x += 1
        y += 1
    return warpImage

def tiny_glyph(character):
    blank = ["000", "000", "000", "000", "000"]
    if character == "A":
        return ["010", "101", "111", "101", "101"]
    if character == "B":
        return ["110", "101", "110", "101", "110"]
    if character == "C":
        return ["011", "100", "100", "100", "011"]
    if character == "D":
        return ["110", "101", "101", "101", "110"]
    if character == "E":
        return ["111", "100", "110", "100", "111"]
    if character == "K":
        return ["101", "101", "110", "101", "101"]
    if character == "O":
        return ["010", "101", "101", "101", "010"]
    if character == "R":
        return ["110", "101", "110", "101", "101"]
    if character == "S":
        return ["011", "100", "010", "001", "110"]
    if character == "T":
        return ["111", "010", "010", "010", "010"]
    if character == "Y":
        return ["101", "101", "010", "010", "010"]
    if character == "0":
        return ["111", "101", "101", "101", "111"]
    if character == "1":
        return ["010", "110", "010", "010", "111"]
    if character == "2":
        return ["110", "001", "010", "100", "111"]
    if character == "3":
        return ["110", "001", "010", "001", "110"]
    if character == "4":
        return ["101", "101", "111", "001", "001"]
    if character == "5":
        return ["111", "100", "110", "001", "110"]
    if character == "6":
        return ["011", "100", "110", "101", "010"]
    if character == "7":
        return ["111", "001", "010", "010", "010"]
    if character == "8":
        return ["010", "101", "010", "101", "010"]
    if character == "9":
        return ["010", "101", "011", "001", "110"]
    if character == ":":
        return ["000", "010", "000", "010", "000"]
    if character == ".":
        return ["000", "000", "000", "000", "010"]
    return blank

def draw_tiny_text(target: Image, textValue, startX: number, startY: number, color: number):
    charIndex = 0
    while charIndex < len(textValue):
        glyph = tiny_glyph(textValue[charIndex])
        row = 0
        while row < 5:
            column = 0
            while column < 3:
                if glyph[row][column] == "1":
                    target.set_pixel(startX + charIndex * 4 + column, startY + row, color)
                column += 1
            row += 1
        charIndex += 1

def time_label(milliseconds: number):
    if milliseconds < 0:
        milliseconds = 0
    tenths = Math.idiv(milliseconds + 99, 100)
    return str(Math.idiv(tenths, 10)) + "." + str(tenths % 10) + "S"

def update_ability_hud():
    now = game.runtime()
    hudImage.fill(15)
    if now < boostUntil:
        boostText = "BOOST: " + time_label(boostUntil - now)
    elif now < boostCooldownUntil:
        boostText = "BOOST CD: " + time_label(boostCooldownUntil - now)
    else:
        boostText = "BOOST CD: READY"
    if now < attackCooldownUntil:
        attackText = "ATK CD: " + time_label(attackCooldownUntil - now)
    else:
        attackText = "ATK CD: READY"
    draw_tiny_text(hudImage, boostText, 2, 1, 9)
    draw_tiny_text(hudImage, attackText, 2, 9, 12)
    hudSprite.set_image(hudImage)

def facing_x():
    direction = mySprite.rotation_degrees
    if direction == 90:
        return 1
    elif direction == -90 or direction == 270:
        return -1
    return 0

def facing_y():
    direction = mySprite.rotation_degrees
    if direction == 180:
        return 1
    elif direction == 0:
        return -1
    return 0

def perform_hyperjump():
    global shipWorldX, shipWorldY, shipVX, shipVY
    global boostUntil, boostCooldownUntil, warpFlashUntil
    directionX = facing_x()
    directionY = facing_y()
    destinationX = shipWorldX + directionX * 1000
    destinationY = shipWorldY + directionY * 1000
    # Wrap to the opposite edge if the 1000-pixel jump crosses a border.
    shipWorldX = 10 + ((destinationX - 10) % (WORLD_WIDTH - 20))
    shipWorldY = 10 + ((destinationY - 10) % (WORLD_HEIGHT - 20))
    shipVX = directionX * 0.8
    shipVY = directionY * 0.8
    boostUntil = 0
    boostCooldownUntil = game.runtime() + 15000
    warpFlashUntil = game.runtime() + 550

def on_a_pressed():
    global aPressStart, aPressAllowed, aHolding
    if gameEnded or endingState != ENDING_NORMAL:
        return
    now = game.runtime()
    aPressStart = now
    aPressAllowed = now >= boostCooldownUntil
    aHolding = aPressAllowed
    if aHolding:
        warpSprite.set_flag(SpriteFlag.INVISIBLE, False)

def on_a_released():
    global aHolding, boostUntil, boostCooldownUntil, warpFlashUntil
    now = game.runtime()
    heldFor = now - aPressStart
    wasAllowed = aPressAllowed
    aHolding = False
    if not wasAllowed or gameEnded or endingState != ENDING_NORMAL:
        warpSprite.set_flag(SpriteFlag.INVISIBLE, True)
        return
    if heldFor >= 450:
        perform_hyperjump()
    else:
        # A quick tap starts a three-second speed boost.
        boostUntil = now + 3000
        boostCooldownUntil = boostUntil + 15000
        warpFlashUntil = now + 200
    warpSprite.set_flag(SpriteFlag.INVISIBLE, False)

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
# BLACK SPACE BACKGROUND WITH A SPARSE WHITE STARFIELD
# This is a background image, not sprite objects, so it will not
# interfere with treasure, asteroid, or UFO collisions.
spaceBackground = image.create(160, 120)
spaceBackground.fill(15)
starDot = 0
while starDot < 85:
    starXPixel = randint(0, 159)
    starYPixel = randint(0, 119)
    starColour = 1
    if starDot % 3 == 0:
        starColour = 12
    elif starDot % 5 == 0:
        starColour = 13
    spaceBackground.set_pixel(starXPixel, starYPixel, starColour)
    starDot += 1
scene.set_background_image(spaceBackground)
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
# FLYING UFOs
# ==================================================
ufoImage = img("""
    . . . . . . 8 8 8 8 . . . . . .
    . . . 8 8 8 9 9 9 9 8 8 8 . . .
    . . 8 9 9 9 9 9 9 9 9 9 9 8 . .
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    . . . 8 8 8 8 8 8 8 8 8 8 . . .
    . . . . . 8 . . . . 8 . . . . .
    """)
UFO_COUNT = 3
# Each UFO loops around its own nearby point, at a different speed.
ufoCentreX = [1365, 1450, 1500]
ufoCentreY = [1500, 1500, 1600]
ufoRadiusX = [55, 80, 100]
ufoRadiusY = [35, 50, 55]
ufoStartAngle = [0, 1.57, 3.14]
ufoOrbitSpeed = [0.00036, 0.00031, 0.00025]
ufoIndex = 0
while ufoIndex < UFO_COUNT:
    flyingUfo = sprites.create(ufoImage, SpriteKind.enemy)
    flyingUfo.z = 35
    # Place each UFO away from the ship before the first game update.
    initialAngle = game.runtime() * ufoOrbitSpeed[ufoIndex] + ufoStartAngle[ufoIndex]
    initialUfoX = ufoCentreX[ufoIndex] + Math.cos(initialAngle) * ufoRadiusX[ufoIndex]
    initialUfoY = ufoCentreY[ufoIndex] + Math.sin(initialAngle) * ufoRadiusY[ufoIndex]
    flyingUfo.set_position(initialUfoX - shipWorldX + SCREEN_CENTER_X,
        initialUfoY - shipWorldY + SCREEN_CENTER_Y)
    ufoSprites.append(flyingUfo)
    ufoIndex += 1

# ==================================================
# CHARGED B PULSE
# Hold B to charge a glowing orb. Releasing B sends a
# non-damaging defensive pulse around the ship.
# ==================================================
chargeOrbImages = [make_charge_orb_image(3), make_charge_orb_image(4),
    make_charge_orb_image(5), make_charge_orb_image(6),
    make_charge_orb_image(7), make_charge_orb_image(8)]
pulseImages = [make_pulse_image(12), make_pulse_image(15),
    make_pulse_image(18), make_pulse_image(21),
    make_pulse_image(24), make_pulse_image(27)]
warpImages = [make_warp_image(0), make_warp_image(1),
    make_warp_image(2), make_warp_image(3)]

chargeOrbSprite = sprites.create(chargeOrbImages[0], SpriteKind.projectile)
chargeOrbSprite.set_flag(SpriteFlag.GHOST, True)
chargeOrbSprite.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
chargeOrbSprite.set_flag(SpriteFlag.INVISIBLE, True)
chargeOrbSprite.z = 160

pulseSprite = sprites.create(pulseImages[0], SpriteKind.projectile)
pulseSprite.set_flag(SpriteFlag.GHOST, True)
pulseSprite.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
pulseSprite.set_flag(SpriteFlag.INVISIBLE, True)
pulseSprite.set_position(SCREEN_CENTER_X, SCREEN_CENTER_Y)
pulseSprite.z = 150

warpSprite = sprites.create(warpImages[0], SpriteKind.projectile)
warpSprite.set_flag(SpriteFlag.GHOST, True)
warpSprite.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
warpSprite.set_flag(SpriteFlag.INVISIBLE, True)
warpSprite.set_position(SCREEN_CENTER_X, SCREEN_CENTER_Y)
warpSprite.z = 90

# Small pixel-font HUD avoids requiring another extension.
hudImage = image.create(100, 16)
hudImage.fill(15)
hudSprite = sprites.create(hudImage, SpriteKind.projectile)
hudSprite.set_flag(SpriteFlag.GHOST, True)
hudSprite.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
hudSprite.set_position(50, 9)
hudSprite.z = 260

def on_b_pressed():
    global attackCharging, attackChargeStart, attackChargeLevel
    if gameEnded or endingState != ENDING_NORMAL:
        return
    if attackCharging or game.runtime() < attackCooldownUntil:
        return
    attackCharging = True
    attackChargeStart = game.runtime()
    attackChargeLevel = 0
    chargeOrbSprite.set_image(chargeOrbImages[0])
    chargeOrbSprite.set_flag(SpriteFlag.INVISIBLE, False)

def on_b_released():
    global attackCharging, attackChargeLevel, attackCooldownUntil
    global attackPulseUntil, attackPulseRange
    if not attackCharging:
        return
    now = game.runtime()
    attackCharging = False
    attackChargeLevel = Math.idiv(now - attackChargeStart, 400)
    if attackChargeLevel > len(chargeOrbImages) - 1:
        attackChargeLevel = len(chargeOrbImages) - 1
    attackPulseRange = 120 + attackChargeLevel * 30
    attackPulseUntil = now + 450
    attackCooldownUntil = now + 500
    chargeOrbSprite.set_flag(SpriteFlag.INVISIBLE, True)
    pulseSprite.set_image(pulseImages[attackChargeLevel])
    pulseSprite.set_position(SCREEN_CENTER_X, SCREEN_CENTER_Y)
    pulseSprite.set_flag(SpriteFlag.INVISIBLE, False)
    # The pulse briefly disables any UFOs close enough to the ship.
    ufoIndex = 0
    while ufoIndex < UFO_COUNT:
        ufoAngle = now * ufoOrbitSpeed[ufoIndex] + ufoStartAngle[ufoIndex]
        nearbyUfoX = ufoCentreX[ufoIndex] + Math.cos(ufoAngle) * ufoRadiusX[ufoIndex]
        nearbyUfoY = ufoCentreY[ufoIndex] + Math.sin(ufoAngle) * ufoRadiusY[ufoIndex]
        dxUfo = nearbyUfoX - shipWorldX
        dyUfo = nearbyUfoY - shipWorldY
        if dxUfo * dxUfo + dyUfo * dyUfo <= attackPulseRange * attackPulseRange:
            ufoDisabledUntil[ufoIndex] = now + 2200
        ufoIndex += 1

controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)
controller.B.on_event(ControllerButtonEvent.RELEASED, on_b_released)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)
controller.A.on_event(ControllerButtonEvent.RELEASED, on_a_released)
game.on_update_interval(100, update_ability_hud)
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
    global acceleration, shipVX, shipVY, shipWorldX, shipWorldY, planetAngle1, planetAngle2, planetAngle3, angle1, angle2, angle3, sunDistance, gameEnded, healthBarVisible, attackChargeLevel
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
    # A-BUTTON WORMHOLE VISUAL WHILE HELD
    # ----------------------------------------------
    abilityNow = game.runtime()
    if aHolding:
        warpFrame = Math.idiv(abilityNow, 100) % len(warpImages)
        warpSprite.set_image(warpImages[warpFrame])
        warpSprite.rotation_degrees = Math.idiv(abilityNow, 8) % 360
        warpSprite.set_position(SCREEN_CENTER_X, SCREEN_CENTER_Y)
        warpSprite.set_flag(SpriteFlag.INVISIBLE, False)
    elif abilityNow >= warpFlashUntil:
        warpSprite.set_flag(SpriteFlag.INVISIBLE, True)
    # ----------------------------------------------
    # B-BUTTON CHARGE ORB GROWS WHILE HELD
    # ----------------------------------------------
    if attackCharging:
        attackChargeLevel = Math.idiv(abilityNow - attackChargeStart, 400)
        if attackChargeLevel > len(chargeOrbImages) - 1:
            attackChargeLevel = len(chargeOrbImages) - 1
        chargeOrbSprite.set_image(chargeOrbImages[attackChargeLevel])
        facingX = facing_x()
        facingY = facing_y()
        chargeOrbSprite.set_position(SCREEN_CENTER_X + facingX * 22,
            SCREEN_CENTER_Y + facingY * 22)
        chargeOrbSprite.set_flag(SpriteFlag.INVISIBLE, False)
    if abilityNow >= attackPulseUntil:
        pulseSprite.set_flag(SpriteFlag.INVISIBLE, True)
    # ----------------------------------------------
    # SHIP ACCELERATION (BOOST MAKES THE SHIP FASTER)
    # ----------------------------------------------
    if abilityNow < boostUntil:
        acceleration = shipSpeed / 75
        currentMaxVelocity = 7.5
    else:
        acceleration = shipSpeed / 200
        currentMaxVelocity = MAX_SHIP_VELOCITY
    if controller.left.is_pressed() and not (controller.right.is_pressed()):
        shipVX += 0 - acceleration
        if shipVX < 0 - currentMaxVelocity:
            shipVX = 0 - currentMaxVelocity
    elif controller.right.is_pressed() and not (controller.left.is_pressed()):
        shipVX += acceleration
        if shipVX > currentMaxVelocity:
            shipVX = currentMaxVelocity
    else:
        shipVX = shipVX * 0.94
    if controller.up.is_pressed() and not (controller.down.is_pressed()):
        shipVY += 0 - acceleration
        if shipVY < 0 - currentMaxVelocity:
            shipVY = 0 - currentMaxVelocity
    elif controller.down.is_pressed() and not (controller.up.is_pressed()):
        shipVY += acceleration
        if shipVY > currentMaxVelocity:
            shipVY = currentMaxVelocity
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
    # UFO FLIGHT PATHS AND DISABLE TIMER
    # ----------------------------------------------
    ufoNow = game.runtime()
    ufoIndex = 0
    while ufoIndex < UFO_COUNT:
        ufoAngle = ufoNow * ufoOrbitSpeed[ufoIndex] + ufoStartAngle[ufoIndex]
        ufoWorldX = ufoCentreX[ufoIndex] + Math.cos(ufoAngle) * ufoRadiusX[ufoIndex]
        ufoWorldY = ufoCentreY[ufoIndex] + Math.sin(ufoAngle) * ufoRadiusY[ufoIndex]
        ufoSprites[ufoIndex].set_position(ufoWorldX - shipWorldX + SCREEN_CENTER_X,
            ufoWorldY - shipWorldY + SCREEN_CENTER_Y)
        if ufoNow < ufoDisabledUntil[ufoIndex]:
            ufoSprites[ufoIndex].set_flag(SpriteFlag.GHOST, True)
        else:
            ufoSprites[ufoIndex].set_flag(SpriteFlag.GHOST, False)
        ufoIndex += 1
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
    pulseSprite.set_position(SCREEN_CENTER_X, SCREEN_CENTER_Y)
    hudSprite.set_position(50, 9)
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
