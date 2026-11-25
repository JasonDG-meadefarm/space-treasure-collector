sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    score += 1
    treasure.setPosition(randint(8, 152), randint(8, 112))
    while (mySprite.overlapsWith(treasure)) {
        treasure.setPosition(randint(8, 152), randint(8, 112))
    }
    music.play(music.melodyPlayable(music.powerUp), music.PlaybackMode.UntilDone)
})
let treasure: Sprite = null
let mySprite: Sprite = null
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
let score = 0
controller.moveSprite(mySprite, 20, 20)
scene.setBackgroundColor(15)
mySprite.setStayInScreen(true)
