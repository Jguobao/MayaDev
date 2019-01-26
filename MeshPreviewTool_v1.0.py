# -*- coding: utf-8 -*-
# Mesh 预览控制
# designed by Jiaguobao
# QQ:779188083 && Tel:15615026078
# Email：779188083@qq.com && jgb2010start@163.com
# Date:2018年10月28日
# version 1.0

# 1.设置物体的预览精度
# 2.设置物体的渲染精度
# 3.解决物体按3不无效果的问题 Render Ctrl
# 4.关闭关联预览 可以为物体分开设置 低级别显示 高级别渲染
#
# 导入模块 定义窗口
import pymel.core as pm
def ContrlUI():
	if pm.window( u'MeshPreviewUI',q=1,exists=1):
		pm.deleteUI(u'MeshPreviewUI')
	pm.window(u'MeshPreviewUI',t=u'Mesh预览--渲染细分Tool v1.0')
	pm.columnLayout(cal='left')
	pm.rowLayout(nc=2)
	pm.intSliderGrp( 'intDis',field=True, label='Display Ctrl',ann=u'物体的显示精度控制',cw=[(1,80),(2,50),(3,100)],cal=[(1,'left'),(2,'left'),(3,'left')], minValue=0, maxValue=7, fieldMinValue=0, fieldMaxValue=7, value=2 )
	pm.setParent('..')
	pm.rowLayout(nc=2)
	pm.intSliderGrp( 'intRen',field=True, label='Render Ctrl',ann=u'物体的渲染精度控制',cw=[(1,80),(2,50),(3,100)],cal=[(1,'left'),(2,'left'),(3,'left')], minValue=0, maxValue=7, fieldMinValue=0, fieldMaxValue=7, value=2,en=0 )
	pm.checkBox('checkMod', l=u'关联预览',ann=u'渲染精度与显示精度关联',v=1,cc=lambda *args:changelink())
	pm.setParent('..')
	pm.rowLayout( nc=3,cw=[(1,75),(2,75),(3,75)])
	pm.button(l=u'按1',w=74,bgc=[0.4,0.2,0.2],ann=u'就是按1啦！！！',c=lambda *args:run(0,0))
	pm.button(l=u'按2',w=74,bgc=[0.2,0.2,0.4],ann=u'就是按2啦！！！',c=lambda *args:run(0,1))
	pm.button(l=u'按3',w=74,bgc=[0.2,0.4,0.2],ann=u'就是按3啦！！！',c=lambda *args:run(0,2))
	pm.setParent('..')
	pm.rowLayout( nc=3,cw=[(1,75),(2,75),(3,75)])
	pm.button(l=u'所有按1',w=74,bgc=[0.4,0.2,0.2],ann=u'就是所有按1啦！！！',c=lambda *args:run(1,0))
	pm.button(l=u'所有按2',w=74,bgc=[0.2,0.2,0.4],ann=u'就是所有按2啦！！！',c=lambda *args:run(1,1))
	pm.button(l=u'所有按3',w=74,bgc=[0.2,0.4,0.2],ann=u'就是所有按3啦！！！',c=lambda *args:run(1,2))
	pm.setParent('..')
	pm.text('designed by jiaguobao',ann=u'作者就是我')
	pm.showWindow(u'MeshPreviewUI')
	pm.window( u'MeshPreviewUI',e=1,w=320,h=120,sizeable=False)

# 获取关联属性	
def changelink():
	if pm.checkBox('checkMod',q=1,v=1) ==0:
		pm.intSliderGrp( 'intRen',e=1,en=1)
	else:
		pm.intSliderGrp( 'intRen',e=1,en=0)
#获取mesh
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
#主函数
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