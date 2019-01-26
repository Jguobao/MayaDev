# -*- coding: utf-8 -*- 
# 选择暂存器
# designed by Jiaguobao
#QQ:779188083 && Tel:15615026078
#Email：779188083@qq.com && jgb2010start@163.com
#Date:2018年10月21日
#version 1.0

#1.筛选物体
#2.存储物体



import maya.cmds as cmds
from maya.OpenMaya import MGlobal
#选择工具
class JGBSelectTool(object):
	def __init__(self):
		self.topBtn = [u'Mesh',u'Surfaces',u'灯光',u'摄像机',u'Curves']
		self.color = [(0.3, 0.39, 0.32),(0.388, 0.29, 0.29),(0.29,0.3,0.388),(0.898,0.412,0.161)]
		#暂存器字典
		self.selStor = {}
		#生成窗口
		if cmds.window('JGBSelectTool',q=1,ex=1):
			cmds.deleteUI('JGBSelectTool')
		
		cmds.window('JGBSelectTool',t=u'选择暂存器 v1.0')
		cmds.scrollLayout( 'scrollLayout' )
		#cmds.gridLayout('topGrid',cwh=[90,30],nrc=[2,3])
		cmds.frameLayout(l='筛选选择',ann=u'筛选出选中物体的某类物体', borderStyle='in')
		cmds.rowColumnLayout('topLayout', nc=3,co=[1,'left',5],ro=[1,'top',5],rat=[2,'top',4],cs=([1,0],[2,10],[3,5]),cw=([1,85],[2,85],[3,85]))
		for s in self.topBtn:
			cmds.button(s,l=s,ann=u"选择%s"%s,w=85 ,c=Callback(self.filterSel,s))
		cmds.setParent('..')
		cmds.setParent('..')
		cmds.frameLayout( 'xuanzeFrame',l='选择暂存',ann=u'存储选择器', borderStyle='in',w=275)
		
		#cmds.setParent('xuanzeFrame')
		#cmds.columnLayout()
		self.geshu = range(6)
		for i in self.geshu:
			cmds.rowLayout('xuanzeLayout%d'%i,nc=4,cw4=[50,115,50,50],h=30)
			cmds.button('sel%d'%i,l='选择%d'%(i+1),w=50,h=22,bgc=self.color[0],ann='选择存储的物体%d'%(i+1),c=Callback(self.getSel, i) )
			cmds.textField('selectName%d'%i,tx='',ann=u'你起得啥名字在这儿！',enable=0,w=115)
			cmds.button(l='拾取',w=50,h=22,ann=u'拾取当前选择的所有物体，起个名字！',c=Callback(self.setSel,i) )
			cmds.button('clearBtn%d'%i,l='清除',w=50,h=22,ann=u'清除当前存储',c=Callback(self.clearSel, i))
			cmds.setParent('..')
		cmds.button(l='清除所有',ann=u'清除所有存储',c=lambda *args:self.claerAll())
		cmds.setParent('..')
		cmds.frameLayout( 'shuoming',l='发明家(*^▽^*)',ann=u'欢迎分享交流学习，意见反馈\n加qq联系我(￣▽￣)~*', borderStyle='in',w=275)
		#cmds.columnLayout( cal='right',cat=['right',1])
		cmds.rowColumnLayout( nc=1,cs=([1,00]))
		cmds.text( l='designed by Jguobao',al='right')

		cmds.text( l='779188083@qq.com',hl=1,al='right')
		cmds.showWindow('JGBSelectTool')
		cmds.window('JGBSelectTool',e=1,wh=[300,420])
#存储选择
	def setSel(self,index):
		print('正在存储选择...')

		sl=cmds.ls(sl=1)
		if sl != []:
			self.selStor[index]=cmds.ls(sl=1)
		else:
			MGlobal.displayInfo('请选择物体')
			return
		#起名字
		result = cmds.promptDialog(title='Rename Object',message='Enter Name:',button=['OK', 'Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')
		if result == 'OK':
			name = cmds.promptDialog(query=True, text=True)
			if name =='':
				name=self.selStor[index][0]
		else:
			name=self.selStor[index][0]
		cmds.textField('selectName%d'%index,e=1,tx=name )
	#获取选择	
	def getSel(self,index):
		print index
		cmds.select(self.selStor[index])
#清除存储
	def clearSel(self,index):
		cmds.textField('selectName%d'%index,e=1,tx='' )
		self.selStor[index]=[]
		MGlobal.displayInfo('清除选择%d'%(index+1))
#清除所有存储
	def claerAll(self):
		for i in self.geshu:
			self.clearSel(i)
	#筛选
	def filterSel(self,t):#[u'Mesh',u'Surfaces',u'灯光',u'摄像机',u'线',u'渲染层']
		try:
			if u'Mesh'==t:
				cmds.select(cmds.ls(sl=1,dag=1,type='mesh'))
			if u'Curves'==t:
				cmds.select(cmds.ls(sl=1,dag=1,type='nurbsCurve'))
			if u'摄像机'==t:
				cmds.select(cmds.ls( sl=1,dag=1,ca=1))
			if u'Surfaces'==t:
				cmds.select(cmds.ls( sl=1,dag=1,type='nurbsSurface'))	
			if u'灯光'==t:	
				cmds.select(cmds.ls(sl=1,dag=1,lt=1))
		except:
			cmds.select(cl=1)
			pass
class Callback(object): 
	def __init__(self, func, *args): 
		self.func = func 
	        self.args = args 
	def __call__(self, *args): 
		return self.func(*self.args )


test = JGBSelectTool()






