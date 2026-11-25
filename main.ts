let mySprite = sprites.create(img`
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
controller.moveSprite(mySprite)
scene.setBackgroundColor(15)
mySprite.setStayInScreen(true)
