# -*- coding: utf-8 -*-
# Mesh Ԥ������
# designed by Jiaguobao
# QQ:779188083 && Tel:15615026078
# Email��779188083@qq.com && jgb2010start@163.com
# Date:2018��10��28��
# version 1.0

# 1.���������Ԥ������
# 2.�����������Ⱦ����
# 3.������尴3����Ч�������� Render Ctrl
# 4.�رչ���Ԥ�� ����Ϊ����ֿ����� �ͼ�����ʾ �߼�����Ⱦ
#
# ����ģ�� ���崰��
import pymel.core as pm
def ContrlUI():
	if pm.window( u'MeshPreviewUI',q=1,exists=1):
		pm.deleteUI(u'MeshPreviewUI')
	pm.window(u'MeshPreviewUI',t=u'MeshԤ��--��Ⱦϸ��Tool v1.0')
	pm.columnLayout(cal='left')
	pm.rowLayout(nc=2)
	pm.intSliderGrp( 'intDis',field=True, label='Display Ctrl',ann=u'�������ʾ���ȿ���',cw=[(1,80),(2,50),(3,100)],cal=[(1,'left'),(2,'left'),(3,'left')], minValue=0, maxValue=7, fieldMinValue=0, fieldMaxValue=7, value=2 )
	pm.setParent('..')
	pm.rowLayout(nc=2)
	pm.intSliderGrp( 'intRen',field=True, label='Render Ctrl',ann=u'�������Ⱦ���ȿ���',cw=[(1,80),(2,50),(3,100)],cal=[(1,'left'),(2,'left'),(3,'left')], minValue=0, maxValue=7, fieldMinValue=0, fieldMaxValue=7, value=2,en=0 )
	pm.checkBox('checkMod', l=u'����Ԥ��',ann=u'��Ⱦ��������ʾ���ȹ���',v=1,cc=lambda *args:changelink())
	pm.setParent('..')
	pm.rowLayout( nc=3,cw=[(1,75),(2,75),(3,75)])
	pm.button(l=u'��1',w=74,bgc=[0.4,0.2,0.2],ann=u'���ǰ�1��������',c=lambda *args:run(0,0))
	pm.button(l=u'��2',w=74,bgc=[0.2,0.2,0.4],ann=u'���ǰ�2��������',c=lambda *args:run(0,1))
	pm.button(l=u'��3',w=74,bgc=[0.2,0.4,0.2],ann=u'���ǰ�3��������',c=lambda *args:run(0,2))
	pm.setParent('..')
	pm.rowLayout( nc=3,cw=[(1,75),(2,75),(3,75)])
	pm.button(l=u'���а�1',w=74,bgc=[0.4,0.2,0.2],ann=u'�������а�1��������',c=lambda *args:run(1,0))
	pm.button(l=u'���а�2',w=74,bgc=[0.2,0.2,0.4],ann=u'�������а�2��������',c=lambda *args:run(1,1))
	pm.button(l=u'���а�3',w=74,bgc=[0.2,0.4,0.2],ann=u'�������а�3��������',c=lambda *args:run(1,2))
	pm.setParent('..')
	pm.text('designed by jiaguobao',ann=u'���߾�����')
	pm.showWindow(u'MeshPreviewUI')
	pm.window( u'MeshPreviewUI',e=1,w=320,h=120,sizeable=False)

# ��ȡ��������	
def changelink():
	if pm.checkBox('checkMod',q=1,v=1) ==0:
		pm.intSliderGrp( 'intRen',e=1,en=1)
	else:
		pm.intSliderGrp( 'intRen',e=1,en=0)
#��ȡmesh
def getMesh(mode):
	selMesh=[]
	if mode==0:
		selTran = pm.ls(sl=1,dag=1,tr=1)
		for s in selTran:
			selMesh += s.getShapes()
		return 	selMesh
	else:
		selTran = pm.ls(type=u'mesh')
		#for s in selTran:
		#	selMesh += s.getShapes()
		return 	selTran
#������
def run(mode,level):
	check =pm.checkBox('checkMod',q=1,v=1)
	intDis = pm.intSliderGrp('intDis',q=1,v=1)
	if check ==False:
		intRen = pm.intSliderGrp('intRen',q=1,v=1)
	else:
		intRen = intDis
	meshs = getMesh(mode)
	for m in meshs:
		m.displaySmoothMesh.set(level)
		m.smoothLevel.set(intDis)
		if check==False:
			m.useSmoothPreviewForRender.set(0)
			print m,intRen
		m.renderSmoothLevel.set(intRen)
		
if __name__ =='__main__':
	ContrlUI()