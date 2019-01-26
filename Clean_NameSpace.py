# -*- coding: utf-8 -*-
# 一键清除名称空间
# designed by Jiaguobao
# QQ:779188083 && Tel:15615026078
# Date:2018年10月15日
# 

import maya.cmds as cmds
def Clean_NameSpace():
	object=cmds.ls()
	for i in object:
		newname = i.split(":")[-1]
		try:
			cmds.rename(i,newname)
		except:
			pass
Clean_NameSpace()