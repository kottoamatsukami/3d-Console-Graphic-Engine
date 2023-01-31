from core import UTWorld, UTFuncs, UTViewport, UTGeneral

viewport = UTViewport.ViewPort(
    width=60,
    height=60,
)
#### Create worlds
world_test_1 = UTWorld.World(
    name="test_world_1",
)

world_test_2 = UTWorld.World(
    name="test_world_2",
)
###################

linker = UTWorld.Linker(
    viewport=viewport,
)

##### Link worlds
linker.link_world(
    world=world_test_1
)

linker.link_world(
    world=world_test_2
)

linker.load_world(0)

