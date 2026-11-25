let starXPixel: number;
let starYPixel: number;
let starColour: number;
let chest: Sprite;
let flyingUfo: Sprite;
let initialAngle: number;
let initialUfoX: number;
let initialUfoY: number;
/** Asteroid orbit angles */
//  ==================================================
//  PLANET IMAGE GENERATOR
//  ==================================================
function make_planet_image(size: number, radius: number, base_color: number, pattern_color: number, highlight_color: number, shadow_color: number, style: number): Image {
    let x: number;
    let dx: number;
    let dy: number;
    let distance_squared: any;
    let color: number;
    
    planet_image = image.create(size, size)
    center = Math.idiv(size, 2)
    let y = 0
    while (y <= size - 1) {
        x = 0
        while (x <= size - 1) {
            dx = x - center
            dy = y - center
            distance_squared = dx * dx + dy * dy
            if (distance_squared <= radius * radius) {
                color = base_color
                if (style == 1) {
                    //  Ocean and land patterns
                    if ((x * 7 + y * 3) % 37 < 11) {
                        color = pattern_color
                    }
                    
                } else if (style == 2) {
                    //  Gas giant bands
                    if (y % 11 < 4) {
                        color = pattern_color
                    }
                    
                } else if ((x + y * 2) % 23 < 6) {
                    color = pattern_color
                }
                
                //  Lit side
                if (dx < 0 - Math.idiv(radius, 3) && dy < Math.idiv(radius, 3)) {
                    color = highlight_color
                } else if (dx > Math.idiv(radius, 3)) {
                    //  Shadow side
                    color = shadow_color
                }
                
                planet_image.setPixel(x, y, color)
            }
            
            x += 1
        }
        y += 1
    }
    return planet_image
}

//  ==================================================
//  ASTEROIDS
//  ==================================================
function create_asteroid(variant: number): Sprite {
    let asteroidImage: Image;
    
    if (variant == 1) {
        asteroidImage = img`
            . . . 8 8 8 . . . . . . . . . . . .
            . . 8 7 7 7 8 8 . . . . . . . . . .
            . 8 7 7 8 7 7 7 8 . . . . . . . . .
            8 7 7 7 7 7 7 7 8 . . . . . . . . .
            8 7 8 7 7 8 7 7 7 8 . . . . . . . .
            . 8 7 7 7 7 7 7 8 . . . . . . . . .
            . . 8 8 7 7 8 8 . . . . . . . . . .
            . . . 8 8 8 8 . . . . . . . . . . .
            `
    } else if (variant == 2) {
        asteroidImage = img`
            . . . . 8 8 8 . . . . . . . . .
            . . 8 8 7 7 7 8 8 . . . . . . .
            . 8 7 7 7 8 7 7 7 8 . . . . . .
            8 7 8 7 7 7 7 7 7 8 . . . . . .
            8 7 7 7 7 8 7 7 8 . . . . . . .
            . 8 7 7 7 7 7 7 8 . . . . . . .
            . . 8 8 7 7 8 8 . . . . . . . .
            . . . 8 8 8 8 . . . . . . . . .
            `
    } else {
        asteroidImage = img`
            . . . . 8 8 . . . . . . . . . . .
            . . 8 8 7 7 8 8 . . . . . . . . .
            . 8 7 7 7 7 7 7 8 . . . . . . . .
            8 7 7 8 7 7 8 7 7 8 . . . . . . .
            8 7 7 7 7 7 7 7 7 8 . . . . . . .
            . 8 7 8 7 7 7 8 7 8 . . . . . . .
            . . 8 7 7 7 7 7 8 . . . . . . . .
            . . . 8 8 8 8 8 . . . . . . . . .
            `
    }
    
    asteroid = sprites.create(asteroidImage, SpriteKind.Enemy)
    asteroid.z = 20
    return asteroid
}

//  ==================================================
//  HEALTH BAR
//  ==================================================
function make_health_bar_image(): Image {
    let bar_color: number;
    
    bar_image = image.create(34, 6)
    bar_image.fill(15)
    bar_image.fillRect(1, 1, 32, 4, 1)
    bar_width = Math.idiv(shipHP * 32, maxHP)
    if (shipHP > 60) {
        bar_color = 6
    } else if (shipHP > 30) {
        bar_color = 14
    } else {
        bar_color = 10
    }
    
    if (bar_width > 0) {
        bar_image.fillRect(1, 1, bar_width, 4, bar_color)
    }
    
    return bar_image
}

//  ==================================================
//  SUN IMAGE
//  ==================================================
function make_sun_image(): Image {
    let x3: number;
    let dx3: number;
    let dy3: number;
    let distance_squared3: any;
    let color3: number;
    
    size22 = 128
    center3 = 64
    sun_image = image.create(size22, size22)
    let y3 = 0
    while (y3 <= size22 - 1) {
        x3 = 0
        while (x3 <= size22 - 1) {
            dx3 = x3 - center3
            dy3 = y3 - center3
            distance_squared3 = dx3 * dx3 + dy3 * dy3
            if (distance_squared3 <= 61 * 61) {
                if (distance_squared3 <= 25 * 25) {
                    color3 = 5
                } else if (distance_squared3 <= 43 * 43) {
                    color3 = 4
                } else {
                    color3 = 2
                }
                
                if (dx3 < -12 && dy3 < -12 && distance_squared3 < 30 * 30) {
                    color3 = 14
                }
                
                if (distance_squared3 > 44 * 44 && (x3 * 3 + y3) % 13 < 4) {
                    color3 = 5
                }
                
                sun_image.setPixel(x3, y3, color3)
            }
            
            x3 += 1
        }
        y3 += 1
    }
    return sun_image
}

