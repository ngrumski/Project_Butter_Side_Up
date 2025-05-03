import mujoco
import mujoco.viewer as viewer

worldSpec = mujoco.MjSpec.from_file("world.xml")

robot = worldSpec.worldbody.add_body(
    pos=[0, 0 , 3],
    euler=[0, 0 , 0],
)

robot.mass = 1 

joint = robot.add_freejoint()

geom = robot.add_geom(
    name='my_geom',
    type=mujoco.mjtGeom.mjGEOM_SPHERE,
    size=[0.1, 0, 0],
    rgba=[1, 0, 0, 1]
)



model = worldSpec.compile()

viewer.launch(model)