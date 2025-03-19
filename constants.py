from pygame import Color


SCREEN_WIDTH:int = 900
SCREEN_HEIGHT:int = 600
BACKGROUND_COLOR:Color = (0,0,0)
FRAMERATE:int = 60


# SPACE PROPERTIES
COULOMBS_CONSTANT:float = 10000000
SPACE_DRAG:float = 0.001
MAX_DISTANCE_FOR_FORCE:int = 1000

PROTON_MASS:float = 20
ELECTRON_MASS:float = 2
NEUTRON_MASS:float = 30
EXTRA_MASS:float = 1

PROTON_CHARGE:float = 2
ELECTRON_CHARGE:float = -2
NEUTRON_CHARGE:float = 0
EXTRA_CHARGE:float = -0.2

PROTON_RADIUS:float = 5
ELECTRON_RADIUS:float = 2.5
NEUTRON_RADIUS:float = 6
EXTRA_RADIUS:float = 4



## 0 electron , 1 proton, 2 neutron, 3 extra 
PARTICLE_COLORS = [(255,255,0), (255,0,0), (255,255,255), (0,255,0)]