//  ==================================================
//  UPDATE THE MINIMAP
//  ==================================================
function update_minimap() {
    let x4: number;
    
    minimapImage = image.create(MINIMAP_WIDTH, MINIMAP_HEIGHT)
    let y4 = 2
    while (y4 < 42) {
        x4 = 2
        while (x4 < 62) {
            if ((x4 + y4) % 2 == 0) {
                minimapImage.setPixel(x4, y4, 12)
            }
            
            x4 += 1
        }
        y4 += 1
    }
    x4 = 0
    while (x4 < MINIMAP_WIDTH) {
        minimapImage.setPixel(x4, 0, 6)
        minimapImage.setPixel(x4, MINIMAP_HEIGHT - 1, 6)
        x4 += 1
    }
    y4 = 0
    while (y4 < MINIMAP_HEIGHT) {
        minimapImage.setPixel(0, y4, 6)
        minimapImage.setPixel(MINIMAP_WIDTH - 1, y4, 6)
        y4 += 1
    }
    //  ----------------------------------------------
    //  SUN MARKER
    //  ----------------------------------------------
    draw_map_marker(minimapImage, starX, starY, 5, 2)
    //  ----------------------------------------------
    //  PLANET MARKERS
    //  ----------------------------------------------
    planet1WorldX = starX + Math.cos(planetAngle1) * planetRadius1
    planet1WorldY = starY + Math.sin(planetAngle1) * planetRadius1
    planet2WorldX = starX + Math.cos(planetAngle2) * planetRadius2
    planet2WorldY = starY + Math.sin(planetAngle2) * planetRadius2
    planet3WorldX = starX + Math.cos(planetAngle3) * planetRadius3
    planet3WorldY = starY + Math.sin(planetAngle3) * planetRadius3
    draw_map_marker(minimapImage, planet1WorldX, planet1WorldY, 8, 1)
    draw_map_marker(minimapImage, planet2WorldX, planet2WorldY, 4, 1)
    draw_map_marker(minimapImage, planet3WorldX, planet3WorldY, 10, 1)
    //  ----------------------------------------------
    //  ASTEROID MARKERS
    //  ----------------------------------------------
    asteroid1WorldX = starX + Math.cos(angle1) * radius1
    asteroid1WorldY = starY + Math.sin(angle1) * radius1
    asteroid2WorldX = starX + Math.cos(angle2) * radius2
    asteroid2WorldY = starY + Math.sin(angle2) * radius2
    asteroid3WorldX = starX + Math.cos(angle3) * radius3
    asteroid3WorldY = starY + Math.sin(angle3) * radius3
    draw_map_marker(minimapImage, asteroid1WorldX, asteroid1WorldY, 13, 0)
    draw_map_marker(minimapImage, asteroid2WorldX, asteroid2WorldY, 13, 0)
    draw_map_marker(minimapImage, asteroid3WorldX, asteroid3WorldY, 13, 0)
    //  ----------------------------------------------
    //  TREASURE CHEST MARKERS
    //  ----------------------------------------------
    let j = 0
    while (j <= TREASURE_COUNT - 1) {
        draw_map_marker(minimapImage, treasureWorldX[j], treasureWorldY[j], 7, 0)
        j += 1
    }
    //  ----------------------------------------------
    //  PLAYER MARKER
    //  ----------------------------------------------
    draw_map_marker(minimapImage, shipWorldX, shipWorldY, 9, 2)
    //  Put the updated image on the minimap sprite.
    minimapSprite.setImage(minimapImage)
    minimapSprite.setPosition(MINIMAP_SCREEN_X, MINIMAP_SCREEN_Y)
}

//  ==================================================
//  RESPAWN TREASURE CHESTS
//  ==================================================
function respawn_chest(index: number) {
    let dxShip: number;
    let dyShip: number;
    let dxSun: number;
    let dySun: number;
    let minimumSunDistance: number;
    let k: number;
    let dxChest: number;
    let dyChest: number;
    
    //  Reset these for EVERY respawn. Without this, later respawns can
    //  reuse an old position because validPosition stays True.
    validPosition = false
    attempts = 0
    while (validPosition == false && attempts < 100) {
        candidateX = randint(150, WORLD_WIDTH - 150)
        candidateY = randint(150, WORLD_HEIGHT - 150)
        validPosition = true
        //  Keep the chest away from the ship.
        dxShip = candidateX - shipWorldX
        dyShip = candidateY - shipWorldY
        if (dxShip * dxShip + dyShip * dyShip < 350 * 350) {
            validPosition = false
        }
        
        //  Keep the chest away from the sun.
        dxSun = candidateX - starX
        dySun = candidateY - starY
        minimumSunDistance = STAR_DEATH_RADIUS + 300
        if (dxSun * dxSun + dySun * dySun < minimumSunDistance * minimumSunDistance) {
            validPosition = false
        }
        
        //  Keep treasure chests separated.
        k = 0
        while (k <= TREASURE_COUNT - 1) {
            if (k != index) {
                dxChest = candidateX - treasureWorldX[k]
                dyChest = candidateY - treasureWorldY[k]
                if (dxChest * dxChest + dyChest * dyChest < 300 * 300) {
                    validPosition = false
                }
                
            }
            
            k += 1
        }
        attempts += 1
    }
    if (validPosition == false) {
        candidateX = randint(150, WORLD_WIDTH - 150)
        candidateY = randint(150, WORLD_HEIGHT - 150)
    }
    
    treasureWorldX[index] = candidateX
    treasureWorldY[index] = candidateY
    //  Move the chest away immediately.
    treasureSprites[index].setPosition(candidateX - shipWorldX + SCREEN_CENTER_X, candidateY - shipWorldY + SCREEN_CENTER_Y)
}

//  ==================================================
//  TREASURE COLLECTION
//  ==================================================
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    if (gameEnded) {
        return
    }
    
    let l = 0
    while (l <= TREASURE_COUNT - 1) {
        if (treasureSprites[l] == otherSprite) {
            //  Award exactly one point.
            info.changeScoreBy(1)
            //  Immediately move this chest elsewhere.
            respawn_chest(l)
            break
        }
        
        l += 1
    }
})
//  ==================================================
//  DRAW A MARKER ON THE MINIMAP
//  ==================================================
function draw_map_marker(map_image: Image, world_x: number, world_y: number, color2: number, marker_radius: number) {
    let dy4: number;
    let pixel_x: number;
    let pixel_y: number;
    
    //  Convert world coordinates into minimap pixels.
    map_x = 2 + Math.round(world_x * 59 / WORLD_WIDTH)
    map_y = 2 + Math.round(world_y * 39 / WORLD_HEIGHT)
    let dx4 = 0 - marker_radius
    while (dx4 < marker_radius + 1) {
        dy4 = 0 - marker_radius
        while (dy4 < marker_radius + 1) {
            if (dx4 * dx4 + dy4 * dy4 <= marker_radius * marker_radius) {
                pixel_x = map_x + dx4
                pixel_y = map_y + dy4
                //  Keep markers inside the map border.
                if (pixel_x >= 1 && pixel_x <= 62) {
                    if (pixel_y >= 1 && pixel_y <= 42) {
                        map_image.setPixel(pixel_x, pixel_y, color2)
                    }
                    
                }
                
            }
            
            dy4 += 1
        }
        dx4 += 1
    }
}

