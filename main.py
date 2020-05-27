from pygame import *
from main_arcade_hero import *
from platforms_def import *
from platform_spawn import *
from run_set import *

win = display.set_mode((1000, 1000))
display.set_caption('runner')

main_hero = main_hero_sprite('main_hero.png',150,500)
wall1 = wall('platform.png', 0,20,1000,50)
wall2 = wall('platform.png', 0, 930,1000,50)
run = True

create1 = obstacles()
create2 = obstacles()
create3 = obstacles()
create4 = obstacles()

def lose(win):
    stop = True
    win.blit(transform.scale(image.load('lose.png'), (1000, 1000)), (0, 0))
    display.update()
    while stop:
        for events in event.get():
            if events.type == QUIT:
                stop = False
                runobject.run = False
            if events.type == KEYDOWN:
                if events.key == K_r:
                    stop = False
                    create1.place = -199
                    create2.place = -199
                    create3.place = -199
                    create4.place = -199
                if events.key == K_t:
                    stop = False
                    runobject.run = False

while runobject.run:

    time.delay(runobject.delay)

    for events in event.get():
        if events.type == KEYDOWN:
            if events.key == K_t:
                runobject.run = False
            if events.key == K_SPACE:
                main_hero.gravity = not(main_hero.gravity)
        if events.type == QUIT:
            runobject.run = False

    runobject.shift+=runobject.speed
    runobject.local_shift = runobject.shift % 1000

    if runobject.local_shift !=0 :
        win.blit(image.load('black_background.jpg'), (runobject.local_shift - 1000, 0))
        win.blit(image.load('black_background.jpg'), (runobject.local_shift, 0))

    wall1.place(win)
    wall2.place(win)

    barrier.place_config()

    if runobject.obs1:
        if not(runobject.obs1_created):
            runobject.obs1_created = True
            #create1 = obstacles()
            create1.place_choose()
            create1.spawn_obstacle1(win)
        elif create1.place< -200:
            create1.place = 1100
            runobject.obs1 = False
        else:
            create1.place_choose()
            create1.spawn_obstacle1(win)

    if runobject.obs2:
        if not(runobject.obs2_created):
            runobject.obs2_created = True
            #create2 = obstacles()
            create2.place_choose()
            create2.spawn_obstacle2(win)
        elif create2.place< -200:
            create2.place = 1100
            runobject.obs2 = False
        else:
            create2.place_choose()
            create2.spawn_obstacle2(win)

    if runobject.obs3:
        if not(runobject.obs3_created):
            runobject.obs3_created = True
            #create3 = obstacles()
            create3.place_choose()
            create3.spawn_obstacle3(win)
        elif create3.place< -200:
            create3.place = 1100
            runobject.obs3 = False
        else:
            create3.place_choose()
            create3.spawn_obstacle3(win)

    if runobject.obs4:
        if not(runobject.obs4_created):
            runobject.obs4_created = True
            #create4 = obstacles()
            create4.place_choose()
            create4.spawn_obstacle4(win)
        elif create4.place< -200:
            create4.place = 1100
            runobject.obs4 = False
        else:
            create4.place_choose()
            create4.spawn_obstacle4(win)

    main_hero.update(main_hero,wall1,wall2)
    main_hero.reset(win)

    death = sprite.collide_rect(main_hero, create1.trap_pl1) or sprite.collide_rect(main_hero,
        create1.trap_pl11) or sprite.collide_rect(
        main_hero, create1.trap_pl12) or sprite.collide_rect(main_hero, create2.trap_pl2) or sprite.collide_rect(
        main_hero, create2.trap_pl3) or sprite.collide_rect(main_hero, create3.trap_pl11) or sprite.collide_rect(
        main_hero, create3.trap_pl4) or sprite.collide_rect(main_hero, create4.trap_pl5) or sprite.collide_rect(
        main_hero, create4.trap_pl12)

    if sprite.collide_rect(main_hero, create1.wall_up) or sprite.collide_rect(main_hero, create3.wall_up):
        main_hero.rect.y = create1.wall_up.rect.bottom
        main_hero.gravity_speed = 0

    if sprite.collide_rect(main_hero, create1.wall_down) or sprite.collide_rect(main_hero, create4.wall_down):
        main_hero.rect.y = create1.wall_down.rect.y-100
        main_hero.gravity_speed = 0

    display.update()

    if death:
        lose(win)

    display.update()
