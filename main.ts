// =====================================
// BUTTON CONTROLS
// =====================================
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.vy > -60) {
        mySprite.vy += 0 - shipSpeed
    }
})
// =====================================
// ASTEROID CREATION
// =====================================
function create_asteroid () {
    asteroid = sprites.create(img`
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
        `, SpriteKind.Enemy)
    asteroid.setPosition(randint(15, 145), randint(15, 105))
    asteroid.vx = randint(-35, 35)
    asteroid.vy = randint(-35, 35)
    if (asteroid.vx == 0) {
        asteroid.vx = 20
    }
    if (asteroid.vy == 0) {
        asteroid.vy = -20
    }
    asteroid.setFlag(SpriteFlag.BounceOnWall, true)
    return asteroid
}
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.vx > -60) {
        mySprite.vx += 0 - shipSpeed
    }
})
// =====================================
// HEALTH BAR IMAGE
// =====================================
function make_health_bar_image () {
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
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.vx < 60) {
        mySprite.vx += shipSpeed
    }
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.vy < 60) {
        mySprite.vy += shipSpeed
    }
})
// =====================================
// TREASURE COLLECTION
// =====================================
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    treasure.setPosition(randint(8, 152), randint(8, 112))
    while (mySprite.overlapsWith(treasure)) {
        treasure.setPosition(randint(8, 152), randint(8, 112))
    }
    music.play(music.melodyPlayable(music.powerUp), music.PlaybackMode.UntilDone)
})
// =====================================
// ASTEROID COLLISION AND DAMAGE
// =====================================
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
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
        otherSprite.setPosition(randint(8, 152), randint(8, 112))
        if (shipHP <= 0) {
            gameEnded = true
            mySprite.vx = 0
            mySprite.vy = 0
            mySprite.startEffect(effects.disintegrate, 500)
            pause(500)
            game.setGameOverMessage(false, "GAME OVER - PRESS A TO RETRY")
            game.gameOver(false)
        }
    }
})
let healthBarVisible = false
let lastDamageTime = 0
let nextDamageTime = 0
let gameEnded = false
let bar_width = 0
let bar_image: Image = null
let asteroid: Sprite = null
let health_bar: Sprite = null
let treasure: Sprite = null
let mySprite: Sprite = null
let maxHP = 0
let shipHP = 0
let shipSpeed = 0
// =====================================
// SPACE TREASURE COLLECTOR
// =====================================
// Game variables
shipSpeed = 20
shipHP = 100
maxHP = 100
// =====================================
// CREATE SPACESHIP
// =====================================
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
// =====================================
// CREATE TREASURE
// =====================================
treasure = sprites.create(img`
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
    `, SpriteKind.Food)
treasure.setPosition(randint(8, 152), randint(8, 112))
// =====================================
// CREATE HEALTH BAR SPRITE
// =====================================
health_bar = sprites.create(make_health_bar_image(), SpriteKind.Projectile)
health_bar.setFlag(SpriteFlag.Ghost, true)
health_bar.setFlag(SpriteFlag.Invisible, true)
// =====================================
// CREATE ASTEROIDS
// =====================================
let asteroid1 = create_asteroid()
let asteroid2 = create_asteroid()
let asteroid3 = create_asteroid()
// =====================================
// INITIAL SETTINGS
// =====================================
scene.setBackgroundColor(15)
mySprite.setStayInScreen(false)
info.setScore(0)
// =====================================
// MAIN GAME UPDATE
// =====================================
game.onUpdate(function () {
    if (controller.right.isPressed()) {
        mySprite.rotationDegrees = 90
    } else if (controller.left.isPressed()) {
        mySprite.rotationDegrees = -90
    } else if (controller.down.isPressed()) {
        mySprite.rotationDegrees = 180
    } else if (controller.up.isPressed()) {
        mySprite.rotationDegrees = 0
    }
    // Screen wrapping
    if (mySprite.x < 0) {
        mySprite.x = 160
    } else if (mySprite.x > 160) {
        mySprite.x = 0
    }
    if (mySprite.y < 0) {
        mySprite.y = 120
    } else if (mySprite.y > 120) {
        mySprite.y = 0
    }
    // Health bar follows spaceship
    health_bar.x = mySprite.x
    health_bar.y = mySprite.y - 15
    // Hide health bar after 3 seconds
    if (healthBarVisible) {
        if (game.runtime() - lastDamageTime >= 3000) {
            health_bar.setFlag(SpriteFlag.Invisible, true)
            healthBarVisible = false
        }
    }
})
// =====================================
// GRADUALLY INCREASE ACCELERATION
// =====================================
forever(function () {
    if (shipSpeed < 60) {
        shipSpeed += 1
    }
    pause(500)
})