//  ==================================================
//  RINGED PLANET IMAGE
//  ==================================================
function make_ringed_planet_image(): Image {
    let x2: number;
    let dx2: number;
    let dy2: number;
    let ellipse: any;
    let distance_squared2: any;
    let color22: number;
    
    size2 = 120
    center2 = 60
    ring_image = image.create(size2, size2)
    let y2 = 0
    while (y2 < size2) {
        x2 = 0
        while (x2 < size2) {
            dx2 = x2 - center2
            dy2 = y2 - center2
            ellipse = Math.idiv(dx2 * dx2 * 100, 54 * 54) + Math.idiv(dy2 * dy2 * 100, 19 * 19)
            if (ellipse >= 80 && ellipse <= 120) {
                if (dx2 < 0) {
                    ring_image.setPixel(x2, y2, 13)
                } else {
                    ring_image.setPixel(x2, y2, 5)
                }
                
            }
            
            x2 += 1
        }
        y2 += 1
    }
    y2 = 0
    while (y2 < size2) {
        x2 = 0
        while (x2 < size2) {
            dx2 = x2 - center2
            dy2 = y2 - center2
            distance_squared2 = dx2 * dx2 + dy2 * dy2
            if (distance_squared2 <= 34 * 34) {
                color22 = 4
                if (y2 % 9 < 3) {
                    color22 = 5
                }
                
                if (dx2 < -10 && dy2 < 5) {
                    color22 = 14
                } else if (dx2 > 10) {
                    color22 = 13
                }
                
                ring_image.setPixel(x2, y2, color22)
            }
            
            x2 += 1
        }
        y2 += 1
    }
    return ring_image
}

//  ==================================================
//  ASTEROID DAMAGE
//  ==================================================
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap2(sprite2: Sprite, otherSprite2: Sprite) {
    
    if (gameEnded == false && game.runtime() >= nextDamageTime) {
        shipHP += 0 - 20
        if (shipHP < 0) {
            shipHP = 0
        }
        
        lastDamageTime = game.runtime()
        nextDamageTime = lastDamageTime + 1000
        health_bar.setImage(make_health_bar_image())
        health_bar.setFlag(SpriteFlag.Invisible, false)
        healthBarVisible = true
        if (shipHP <= 0) {
            gameEnded = true
            shipVX = 0
            shipVY = 0
            mySprite.startEffect(effects.disintegrate, 500)
            pause(500)
            game.setGameOverMessage(false, "SHIP DESTROYED!")
            game.gameOver(false)
        }
        
    }
    
})
let sunDistance = 0
let acceleration = 0
let shipVY = 0
let shipVX = 0
let healthBarVisible = false
let lastDamageTime = 0
let nextDamageTime = 0
let ring_image : Image = null
let center2 = 0
let size2 = 0
let map_y = 0
let map_x = 0
let gameEnded = false
let candidateY = 0
let candidateX = 0
let attempts = 0
let validPosition = false
let asteroid3WorldY = 0
let asteroid3WorldX = 0
let asteroid2WorldY = 0
let asteroid2WorldX = 0
let asteroid1WorldY = 0
let angle1 = 0
let asteroid1WorldX = 0
let planet3WorldY = 0
let planet3WorldX = 0
let planet2WorldY = 0
let planet2WorldX = 0
let planet1WorldY = 0
let planet1WorldX = 0
let minimapImage : Image = null
let sun_image : Image = null
let center3 = 0
let size22 = 0
let bar_width = 0
let bar_image : Image = null
let asteroid : Sprite = null
let center = 0
let planet_image : Image = null
let minimapSprite : Sprite = null
let MINIMAP_SCREEN_Y = 0
let MINIMAP_SCREEN_X = 0
let MINIMAP_HEIGHT = 0
let MINIMAP_WIDTH = 0
let health_bar : Sprite = null
let TREASURE_COUNT = 0
let mySprite : Sprite = null
let radius3 = 0
let radius2 = 0
let radius1 = 0
let angle3 = 0
let angle2 = 0
let planetRadius3 = 0
let planetRadius2 = 0
let planetRadius1 = 0
let planetAngle3 = 0
let planetAngle2 = 0
let planetAngle1 = 0
let STAR_DEATH_RADIUS = 0
let starY = 0
let starX = 0
let shipWorldY = 0
let shipWorldX = 0
let maxHP = 0
let shipHP = 0
let SCREEN_CENTER_Y = 0
let SCREEN_CENTER_X = 0
let WORLD_HEIGHT = 0
let WORLD_WIDTH = 0
let treasureWorldY : number[] = []
let treasureWorldX : number[] = []
let treasureSprites : Sprite[] = []
let ufoSprites : Sprite[] = []
let ufoDisabledUntil = [0, 0, 0]
//  A: tap = 3-second boost; hold 0.45 seconds and release = 1000-pixel hyperjump.
//  Both A abilities share a 15-second cooldown.
let boostUntil = 0
let boostCooldownUntil = 0
let aPressStart = 0
let aPressAllowed = false
let aHolding = false
let warpFlashUntil = 0
//  B: hold to charge a capped orb; release = non-damaging UFO-disabling pulse.
//  The pulse has a 0.5-second cooldown.
let attackCharging = false
let attackChargeStart = 0
let attackChargeLevel = 0
let attackCooldownUntil = 0
let attackPulseUntil = 0
let attackPulseRange = 0
//  Visual ability sprites and images
let chargeOrbImages : Image[] = []
let pulseImages : Image[] = []
let warpImages : Image[] = []
let chargeOrbSprite : Sprite = null
let pulseSprite : Sprite = null
let warpSprite : Sprite = null
let hudImage : Image = null
let hudSprite : Sprite = null
//  ==================================================
//  ABILITY VISUALS AND HUD FONT
//  ==================================================
function make_charge_orb_image(radius: number): Image {
    let x: number;
    let dx: number;
    let dy: number;
    let distanceSquared: any;
    let orbColor: number;
    let size = radius * 2 + 1
    let centre = radius
    let orbImage = image.create(size, size)
    let y = 0
    while (y < size) {
        x = 0
        while (x < size) {
            dx = x - centre
            dy = y - centre
            distanceSquared = dx * dx + dy * dy
            if (distanceSquared <= radius * radius) {
                if (distanceSquared <= (radius - 2) * (radius - 2)) {
                    orbColor = 1
                } else if (distanceSquared <= (radius - 1) * (radius - 1)) {
                    orbColor = 9
                } else {
                    orbColor = 13
                }
                
                orbImage.setPixel(x, y, orbColor)
            }
            
            x += 1
        }
        y += 1
    }
    return orbImage
}

