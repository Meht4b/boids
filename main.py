from classes import *


pygame.init()

window = pygame.display.set_mode((700,700))
clock = pygame.time.Clock()


a = flock(vector(250,500),vector(250,500),1000,100,window)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        

    window.fill((0,0,0))
    #print(bone.bones[0].angle,bone.bones[1].rotation,bone.bones[1].rotation)
    a.update()
    clock.tick(30)

    pygame.display.update()