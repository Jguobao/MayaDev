# -*- coding: utf-8 -*-
# һ��������ƿռ�
# designed by Jiaguobao
# QQ:779188083 && Tel:15615026078
# Date:2018��10��15��
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