function make_pulse_image(radius: number): Image {
    let x: number;
    let dx: number;
    let dy: number;
    let distanceSquared: any;
    let size = radius * 2 + 1
    let centre = radius
    let pulseImage = image.create(size, size)
    let y = 0
    while (y < size) {
        x = 0
        while (x < size) {
            dx = x - centre
            dy = y - centre
            distanceSquared = dx * dx + dy * dy
            if (distanceSquared <= radius * radius && distanceSquared >= (radius - 2) * (radius - 2)) {
                pulseImage.setPixel(x, y, 9)
            } else if (distanceSquared <= (radius - 6) * (radius - 6) && distanceSquared >= (radius - 8) * (radius - 8)) {
                pulseImage.setPixel(x, y, 12)
            }
            
            x += 1
        }
        y += 1
    }
    return pulseImage
}

function make_warp_image(frame: number): Image {
    let x: number;
    let dx: number;
    let dy: number;
    let distanceSquared: any;
    let pattern: any;
    let size = 49
    let centre = 24
    let warpImage = image.create(size, size)
    let y = 0
    while (y < size) {
        x = 0
        while (x < size) {
            dx = x - centre
            dy = y - centre
            distanceSquared = dx * dx + dy * dy
            if (distanceSquared >= 11 * 11 && distanceSquared <= 22 * 22) {
                pattern = (x * 2 + y * 3 + frame * 5) % 13
                if (pattern < 4) {
                    warpImage.setPixel(x, y, 9)
                } else if (pattern < 7) {
                    warpImage.setPixel(x, y, 13)
                }
                
            } else if (distanceSquared >= 7 * 7 && distanceSquared <= 9 * 9) {
                warpImage.setPixel(x, y, 1)
            }
            
            x += 1
        }
        y += 1
    }
    return warpImage
}

function tiny_glyph(character: string): string[] {
    let blank = ["000", "000", "000", "000", "000"]
    if (character == "A") {
        return ["010", "101", "111", "101", "101"]
    }
    
    if (character == "B") {
        return ["110", "101", "110", "101", "110"]
    }
    
    if (character == "C") {
        return ["011", "100", "100", "100", "011"]
    }
    
    if (character == "D") {
        return ["110", "101", "101", "101", "110"]
    }
    
    if (character == "E") {
        return ["111", "100", "110", "100", "111"]
    }
    
    if (character == "K") {
        return ["101", "101", "110", "101", "101"]
    }
    
    if (character == "O") {
        return ["010", "101", "101", "101", "010"]
    }
    
    if (character == "R") {
        return ["110", "101", "110", "101", "101"]
    }
    
    if (character == "S") {
        return ["011", "100", "010", "001", "110"]
    }
    
    if (character == "T") {
        return ["111", "010", "010", "010", "010"]
    }
    
    if (character == "Y") {
        return ["101", "101", "010", "010", "010"]
    }
    
    if (character == "0") {
        return ["111", "101", "101", "101", "111"]
    }
    
    if (character == "1") {
        return ["010", "110", "010", "010", "111"]
    }
    
    if (character == "2") {
        return ["110", "001", "010", "100", "111"]
    }
    
    if (character == "3") {
        return ["110", "001", "010", "001", "110"]
    }
    
    if (character == "4") {
        return ["101", "101", "111", "001", "001"]
    }
    
    if (character == "5") {
        return ["111", "100", "110", "001", "110"]
    }
    
    if (character == "6") {
        return ["011", "100", "110", "101", "010"]
    }
    
    if (character == "7") {
        return ["111", "001", "010", "010", "010"]
    }
    
    if (character == "8") {
        return ["010", "101", "010", "101", "010"]
    }
    
    if (character == "9") {
        return ["010", "101", "011", "001", "110"]
    }
    
    if (character == ":") {
        return ["000", "010", "000", "010", "000"]
    }
    
    if (character == ".") {
        return ["000", "000", "000", "000", "010"]
    }
    
    return blank
}

function draw_tiny_text(target: Image, textValue: string, startX: number, startY: number, color: number) {
    let glyph: string[];
    let row: number;
    let column: number;
    let charIndex = 0
    while (charIndex < textValue.length) {
        glyph = tiny_glyph(textValue[charIndex])
        row = 0
        while (row < 5) {
            column = 0
            while (column < 3) {
                if (glyph[row][column] == "1") {
                    target.setPixel(startX + charIndex * 4 + column, startY + row, color)
                }
                
                column += 1
            }
            row += 1
        }
        charIndex += 1
    }
}

function time_label(milliseconds: number) {
    if (milliseconds < 0) {
        milliseconds = 0
    }
    
    let tenths = Math.idiv(milliseconds + 99, 100)
    return "" + Math.idiv(tenths, 10) + "." + ("" + tenths % 10) + "S"
}

function facing_x(): number {
    let direction = mySprite.rotationDegrees
    if (direction == 90) {
        return 1
    } else if (direction == -90 || direction == 270) {
        return -1
    }
    
    return 0
}

function facing_y(): number {
    let direction = mySprite.rotationDegrees
    if (direction == 180) {
        return 1
    } else if (direction == 0) {
        return -1
    }
    
    return 0
}

function perform_hyperjump() {
    
    
    let directionX = facing_x()
    let directionY = facing_y()
    let destinationX = shipWorldX + directionX * 1000
    let destinationY = shipWorldY + directionY * 1000
    //  Wrap to the opposite edge if the 1000-pixel jump crosses a border.
    shipWorldX = 10 + (destinationX - 10) % (WORLD_WIDTH - 20)
    shipWorldY = 10 + (destinationY - 10) % (WORLD_HEIGHT - 20)
    shipVX = directionX * 0.8
    shipVY = directionY * 0.8
    boostUntil = 0
    boostCooldownUntil = game.runtime() + 15000
    warpFlashUntil = game.runtime() + 550
}

