
# -*- coding: utf-8 -*-
# 将所选物体贴在坐标网格上
# designed by Jiaguobao
# QQ:779188083 && Tel:15615026078
# Date:2018年10月14日
# version 1.0

# 
# 1.选择物体
# 2.执行脚本
# 3.将所选物体全部最低点归于坐标y轴零点


from maya.OpenMaya import MGlobal
#所有物体贴地
def doit():
	tr = cmds.ls(sl=1,dag=1,tr=1)
	for i in tr:
		bb = cmds.xform(i,q=1,bb=1)
		cmds.xform(i,r=1,t=[0,-bb[1],0])
MGlobal.displayInfo(u'执行完成')

if __name__ == '__main__':
	doit()

