from mine import *
import time

mc = Minecraft()

while True:
	pos = mc.player.getPos()
	mc.setBlock(pos.x, pos.y, pos.z, 46, 1)
	time.sleep(1)