//  ==================================================
//  SPACE TREASURE COLLECTOR
//  EXPANDED SOLAR SYSTEM + LIVE MINIMAP
//  ==================================================
//  WORLD SETTINGS
WORLD_WIDTH = 7000
WORLD_HEIGHT = 5000
SCREEN_CENTER_X = 80
SCREEN_CENTER_Y = 60
//  ==================================================
//  GAME VARIABLES
//  ==================================================
let shipSpeed = 20
shipHP = 100
maxHP = 100
shipWorldX = 1330
shipWorldY = 1550
let MAX_SHIP_VELOCITY = 3
//  ==================================================
//  CINEMATIC ENDING VARIABLES
//  ==================================================
let mothershipSprite : Sprite = null
let chargeBarSprite : Sprite = null
let endingState = 0
let endingTimer = 0
let explosionIndex = 0
let redLevel = 0
let starCharge = 0
let collapseFrame = 0
let bWasDown = false
let restartArmed = false
//  Ending states
let ENDING_NORMAL = 0
let ENDING_MOTHERSHIP_FALL = 1
let ENDING_BOSS_EXPLOSION = 2
let ENDING_STAR_CHARGE = 3
let ENDING_STAR_COLLAPSE = 4
let ENDING_BLACK_HOLE = 5
let ENDING_DARKNESS_CHOICE = 6
let ENDING_STAY_IN_DARKNESS = 7
//  ==================================================
//  SOLAR SYSTEM
//  ==================================================
starX = 3500
starY = 2500
STAR_DEATH_RADIUS = 100
//  Planet orbit angles
planetAngle1 = 0.8
planetAngle2 = 5.2
planetAngle3 = 3.55
//  Planet orbit speeds
let planetSpeed1 = 0.002
let planetSpeed2 = 0.0013
let planetSpeed3 = 0.0008
//  Planet orbit distances
planetRadius1 = 750
planetRadius2 = 1450
planetRadius3 = 2300
angle2 = 2.8
angle3 = 4.8
//  Asteroid orbit speeds
let orbitSpeed1 = 0.015
let orbitSpeed2 = 0.011
let orbitSpeed3 = 0.008
//  Asteroid orbit distances
radius1 = 160
radius2 = 280
radius3 = 400
//  ==================================================
//  BACKGROUND
//  ==================================================
//  BLACK SPACE BACKGROUND WITH A SPARSE WHITE STARFIELD
//  This is a background image, not sprite objects, so it will not
//  interfere with treasure, asteroid, or UFO collisions.
let spaceBackground = image.create(160, 120)
spaceBackground.fill(15)
let starDot = 0
while (starDot < 85) {
    starXPixel = randint(0, 159)
    starYPixel = randint(0, 119)
    starColour = 1
    if (starDot % 3 == 0) {
        starColour = 12
    } else if (starDot % 5 == 0) {
        starColour = 13
    }
    
    spaceBackground.setPixel(starXPixel, starYPixel, starColour)
    starDot += 1
}
scene.setBackgroundImage(spaceBackground)
//  ==================================================
//  RED GRADIENT BACKGROUND
//  ==================================================
function set_red_gradient(level: number) {
    let rowLevel: number;
    let colour: number;
    let backgroundImage = image.create(160, 120)
    let y = 0
    while (y < 120) {
        rowLevel = Math.idiv(y * 100, 120)
        if (rowLevel < level) {
            if (rowLevel < 30) {
                colour = 14
            } else if (rowLevel < 70) {
                colour = 2
            } else {
                colour = 4
            }
            
        } else {
            colour = 15
        }
        
        backgroundImage.fillRect(0, y, 160, 1, colour)
        y += 1
    }
    scene.setBackgroundImage(backgroundImage)
}

//  ==================================================
//  STAR AND BLACK HOLE IMAGES
//  ==================================================
function make_ending_core_image(radius: number, blackHole: boolean): Image {
    let x: number;
    let dx: number;
    let dy: number;
    let distanceSquared: any;
    let colour: number;
    let size = radius * 2 + 2
    let centre = radius + 1
    let coreImage = image.create(size, size)
    let y = 0
    while (y < size) {
        x = 0
        while (x < size) {
            dx = x - centre
            dy = y - centre
            distanceSquared = dx * dx + dy * dy
            if (distanceSquared <= radius * radius) {
                if (blackHole) {
                    if (distanceSquared > (radius - 5) * (radius - 5)) {
                        colour = 10
                    } else if (distanceSquared > 9 * 9) {
                        colour = 11
                    } else {
                        colour = 15
                    }
                    
                } else if (distanceSquared > (radius - 6) * (radius - 6)) {
                    colour = 5
                } else if (distanceSquared > Math.idiv(radius, 2) * Math.idiv(radius, 2)) {
                    colour = 4
                } else {
                    colour = 2
                }
                
                coreImage.setPixel(x, y, colour)
            }
            
            x += 1
        }
        y += 1
    }
    return coreImage
}

//  ==================================================
//  EXPLOSION IMAGE
//  ==================================================
function make_ending_explosion(radius: number): Image {
    let x: number;
    let dx: number;
    let dy: number;
    let colour: number;
    let size = radius * 2 + 1
    let centre = radius
    let explosionImage = image.create(size, size)
    let y = 0
    while (y < size) {
        x = 0
        while (x < size) {
            dx = x - centre
            dy = y - centre
            if (dx * dx + dy * dy <= radius * radius) {
                colour = 4
                if (Math.abs(dx) <= 1 || Math.abs(dy) <= 1) {
                    colour = 5
                } else if (Math.abs(dx - dy) <= 1 || Math.abs(dx + dy) <= 1) {
                    colour = 5
                }
                
                explosionImage.setPixel(x, y, colour)
            }
            
            x += 1
        }
        y += 1
    }
    return explosionImage
}

function create_ending_explosion(x: number, y: number, radius: number) {
    let flash = sprites.create(make_ending_explosion(radius), SpriteKind.Projectile)
    flash.setPosition(x, y)
    flash.z = 220
    flash.lifespan = 350
    flash.startEffect(effects.fire, 250)
}

//  ==================================================
//  SPACESHIP
//  ==================================================
mySprite = sprites.create(assets.image`
    ship
    `, SpriteKind.Player)
mySprite.setPosition(SCREEN_CENTER_X, SCREEN_CENTER_Y)
//  Ship is above planets and asteroids.
mySprite.z = 100
//  ==================================================
//  TREASURE CHEST IMAGE
//  ==================================================
let treasureImage = img`
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
    `
//  ==================================================
//  TEN TREASURE CHESTS
//  ==================================================
TREASURE_COUNT = 10
let initialTreasureX = [1270, 400, 2100, 3400, 6500, 6500, 4600, 1600, 300, 3600]
let initialTreasureY = [1560, 400, 450, 300, 800, 4400, 4600, 4400, 2800, 3700]
let i = 0
while (i < TREASURE_COUNT) {
    chest = sprites.create(treasureImage, SpriteKind.Food)
    chest.z = 40
    treasureSprites.push(chest)
    treasureWorldX.push(initialTreasureX[i])
    treasureWorldY.push(initialTreasureY[i])
    chest.setPosition(initialTreasureX[i] - shipWorldX + SCREEN_CENTER_X, initialTreasureY[i] - shipWorldY + SCREEN_CENTER_Y)
    i += 1
}
health_bar = sprites.create(make_health_bar_image(), SpriteKind.Projectile)
health_bar.setFlag(SpriteFlag.Ghost, true)
health_bar.setFlag(SpriteFlag.Invisible, true)
health_bar.z = 200
function start_victory_sequence() {
    
    
    
    if (endingState != ENDING_NORMAL) {
        return
    }
    
    gameEnded = true
    shipVX = 0
    shipVY = 0
    endingState = ENDING_MOTHERSHIP_FALL
    endingTimer = 0
    explosionIndex = 0
    redLevel = 0
    starCharge = 0
}

