"""
An example of using pin joints.  A screencast showing the development
of this example can be found at:
"""

from pyphysicssandbox import *

window("Pin Joints", 300, 300)

arm1 = box((100, 50), 100, 10, 100)
arm1.color = Color("yellow")

arm2 = box((100, 135), 10, 100)
arm2.color = Color("green")

pivot1 = pivot((105, 55))
pivot1.connect(arm1)

pivot2 = pivot((105, 185))
pivot2.connect(arm2)

motor(arm1, -3)
motor(arm2, 3)

run()



