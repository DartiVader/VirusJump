    import pygame
    from pygame.locals import *
    from pygame import gfxdraw

    import math
    import random
    import time
    import sys
    import os

    # define display surface
    W, H = 405, 720
    HW, HH = W / 2, H / 2

    # initialise display
    pygame.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "{},{}".format(pygame.display.Info().current_w / 2 - HW, 0)
    DS = pygame.display.set_mode((W, H), NOFRAME, 24)
    CLOCK = pygame.time.Clock()
    pygame.display.set_caption("Virus sucks")
    FPS = 60


    # functions
    def sprite2D(polyData, scale, bkgdColor, colorKey):
        global H

        sprite = pygame.Surface((polyData['width'], polyData['height']), 0, 24)
        sprite.fill(bkgdColor)
        if colorKey:
            sprite.set_colorkey(bkgdColor)

        for poly in polyData['data']:
            # pygame.gfxdraw.aapolygon(self.sprite, poly['points'], poly['color'])
            pygame.gfxdraw.filled_polygon(sprite, poly['points'], poly['color'])

            # pygame.draw.polygon(self.sprite, poly['color'], poly['points'])

        if scale:
            if scale[0] and not scale[1]:
                width = scale[0]
                height = (float(width) / polyData['width']) * polyData['height']
            elif not scale[0] and scale[1]:
                height = scale[1]
                width = (float(height) / polyData['height']) * polyData['width']
            else:
                width = scale[0]
                height = scale[1]
        else:
            width = polyData['width']
            height = polyData['height']

        displayScale = float(H) / 720
        return pygame.transform.scale(sprite, (int(width * displayScale), int(height * displayScale)))


    # exit the program
    def quit():
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return True
        return False


    # define some colors
    FUCHSIA = (255, 0, 255)
    PURPLE = (128, 0, 128)
    TEAL = (0, 128, 128)
    LIME = (0, 255, 0)
    GREEN = (0, 128, 0)
    OLIVE = (128, 128, 0)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 165, 0)
    RED = (255, 0, 0)
    MAROON = (128, 0, 0)
    SILVER = (192, 192, 192)
    GRAY = (128, 128, 128)
    BLUE = (0, 0, 255)
    NAVY = (0, 0, 128)
    AQUA = (0, 255, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # start FPS monitoring
    FPSTime = time.time()

    doodlePoly1 = {'width': 433, 'height': 420, 'data':
        [
            {
                'color': BLACK,
                'points':
                    [[156, 0], [200, 13], [232, 35], [258, 66], [275, 92], [288, 119], [294, 132], [302, 140], [314, 147],
                     [334, 151],
                     [357, 152], [381, 147], [404, 140], [416, 136], [426, 157], [433, 189], [431, 216], [424, 230],
                     [412, 238], [405, 239],
                     [389, 228], [370, 217], [342, 209], [314, 208], [292, 214], [280, 225], [276, 243], [279, 274],
                     [279, 305], [280, 329],
                     [276, 349], [275, 352], [245, 357], [243, 366], [243, 385], [243, 392], [264, 394], [277, 396],
                     [278, 402], [274, 407],
                     [257, 408], [227, 406], [225, 398], [227, 380], [228, 366], [224, 356], [198, 356], [185, 357],
                     [180, 373], [179, 390],
                     [181, 402], [193, 402], [201, 403], [201, 410], [198, 417], [188, 418], [162, 410], [163, 392],
                     [164, 365], [164, 357],
                     [144, 357], [121, 356], [115, 387], [114, 401], [117, 406], [132, 406], [143, 408], [142, 415],
                     [135, 420], [118, 420],
                     [105, 415], [100, 406], [102, 383], [105, 360], [94, 359], [73, 360], [61, 362], [58, 376], [56, 397],
                     [56, 401],
                     [69, 404], [79, 404], [82, 408], [76, 415], [69, 418], [52, 414], [37, 404], [41, 395], [44, 379],
                     [45, 359],
                     [32, 359], [17, 352], [11, 352], [15, 318], [14, 295], [7, 284], [14, 276], [14, 261], [7, 244],
                     [0, 237],
                     [8, 234], [11, 231], [9, 211], [5, 155], [9, 118], [22, 83], [49, 49], [81, 23], [109, 6], [133, 1],
                     [156, 0]]
            },
            {
                'color': (231, 223, 49),
                'points':
                    [[265, 240], [155, 237], [92, 235], [25, 230], [20, 168], [25, 123], [40, 81], [73, 42], [112, 20],
                     [150, 15],
                     [183, 22], [224, 45], [252, 80], [275, 126], [282, 143], [301, 157], [333, 165], [363, 165],
                     [378, 163], [378, 181],
                     [382, 214], [371, 205], [334, 196], [309, 196], [289, 200], [273, 211], [267, 226], [265, 240]]
            },
            {
                'color': (231, 223, 49),
                'points':
                    [[391, 162], [397, 155], [406, 155], [414, 165], [421, 188], [419, 212], [413, 224], [404, 215],
                     [394, 194], [392, 177], [391, 162]]
            },
            {
                'color': BLACK,
                'points':
                    [[196, 126], [205, 122], [213, 124], [215, 137], [212, 146], [205, 148], [197, 142], [196, 135],
                     [196, 126]]

            },
            {
                'color': BLACK,
                'points':
                    [[235, 132], [238, 127], [247, 126], [252, 129], [254, 136], [252, 146], [245, 151], [238, 150],
                     [234, 143], [235, 132]]

            },
            {
                'color': (85, 143, 64),
                'points':
                    [[27, 242], [109, 248], [175, 250], [268, 254], [267, 281], [235, 282], [193, 282], [133, 279],
                     [59, 278], [29, 278], [27, 242]]
            },
            {
                'color': (85, 143, 64),
                'points':
                    [[28, 292], [93, 289], [151, 290], [205, 293], [267, 298], [266, 310], [266, 323], [192, 320],
                     [141, 320], [94, 319],
                     [64, 318], [34, 315], [30, 322], [29, 317], [30, 306], [28, 292]]
            },
            {
                'color': (85, 143, 64),
                'points':
                    [[29, 340], [33, 333], [44, 331], [90, 332], [120, 334], [178, 333], [217, 332], [242, 334], [261, 339],
                     [247, 340],
                     [209, 343], [152, 344], [98, 345], [67, 344], [29, 340]]
            },
        ]
                   }

    doodlePoly2 = {'width': 433, 'height': 390, 'data':
        [
            {
                'color': BLACK,
                'points':
                    [[156, 0], [200, 13], [232, 35], [258, 66], [275, 92], [288, 119], [294, 132], [302, 140], [314, 147],
                     [334, 151],
                     [357, 152], [381, 147], [404, 140], [416, 136], [426, 157], [433, 189], [431, 216], [424, 230],
                     [412, 238], [405, 239],
                     [389, 228], [370, 217], [342, 209], [314, 208], [292, 214], [280, 225], [276, 243], [279, 274],
                     [279, 305], [280, 329],
                     [276, 349], [275, 352], [245, 357], [243, 358], [242, 361], [243, 362], [264, 364], [277, 366],
                     [278, 372], [274, 377],
                     [257, 378], [227, 376], [225, 368], [225, 361], [225, 358], [224, 356], [198, 356], [185, 357],
                     [180, 363], [179, 370],
                     [181, 372], [193, 372], [201, 373], [201, 380], [198, 387], [188, 388], [162, 380], [163, 362],
                     [163, 360], [164, 357],
                     [144, 357], [121, 356], [115, 357], [114, 371], [117, 376], [132, 376], [143, 378], [142, 385],
                     [135, 390], [118, 390],
                     [105, 385], [100, 376], [103, 365], [103, 359], [94, 359], [73, 360], [61, 362], [57, 365], [56, 367],
                     [56, 371],
                     [69, 374], [79, 374], [82, 378], [76, 385], [69, 388], [52, 384], [37, 374], [41, 365], [43, 361],
                     [45, 359],
                     [32, 359], [17, 352], [11, 352], [15, 318], [14, 295], [7, 284], [14, 276], [14, 261], [7, 244],
                     [0, 237],
                     [8, 234], [11, 231], [9, 211], [5, 155], [9, 118], [22, 83], [49, 49], [81, 23], [109, 6], [133, 1],
                     [156, 0], ]
            },
        ]
                   }
    doodlePoly2['data'] += doodlePoly1['data'][1:8]

    doodleSprites = [sprite2D(doodlePoly1, (50, None), PURPLE, True)]
    doodleSprites += [pygame.transform.flip(doodleSprites[0], True, False)]
    doodleSprites += [sprite2D(doodlePoly2, (50, None), PURPLE, True)]
    doodleSprites += [pygame.transform.flip(doodleSprites[2], True, False)]

    doodleSpriteID = 2
    doodleWidth = doodleSprites[0].get_rect().width
    doodleWidthHalf = doodleWidth / 2

    PLATFORM_WIDTH = 70
    PLATFORM_WIDTH_X2 = PLATFORM_WIDTH * 10
    PLATFORM_HEIGHT = 20
    PLATFORM_SIZE = [PLATFORM_WIDTH, PLATFORM_HEIGHT]
    PLATFORMS_AT_START = 10
    PLATFORM_MAX_SPACING = 100
    PLATFORM_MIN_SPACING = 20

    platforms = []
    for index in range(PLATFORMS_AT_START):
        x = random.randint(0, W - PLATFORM_WIDTH)
        y = random.randint(0, H - PLATFORM_HEIGHT)
        hitPlatform = False
        for p in platforms:
            if x <= p[0] - PLATFORM_WIDTH - PLATFORM_MIN_SPACING or x >= p[
                0] + PLATFORM_WIDTH_X2 + PLATFORM_MIN_SPACING or y >= p[1] + PLATFORM_HEIGHT + PLATFORM_MIN_SPACING or y <= \
                    p[1] - PLATFORM_HEIGHT - PLATFORM_MIN_SPACING:
                continue
            hitPlatform = True
            break
        if not hitPlatform:
            platforms.append([x, y])

    GRAVITY = 0.5 # 0 - летит 100 - стоит
    INCREMENT_VELOCITY_X = 0.5 # 0 - не перемещается 100 - крутит но жто только прирост(
    MAX_VELOCITY_X = 4 # скорость
    MAX_VELOCITY_Y = 20 # макс скорость по y
    VELOCITY_X_SLOW_DOWN = 1.05 # инерция по x

    dx = float(HW)
    dy = float(H - doodleSprites[2].get_rect().height)
    dyv = -MAX_VELOCITY_Y
    dxv = 0

    screenshot = False

    # main loop
    while not quit():
        DS.blit(doodleSprites[doodleSpriteID], (dx - doodleWidthHalf, dy - doodleSprites[doodleSpriteID].get_rect().height))
        pygame.draw.circle(DS, RED, (int(dx), int(dy)), 3, 0)

        for p in platforms:
            pygame.draw.rect(DS, BLACK, p + PLATFORM_SIZE, 0)

        pygame.display.update()

        if screenshot:
            pygame.image.save(DS, "screenshot.png")
            pygame.quit()
            sys.exit()

        DS.fill(WHITE)
        CLOCK.tick(FPS)

        if dy <= H / 3 * 2 and dyv < 0:
            for p in platforms:
                p[1] -= dyv
                if p[1] > H:
                    p[1] = -PLATFORM_HEIGHT
        else:
            dy += dyv
        dyv += GRAVITY
        if dyv >= 0:
            for p in platforms:
                if dx >= p[0] and dx <= p[0] + PLATFORM_WIDTH:
                    if dy < p[1] and dy + dyv >= p[1]:
                        dy = p[1]
                        dyv = -MAX_VELOCITY_Y

        if dy > H - doodleSprites[doodleSpriteID].get_rect().height:
            dy = H - doodleSprites[doodleSpriteID].get_rect().height
            dyv = -MAX_VELOCITY_Y

    # нужно добавить паузу на пробел
        k = pygame.key.get_pressed()
        if k[K_LEFT]:
            dxv -= INCREMENT_VELOCITY_X
            if dxv < -MAX_VELOCITY_X: dxv = -MAX_VELOCITY_X
        if k[K_RIGHT]:
            dxv += INCREMENT_VELOCITY_X
            if dxv > MAX_VELOCITY_X: dxv = MAX_VELOCITY_X
        if not k[K_LEFT] and not k[K_RIGHT]: dxv /= VELOCITY_X_SLOW_DOWN
        if k[K_RETURN]: screenshot = True

        dx += dxv
        if dx < -doodleWidthHalf: dx = W + doodleWidthHalf
        if dx > W + doodleWidthHalf: dx = -doodleWidthHalf

        if dyv > 0:
            doodleSpriteID = 0
            if dxv < 0:
                doodleSpriteID = 1
        else:
            doodleSpriteID = 2
            if dxv < 0:
                doodleSpriteID = 3

    pygame.quit()
    sys.exit()