//  ==================================================
//  PLANETS
//  ==================================================
let planet1 = sprites.create(make_planet_image(96, 44, 8, 7, 1, 12, 1), SpriteKind.Projectile)
let planet2 = sprites.create(make_ringed_planet_image(), SpriteKind.Projectile)
let planet3 = sprites.create(make_planet_image(100, 46, 10, 9, 1, 12, 3), SpriteKind.Projectile)
planet1.setFlag(SpriteFlag.Ghost, true)
planet2.setFlag(SpriteFlag.Ghost, true)
planet3.setFlag(SpriteFlag.Ghost, true)
planet1.z = 10
planet2.z = 10
planet3.z = 10
//  ==================================================
//  CENTRAL SUN
//  ==================================================
let centralStar = sprites.create(make_sun_image(), SpriteKind.Projectile)
centralStar.setFlag(SpriteFlag.Ghost, true)
centralStar.z = 0
let asteroid1 = create_asteroid(1)
let asteroid2 = create_asteroid(2)
let asteroid3 = create_asteroid(3)
//  ==================================================
//  FLYING UFOs
//  ==================================================
let ufoImage = img`
    . . . . . . 8 8 8 8 . . . . . .
    . . . 8 8 8 9 9 9 9 8 8 8 . . .
    . . 8 9 9 9 9 9 9 9 9 9 9 8 . .
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    . . . 8 8 8 8 8 8 8 8 8 8 . . .
    . . . . . 8 . . . . 8 . . . . .
    `
