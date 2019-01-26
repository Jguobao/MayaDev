# -*- coding: utf-8 -*- 
# ѡ���ݴ���
# designed by Jiaguobao
#QQ:779188083 && Tel:15615026078
#Email��779188083@qq.com && jgb2010start@163.com
#Date:2018��10��21��
#version 1.0

#1.ɸѡ����
#2.�洢����



import maya.cmds as cmds
from maya.OpenMaya import MGlobal
#ѡ�񹤾�
class JGBSelectTool(object):
	def __init__(self):
		self.topBtn = [u'Mesh',u'Surfaces',u'�ƹ�',u'�����',u'Curves']
		self.color = [(0.3, 0.39, 0.32),(0.388, 0.29, 0.29),(0.29,0.3,0.388),(0.898,0.412,0.161)]
		#�ݴ����ֵ�
		self.selStor = {}
		#���ɴ���
		if cmds.window('JGBSelectTool',q=1,ex=1):
			cmds.deleteUI('JGBSelectTool')
		
		cmds.window('JGBSelectTool',t=u'ѡ���ݴ��� v1.0')
		cmds.scrollLayout( 'scrollLayout' )
		#cmds.gridLayout('topGrid',cwh=[90,30],nrc=[2,3])
		cmds.frameLayout(l='ɸѡѡ��',ann=u'ɸѡ��ѡ�������ĳ������', borderStyle='in')
		cmds.rowColumnLayout('topLayout', nc=3,co=[1,'left',5],ro=[1,'top',5],rat=[2,'top',4],cs=([1,0],[2,10],[3,5]),cw=([1,85],[2,85],[3,85]))
		for s in self.topBtn:
			cmds.button(s,l=s,ann=u"ѡ��%s"%s,w=85 ,c=Callback(self.filterSel,s))
		cmds.setParent('..')
		cmds.setParent('..')
		cmds.frameLayout( 'xuanzeFrame',l='ѡ���ݴ�',ann=u'�洢ѡ����', borderStyle='in',w=275)
		
		#cmds.setParent('xuanzeFrame')
		#cmds.columnLayout()
		self.geshu = range(6)
		for i in self.geshu:
			cmds.rowLayout('xuanzeLayout%d'%i,nc=4,cw4=[50,115,50,50],h=30)
			cmds.button('sel%d'%i,l='ѡ��%d'%(i+1),w=50,h=22,bgc=self.color[0],ann='ѡ��洢������%d'%(i+1),c=Callback(self.getSel, i) )
			cmds.textField('selectName%d'%i,tx='',ann=u'�����ɶ�����������',enable=0,w=115)
			cmds.button(l='ʰȡ',w=50,h=22,ann=u'ʰȡ��ǰѡ����������壬������֣�',c=Callback(self.setSel,i) )
			cmds.button('clearBtn%d'%i,l='���',w=50,h=22,ann=u'�����ǰ�洢',c=Callback(self.clearSel, i))
			cmds.setParent('..')
		cmds.button(l='�������',ann=u'������д洢',c=lambda *args:self.claerAll())
		cmds.setParent('..')
		cmds.frameLayout( 'shuoming',l='������(*^��^*)',ann=u'��ӭ������ѧϰ���������\n��qq��ϵ��(������)~*', borderStyle='in',w=275)
		#cmds.columnLayout( cal='right',cat=['right',1])
		cmds.rowColumnLayout( nc=1,cs=([1,00]))
		cmds.text( l='designed by Jguobao',al='right')

		cmds.text( l='779188083@qq.com',hl=1,al='right')
		cmds.showWindow('JGBSelectTool')
		cmds.window('JGBSelectTool',e=1,wh=[300,420])
#�洢ѡ��
	def setSel(self,index):
		print('���ڴ洢ѡ��...')

		sl=cmds.ls(sl=1)
		if sl != []:
			self.selStor[index]=cmds.ls(sl=1)
		else:
			MGlobal.displayInfo('��ѡ������')
			return
		#������
		result = cmds.promptDialog(title='Rename Object',message='Enter Name:',button=['OK', 'Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')
		if result == 'OK':
			name = cmds.promptDialog(query=True, text=True)
			if name =='':
				name=self.selStor[index][0]
		else:
			name=self.selStor[index][0]
		cmds.textField('selectName%d'%index,e=1,tx=name )
	#��ȡѡ��	
	def getSel(self,index):
		print index
		cmds.select(self.selStor[index])
#����洢
	def clearSel(self,index):
		cmds.textField('selectName%d'%index,e=1,tx='' )
		self.selStor[index]=[]
		MGlobal.displayInfo('���ѡ��%d'%(index+1))
#������д洢
	def claerAll(self):
		for i in self.geshu:
			self.clearSel(i)
	#ɸѡ
	def filterSel(self,t):#[u'Mesh',u'Surfaces',u'�ƹ�',u'�����',u'��',u'��Ⱦ��']
		try:
			if u'Mesh'==t:
				cmds.select(cmds.ls(sl=1,dag=1,type='mesh'))
			if u'Curves'==t:
				cmds.select(cmds.ls(sl=1,dag=1,type='nurbsCurve'))
			if u'�����'==t:
				cmds.select(cmds.ls( sl=1,dag=1,ca=1))
			if u'Surfaces'==t:
				cmds.select(cmds.ls( sl=1,dag=1,type='nurbsSurface'))	
			if u'�ƹ�'==t:	
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






