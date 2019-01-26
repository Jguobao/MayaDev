# -*- coding: utf-8 -*-
# ͬ����ģ�ʹ��ݹ���
# designed by Jiaguobao
# QQ:779188083 && Tel:15615026078
# Date:2018��10��24��
#Email��jgb2010start@163.com && 779188083@qq.com
# version 1.1

# ��ͬ���˵�ģ�Ͳ��ʴ���
# 1.ѡ��Դ����
# 2.ѡ��Ŀ������
# 3.ִ��

import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel
from maya.OpenMaya import MGlobal
#��ȡԴ���� shapes
#��ȡĿ������ shapes
#����
txt = u'1.ѡ������ݵ�Դ���壻\n\n2.ѡ������ݵ�Ŀ�����壻\n\n3.ִ��ok'
def transferMat():
	sel = pm.ls(sl=1)
	if sel ==[] or len(sel) !=2:
		MGlobal.displayInfo('��ѡ��2������(Դ+Ŀ��)��Ҫ��ѡ������ѡ��')
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
	MGlobal.displayInfo('��ɣ�������������')

def myUI():
	if cmds.window( 'TransferMat',q=1,exists =1):
		cmds.deleteUI('TransferMat')
	cmds.window('TransferMat',t='1��1 ���ʴ��ݹ���v1.1')
	cmds.rowColumnLayout( 'topLayout', nc=1,co=([1,'both',5]),ro=([1,'both',5]))
	cmds.frameLayout( l='ʹ��˵��',borderStyle='in',bv=1)
	#cmds.columnLayout()
	cmds.text( l=txt,w=285,h=60,ww=1,al='left',bgc=[0.2,0.3,0.35],fn='boldLabelFont')
	cmds.button( l='ִ��',c='transferMat()',h=30,bgc=[0.5,0.4,0.35] )
	cmds.text(l='designed by jiaguobao')
	cmds.showWindow('TransferMat')
	cmds.window( 'TransferMat',e=1,w=300,h=180,s=0)
	
if __name__ == '__main__':
	myUI()