let UFO_COUNT = 3
//  Each UFO loops around its own nearby point, at a different speed.
let ufoCentreX = [1365, 1450, 1500]
let ufoCentreY = [1500, 1500, 1600]
let ufoRadiusX = [55, 80, 100]
let ufoRadiusY = [35, 50, 55]
let ufoStartAngle = [0, 1.57, 3.14]
let ufoOrbitSpeed = [0.00036, 0.00031, 0.00025]
let ufoIndex = 0
while (ufoIndex < UFO_COUNT) {
    flyingUfo = sprites.create(ufoImage, SpriteKind.Enemy)
    flyingUfo.z = 35
    //  Place each UFO away from the ship before the first game update.
    initialAngle = game.runtime() * ufoOrbitSpeed[ufoIndex] + ufoStartAngle[ufoIndex]
    initialUfoX = ufoCentreX[ufoIndex] + Math.cos(initialAngle) * ufoRadiusX[ufoIndex]
    initialUfoY = ufoCentreY[ufoIndex] + Math.sin(initialAngle) * ufoRadiusY[ufoIndex]
    flyingUfo.setPosition(initialUfoX - shipWorldX + SCREEN_CENTER_X, initialUfoY - shipWorldY + SCREEN_CENTER_Y)
    ufoSprites.push(flyingUfo)
    ufoIndex += 1
}
//  ==================================================
//  CHARGED B PULSE
//  Hold B to charge a glowing orb. Releasing B sends a
//  non-damaging defensive pulse around the ship.
//  ==================================================
chargeOrbImages = [make_charge_orb_image(3), make_charge_orb_image(4), make_charge_orb_image(5), make_charge_orb_image(6), make_charge_orb_image(7), make_charge_orb_image(8)]
pulseImages = [make_pulse_image(12), make_pulse_image(15), make_pulse_image(18), make_pulse_image(21), make_pulse_image(24), make_pulse_image(27)]
warpImages = [make_warp_image(0), make_warp_image(1), make_warp_image(2), make_warp_image(3)]
chargeOrbSprite = sprites.create(chargeOrbImages[0], SpriteKind.Projectile)
chargeOrbSprite.setFlag(SpriteFlag.Ghost, true)
chargeOrbSprite.setFlag(SpriteFlag.RelativeToCamera, true)
chargeOrbSprite.setFlag(SpriteFlag.Invisible, true)
chargeOrbSprite.z = 160
pulseSprite = sprites.create(pulseImages[0], SpriteKind.Projectile)
pulseSprite.setFlag(SpriteFlag.Ghost, true)
pulseSprite.setFlag(SpriteFlag.RelativeToCamera, true)
pulseSprite.setFlag(SpriteFlag.Invisible, true)
pulseSprite.setPosition(SCREEN_CENTER_X, SCREEN_CENTER_Y)
pulseSprite.z = 150
warpSprite = sprites.create(warpImages[0], SpriteKind.Projectile)
warpSprite.setFlag(SpriteFlag.Ghost, true)
warpSprite.setFlag(SpriteFlag.RelativeToCamera, true)
warpSprite.setFlag(SpriteFlag.Invisible, true)
warpSprite.setPosition(SCREEN_CENTER_X, SCREEN_CENTER_Y)
warpSprite.z = 90
//  Small pixel-font HUD avoids requiring another extension.
hudImage = image.create(100, 16)
hudImage.fill(15)
hudSprite = sprites.create(hudImage, SpriteKind.Projectile)
hudSprite.setFlag(SpriteFlag.Ghost, true)
hudSprite.setFlag(SpriteFlag.RelativeToCamera, true)
hudSprite.setPosition(50, 9)
hudSprite.z = 260
controller.B.onEvent(ControllerButtonEvent.Pressed, function on_b_pressed() {
    
    if (gameEnded || endingState != ENDING_NORMAL) {
        return
    }
    
    if (attackCharging || game.runtime() < attackCooldownUntil) {
        return
    }
    
    attackCharging = true
    attackChargeStart = game.runtime()
    attackChargeLevel = 0
    chargeOrbSprite.setImage(chargeOrbImages[0])
    chargeOrbSprite.setFlag(SpriteFlag.Invisible, false)
})
controller.B.onEvent(ControllerButtonEvent.Released, function on_b_released() {
    let ufoAngle: number;
    let nearbyUfoX: number;
    let nearbyUfoY: number;
    let dxUfo: number;
    let dyUfo: number;
    
    
    if (!attackCharging) {
        return
    }
    
    let now = game.runtime()
    attackCharging = false
    attackChargeLevel = Math.idiv(now - attackChargeStart, 400)
    if (attackChargeLevel > chargeOrbImages.length - 1) {
        attackChargeLevel = chargeOrbImages.length - 1
    }
    
    attackPulseRange = 120 + attackChargeLevel * 30
    attackPulseUntil = now + 450
    attackCooldownUntil = now + 500
    chargeOrbSprite.setFlag(SpriteFlag.Invisible, true)
    pulseSprite.setImage(pulseImages[attackChargeLevel])
    pulseSprite.setPosition(SCREEN_CENTER_X, SCREEN_CENTER_Y)
    pulseSprite.setFlag(SpriteFlag.Invisible, false)
    //  The pulse briefly disables any UFOs close enough to the ship.
    let ufoIndex = 0
    while (ufoIndex < UFO_COUNT) {
        ufoAngle = now * ufoOrbitSpeed[ufoIndex] + ufoStartAngle[ufoIndex]
        nearbyUfoX = ufoCentreX[ufoIndex] + Math.cos(ufoAngle) * ufoRadiusX[ufoIndex]
        nearbyUfoY = ufoCentreY[ufoIndex] + Math.sin(ufoAngle) * ufoRadiusY[ufoIndex]
        dxUfo = nearbyUfoX - shipWorldX
        dyUfo = nearbyUfoY - shipWorldY
        if (dxUfo * dxUfo + dyUfo * dyUfo <= attackPulseRange * attackPulseRange) {
            ufoDisabledUntil[ufoIndex] = now + 2200
        }
        
        ufoIndex += 1
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    if (gameEnded || endingState != ENDING_NORMAL) {
        return
    }
    
    let now = game.runtime()
    aPressStart = now
    aPressAllowed = now >= boostCooldownUntil
    aHolding = aPressAllowed
    if (aHolding) {
        warpSprite.setFlag(SpriteFlag.Invisible, false)
    }
    
})
controller.A.onEvent(ControllerButtonEvent.Released, function on_a_released() {
    
    let now = game.runtime()
    let heldFor = now - aPressStart
    let wasAllowed = aPressAllowed
    aHolding = false
    if (!wasAllowed || gameEnded || endingState != ENDING_NORMAL) {
        warpSprite.setFlag(SpriteFlag.Invisible, true)
        return
    }
    
    if (heldFor >= 450) {
        perform_hyperjump()
    } else {
        //  A quick tap starts a three-second speed boost.
        boostUntil = now + 3000
        boostCooldownUntil = boostUntil + 15000
        warpFlashUntil = now + 200
    }
    
    warpSprite.setFlag(SpriteFlag.Invisible, false)
})
game.onUpdateInterval(100, function update_ability_hud() {
    let boostText: string;
    let attackText: string;
    let now = game.runtime()
    hudImage.fill(15)
    if (now < boostUntil) {
        boostText = "BOOST: " + time_label(boostUntil - now)
    } else if (now < boostCooldownUntil) {
        boostText = "BOOST CD: " + time_label(boostCooldownUntil - now)
    } else {
        boostText = "BOOST CD: READY"
    }
    
    if (now < attackCooldownUntil) {
        attackText = "ATK CD: " + time_label(attackCooldownUntil - now)
    } else {
        attackText = "ATK CD: READY"
    }
    
    draw_tiny_text(hudImage, boostText, 2, 1, 9)
    draw_tiny_text(hudImage, attackText, 2, 9, 12)
    hudSprite.setImage(hudImage)
})
//  ==================================================
//  MINIMAP SETTINGS
//  ==================================================
MINIMAP_WIDTH = 64
MINIMAP_HEIGHT = 44
MINIMAP_SCREEN_X = 124
MINIMAP_SCREEN_Y = 96
//  Create the minimap display sprite.
minimapSprite = sprites.create(image.create(MINIMAP_WIDTH, MINIMAP_HEIGHT), SpriteKind.Projectile)
minimapSprite.setFlag(SpriteFlag.Ghost, true)
//  Keep the minimap fixed on the screen.
minimapSprite.setFlag(SpriteFlag.RelativeToCamera, true)
minimapSprite.setPosition(MINIMAP_SCREEN_X, MINIMAP_SCREEN_Y)
//  Draw it above the game world and health bar.
minimapSprite.z = 250
game.onUpdateInterval(500, update_minimap)
//  Draw the first map immediately.
update_minimap()
//  ==================================================
//  START GAME
//  ==================================================
info.setScore(0)
//  ==================================================
//  WORLD UPDATE AND CAMERA
//  ==================================================
game.onUpdate(function on_on_update() {
    let warpFrame: number;
    let facingX: number;
    let facingY: number;
    let currentMaxVelocity: number;
    let ufoAngle: number;
    let ufoWorldX: number;
    let ufoWorldY: number;
    
    if (gameEnded) {
        return
    }
    
    //  ----------------------------------------------
    //  SHIP DIRECTION
    //  ----------------------------------------------
    if (controller.right.isPressed() && !controller.left.isPressed()) {
        mySprite.rotationDegrees = 90
    } else if (controller.left.isPressed() && !controller.right.isPressed()) {
        mySprite.rotationDegrees = -90
    } else if (controller.down.isPressed() && !controller.up.isPressed()) {
        mySprite.rotationDegrees = 180
    } else if (controller.up.isPressed() && !controller.down.isPressed()) {
        mySprite.rotationDegrees = 0
    }
    
    //  ----------------------------------------------
    //  A-BUTTON WORMHOLE VISUAL WHILE HELD
    //  ----------------------------------------------
    let abilityNow = game.runtime()
    if (aHolding) {
        warpFrame = Math.idiv(abilityNow, 100) % warpImages.length
        warpSprite.setImage(warpImages[warpFrame])
        warpSprite.rotationDegrees = Math.idiv(abilityNow, 8) % 360
        warpSprite.setPosition(SCREEN_CENTER_X, SCREEN_CENTER_Y)
        warpSprite.setFlag(SpriteFlag.Invisible, false)
    } else if (abilityNow >= warpFlashUntil) {
        warpSprite.setFlag(SpriteFlag.Invisible, true)
    }
    
    //  ----------------------------------------------
    //  B-BUTTON CHARGE ORB GROWS WHILE HELD
    //  ----------------------------------------------
    if (attackCharging) {
        attackChargeLevel = Math.idiv(abilityNow - attackChargeStart, 400)
        if (attackChargeLevel > chargeOrbImages.length - 1) {
            attackChargeLevel = chargeOrbImages.length - 1
        }
        
        chargeOrbSprite.setImage(chargeOrbImages[attackChargeLevel])
        facingX = facing_x()
        facingY = facing_y()
        chargeOrbSprite.setPosition(SCREEN_CENTER_X + facingX * 22, SCREEN_CENTER_Y + facingY * 22)
        chargeOrbSprite.setFlag(SpriteFlag.Invisible, false)
    }
    
    if (abilityNow >= attackPulseUntil) {
        pulseSprite.setFlag(SpriteFlag.Invisible, true)
    }
    
    //  ----------------------------------------------
    //  SHIP ACCELERATION (BOOST MAKES THE SHIP FASTER)
    //  ----------------------------------------------
    if (abilityNow < boostUntil) {
        acceleration = shipSpeed / 75
        currentMaxVelocity = 7.5
    } else {
        acceleration = shipSpeed / 200
        currentMaxVelocity = MAX_SHIP_VELOCITY
    }
    
    if (controller.left.isPressed() && !controller.right.isPressed()) {
        shipVX += 0 - acceleration
        if (shipVX < 0 - currentMaxVelocity) {
            shipVX = 0 - currentMaxVelocity
        }
        
    } else if (controller.right.isPressed() && !controller.left.isPressed()) {
        shipVX += acceleration
        if (shipVX > currentMaxVelocity) {
            shipVX = currentMaxVelocity
        }
        
    } else {
        shipVX = shipVX * 0.94
    }
    
    if (controller.up.isPressed() && !controller.down.isPressed()) {
        shipVY += 0 - acceleration
        if (shipVY < 0 - currentMaxVelocity) {
            shipVY = 0 - currentMaxVelocity
        }
        
    } else if (controller.down.isPressed() && !controller.up.isPressed()) {
        shipVY += acceleration
        if (shipVY > currentMaxVelocity) {
            shipVY = currentMaxVelocity
        }
        
    } else {
        shipVY = shipVY * 0.94
    }
    
    //  ----------------------------------------------
    //  MOVE THROUGH THE WORLD
    //  ----------------------------------------------
    shipWorldX += shipVX
    shipWorldY += shipVY
    if (shipWorldX < 10) {
        shipWorldX = 10
        shipVX = 0
    }
    
    if (shipWorldX > WORLD_WIDTH - 10) {
        shipWorldX = WORLD_WIDTH - 10
        shipVX = 0
    }
    
    if (shipWorldY < 10) {
        shipWorldY = 10
        shipVY = 0
    }
    
    if (shipWorldY > WORLD_HEIGHT - 10) {
        shipWorldY = WORLD_HEIGHT - 10
        shipVY = 0
    }
    
    //  ----------------------------------------------
    //  KEEP THE SHIP CENTRED
    //  ----------------------------------------------
    mySprite.setPosition(SCREEN_CENTER_X, SCREEN_CENTER_Y)
    //  ----------------------------------------------
    //  MOVE THE SUN
    //  ----------------------------------------------
    centralStar.setPosition(starX - shipWorldX + SCREEN_CENTER_X, starY - shipWorldY + SCREEN_CENTER_Y)
    //  ----------------------------------------------
    //  PLANET ORBITS
    //  ----------------------------------------------
    planetAngle1 += planetSpeed1
    planetAngle2 += planetSpeed2
    planetAngle3 += planetSpeed3
    spriteutils.placeAngleFrom(planet1, planetAngle1, planetRadius1, centralStar)
    spriteutils.placeAngleFrom(planet2, planetAngle2, planetRadius2, centralStar)
    spriteutils.placeAngleFrom(planet3, planetAngle3, planetRadius3, centralStar)
    //  ----------------------------------------------
    //  ASTEROID ORBITS
    //  ----------------------------------------------
    angle1 += orbitSpeed1
    angle2 += orbitSpeed2
    angle3 += orbitSpeed3
    spriteutils.placeAngleFrom(asteroid1, angle1, radius1, centralStar)
    spriteutils.placeAngleFrom(asteroid2, angle2, radius2, centralStar)
    spriteutils.placeAngleFrom(asteroid3, angle3, radius3, centralStar)
    //  ----------------------------------------------
    //  UFO FLIGHT PATHS AND DISABLE TIMER
    //  ----------------------------------------------
    let ufoNow = game.runtime()
    let ufoIndex = 0
    while (ufoIndex < UFO_COUNT) {
        ufoAngle = ufoNow * ufoOrbitSpeed[ufoIndex] + ufoStartAngle[ufoIndex]
        ufoWorldX = ufoCentreX[ufoIndex] + Math.cos(ufoAngle) * ufoRadiusX[ufoIndex]
        ufoWorldY = ufoCentreY[ufoIndex] + Math.sin(ufoAngle) * ufoRadiusY[ufoIndex]
        ufoSprites[ufoIndex].setPosition(ufoWorldX - shipWorldX + SCREEN_CENTER_X, ufoWorldY - shipWorldY + SCREEN_CENTER_Y)
        if (ufoNow < ufoDisabledUntil[ufoIndex]) {
            ufoSprites[ufoIndex].setFlag(SpriteFlag.Ghost, true)
        } else {
            ufoSprites[ufoIndex].setFlag(SpriteFlag.Ghost, false)
        }
        
        ufoIndex += 1
    }
    //  ----------------------------------------------
    //  TREASURE CHEST POSITIONS
    //  ----------------------------------------------
    let m = 0
    while (m <= TREASURE_COUNT - 1) {
        treasureSprites[m].setPosition(treasureWorldX[m] - shipWorldX + SCREEN_CENTER_X, treasureWorldY[m] - shipWorldY + SCREEN_CENTER_Y)
        m += 1
    }
    //  ----------------------------------------------
    //  SUN DANGER ZONE
    //  ----------------------------------------------
    sunDistance = spriteutils.distanceBetween(mySprite, centralStar)
    if (sunDistance <= STAR_DEATH_RADIUS) {
        gameEnded = true
        shipVX = 0
        shipVY = 0
        mySprite.startEffect(effects.fire, 400)
        pause(250)
        game.setGameOverMessage(false, "BURNED BY THE SUN!")
        game.gameOver(false)
        return
    }
    
    //  ----------------------------------------------
    //  HEALTH BAR
    //  ----------------------------------------------
    health_bar.setPosition(SCREEN_CENTER_X, SCREEN_CENTER_Y - 15)
    pulseSprite.setPosition(SCREEN_CENTER_X, SCREEN_CENTER_Y)
    hudSprite.setPosition(50, 9)
    if (healthBarVisible) {
        if (game.runtime() - lastDamageTime >= 3000) {
            health_bar.setFlag(SpriteFlag.Invisible, true)
            healthBarVisible = false
        }
        
    }
    
})
//  ==================================================
//  GRADUALLY INCREASE SHIP SPEED
//  ==================================================
forever(function on_forever() {
    
    if (!gameEnded && shipSpeed < 60) {
        shipSpeed += 1
    }
    
    pause(500)
})
