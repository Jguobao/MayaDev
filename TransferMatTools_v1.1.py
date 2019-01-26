# -*- coding: utf-8 -*-
# 同拓扑模型传递工具
# designed by Jiaguobao
# QQ:779188083 && Tel:15615026078
# Date:2018年10月24日
#Email：jgb2010start@163.com && 779188083@qq.com
# version 1.1

# 相同拓扑的模型材质传递
# 1.选择源物体
# 2.选择目标物体
# 3.执行

import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel
from maya.OpenMaya import MGlobal
#获取源物体 shapes
#获取目标物体 shapes
#传递
txt = u'1.选择待传递的源物体；\n\n2.选择待传递的目标物体；\n\n3.执行ok'
def transferMat():
	sel = pm.ls(sl=1)
	if sel ==[] or len(sel) !=2:
		MGlobal.displayInfo('请选择2个物体(源+目标)不要多选或者少选！')
		return
	if pm.objectType(sel[0]) == 'mesh':
		sourceShape = sel[0]
	else:
		sourceShape = sel[0].getShapes()[0]
	if pm.objectType(sel[1]) == 'mesh':
		targetShape = sel[1]
	else:
		targetShape = sel[1].getShapes()[0]
	mel.eval('deformerAfterObjectSetMod %s %s'%(sourceShape.name(),targetShape.name() ))
	MGlobal.displayInfo('完成！请检查结果！！！')

def myUI():
	if cmds.window( 'TransferMat',q=1,exists =1):
		cmds.deleteUI('TransferMat')
	cmds.window('TransferMat',t='1对1 材质传递工具v1.1')
	cmds.rowColumnLayout( 'topLayout', nc=1,co=([1,'both',5]),ro=([1,'both',5]))
	cmds.frameLayout( l='使用说明',borderStyle='in',bv=1)
	#cmds.columnLayout()
	cmds.text( l=txt,w=285,h=60,ww=1,al='left',bgc=[0.2,0.3,0.35],fn='boldLabelFont')
	cmds.button( l='执行',c='transferMat()',h=30,bgc=[0.5,0.4,0.35] )
	cmds.text(l='designed by jiaguobao')
	cmds.showWindow('TransferMat')
	cmds.window( 'TransferMat',e=1,w=300,h=180,s=0)
	
if __name__ == '__main__':
	myUI()


