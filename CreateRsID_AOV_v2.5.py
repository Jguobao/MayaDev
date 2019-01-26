# -*- coding: utf-8 -*- 
# RsID ���ɲ��
# designed by Jiaguobao
#QQ:779188083 && Tel:15615026078
#Date:2018��10��13��
#version 1.0

#1.rs ID ����
#2.aov ����
#3.aov �� ID����
#

import maya.cmds as cmds
import re
import maya.mel as mel
class RsAovGenerate(object):
	def __init__(self):
		self.idArr = None
		self.aovArr = None
		if cmds.window( 'myRsAovWindow',q=1,exists=1):
			cmds.deleteUI('myRsAovWindow')
		self.myWin =  cmds.window('myRsAovWindow',t = 'Redshift ID_AOV ���ɹ��� v2.5')
		self.myColLayout = cmds.columnLayout(cat=['both',12],rowSpacing =8,columnWidth = 400,adjustableColumn=1)
		#self.myRowLayout = cmds.rowLayout( nc=3,columnWidth2 = [150,100],h=50)
		#self.myTxt1 = cmds.text( '��ʼID',w=100)
		self.myIntSlider = cmds.intSliderGrp(l='��ʼID :',v=1001,f=1,minValue = 0,maxValue = 99999,h=50,cw3=[80,80,200])
		cmds.rowLayout(nc=2,adj=True)
		self.myTextField = cmds.textFieldGrp( label='AOV ���� :',cw2=[80,200])
		self.myRadioBtn = cmds.radioButtonGrp( l= '��������',nrb=2,la2=['ģ��','����'],sl=2,cal = [1,'left'],w=300,cw2=[50,50])
		cmds.setParent('..')
		self.myRowLayout = cmds.rowLayout( nc=3,columnWidth3 = [145,145,145],h=50,cl3=["left", "right", "center"])
		self.myBtn1 = cmds.button( l='���',w=100,c = lambda *args:self.check1())
		self.myBtn2 = cmds.button(l='����ID',w=100,c=lambda *args:self.run(cmds.intSliderGrp(self.myIntSlider,q=1,v=1),cmds.textFieldGrp(self.myTextField,q=1,tx=1) ) )
		self.myBtn3 = cmds.button(l='��������',w=100,c=lambda *args:self.run(cmds.intSliderGrp(self.myIntSlider,q=1,v=1),cmds.textFieldGrp(self.myTextField,q=1,tx=1),remove = True ) )
		cmds.setParent('..')
		self.myRowLayout2 = cmds.rowLayout( nc=3,columnWidth3 = [145,145,145],h=50,cl3=["left", "right", "center"])
		self.myBtn4 = cmds.button( l='����ID����',w=100,c =lambda *args:self.proxyOveride() )
		self.myBtn5 = cmds.button( l='ˢ����Ⱦ���',w=100,c = "mel.eval('redshiftCreateAovTab')" )
		cmds.setParent('..')
		self.textBB =cmds.text('1.ѡ����Ҫ����ID������;\n2.����AOV;\n3.������鿴��Ҫ��������AOV;\n4.ִ�д���;\n5.*����ѡ���������������ID��ѡ������Խ�ഴ��Խ�࣬���Ծ���ѡ��;',al='left',bgc=[0.2,0.2,0.4])
		self.jgb = cmds.text( 'Designed by Jguobao')

		cmds.showWindow(self.myWin)
		cmds.window(self.myWin,e=1,w=500,h=300,sizeable=True)
	#����Ƿ����ظ�ID
	#������Ҫ��������ID
	#������Ҫ��������AOV
	
	def check1(self):
		start = self.getIDStart()
		if cmds.radioButtonGrp(self.myRadioBtn,q=1,sl=1) ==1:
			sel = cmds.ls(sl=1)
			num = len(sel)
			color = ([0.267,0.267,0.267],[0.3,0.3,0.8],[0.8,0.6,0.1],[0.9,0.1,0.1])
			msg='ѡ����%d�����壬������%d��ID��%d��AOV;\nID��Χ:%d----%d'%(num,num,(num-1)/3+1,start,start+num)
			if num <10:
				cmds.confirmDialog( m=msg,button = 'ȷ��',bgc=color[0])
			elif num < 20:
				cmds.confirmDialog( m=msg,button = 'ȷ��',bgc=color[1])
			elif num < 40:
				cmds.confirmDialog( m=msg,button = 'ȷ��',bgc=color[2])
			else:
				cmds.confirmDialog( m=msg,button = 'ȷ��',bgc=color[3])
		else:
			num = len(self.getMatSGArr())
			msg = 'ѡ����%d�����ʣ�������%d��ID��%d��AOV;\nID��Χ:%d----%d'%(num,num,(num-1)/3+1,start,start+num)
			cmds.confirmDialog( m=msg,button = 'ȷ��')
		

	def proxyOveride(self):
		for i in cmds.ls(type='RedshiftProxyMesh'):
			if cmds.getAttr(i+'.objectIdMode',l=1):
				cmds.setAttr(i+'.objectIdMode',l=0)
			cmds.setAttr(i+'.objectIdMode',1)

	def getTex(self):
		return cmds.textFieldGrp(self.myTextField,q=1,tx=1)
	def getIDStart(self):
	    return cmds.intSliderGrp(self.myIntSlider,q=1,v=1)	
	def createAov(self,number,aovName='jgb'):
		index = 1
		#AOV �ڵ���
		aovArr= []
		if number==1:
			number=1
		else:
			number = (number-1)/3+1
		for i in range(number):
			tmp = cmds.rsCreateAov(type='Puzzle Matte')
			aovName1 = aovName+str(index)
			cmds.setAttr(tmp+'.name',aovName1,type='string')
			if cmds.radioButtonGrp(self.myRadioBtn,q=1,select=1) == 1:
			    cmds.setAttr(tmp+'.mode',1)
			aovArr.append(tmp)
			index +=1
		#mel.eval('redshiftCreateAovTab')
		mel.eval('redshiftUpdateActiveAovList')
		return aovArr


	def createID(self,startVaule=1001):
	    #������rsID OBJ
		idArr = []
		sel= cmds.ls(sl=1)
		#��Ҫ������ID��Ŀ
		idNum = len(sel)
		#idVaule ��
		idVauleArr = []
		for i in sel:
			cmds.select(i)
			rsObjId = mel.eval('redshiftCreateObjectIdNode()')
			print self.getTex()
			idArr.append(cmds.rename(rsObjId,self.getTex()))
			
		for i in idArr:
			cmds.setAttr(i+'.objectId',startVaule)
			idVauleArr.append(startVaule)
			startVaule +=1
		cmds.select(sel)
		return idNum,idVauleArr,idArr
	#���ô�����AOV ID
	def setAovID(self,idVauleArr,aovArr):
		index = 0
		for i in aovArr:
				cmds.setAttr(i+'.redId',idVauleArr[index])
				index +=1
				if index==len(idVauleArr):
				    return
				cmds.setAttr(i+'.greenId',idVauleArr[index])
				index +=1
				if index==len(idVauleArr):
				    return
				cmds.setAttr(i+'.blueId',idVauleArr[index])
				index +=1
				if index==len(idVauleArr):
				    return
	#����        
	def run(self, startVaule, aovName,remove = False):
		model = cmds.radioButtonGrp(self.myRadioBtn,q=1,sl=1)

		if model ==1:
			if remove == False:
				print 'txt',self.getTex()
				if self.getTex()=='':
					print '123'
					cmds.confirmDialog(m='������AOV���� !!!',button = 'ȷ��')
					return
				#idNum ��Ҫ������ID��Ŀ 
				#idVauleArr  idVaule ��
				#self.idArr #������rsID OBJ
				idNum,idVauleArr,self.idArr = self.createID(startVaule)
				self.aovArr = self.createAov(idNum,self.getTex())
				self.setAovID(idVauleArr,self.aovArr)
			if remove == True:
				if self.idArr !=None:
					if self.aovArr !=None:
						cmds.delete(self.idArr)
						cmds.delete(self.aovArr)
		else:
			if remove == True:
				print 'ɾ��AOV 0'
				if self.aovArr !=None:
					#cmds.delete(self.idArr)
					cmds.delete(self.aovArr)
					print 'ɾ��AOV'
					return
			matID_arr = self.mat_ID(startVaule)
			self.aovArr = self.createAov(len(matID_arr),aovName)
			self.setAovID(matID_arr,self.aovArr)
			
#�ֲ���ID
	def getSG(self):
		#ѡ��SG�ڵ�
		tmp = cmds.ls(sl=1)
		sgs = cmds.ls(sl=1, type='shadingEngine')
		if sgs !=[]:
			return sgs
		#ѡ������
		'''
		mats = cmds.hyperShade(smn=1)
		selMats = cmds.ls(sl=1)
		cmds.select(tmp)
		# ɸѡSG �ų��ظ���Ĭ�Ͻڵ㣬����ѡ��
		sgs = cmds.listConnections(selMats, t='shadingEngine')
		'''
		geo = cmds.ls(sl=1,dag=1,type='mesh')
		sgs = cmds.listConnections(geo,type='shadingEngine')
		return sgs


    # �ֲ���ID
	def getMatSGArr(self):
		# ȥ�ظ�
		selSgSet = self.getSG()
		#  selSgSet[0][0]
		return self.quchong(selSgSet)
    

	def mat_ID(self,startVaule):
		mat_IdNumbs =[]
		selSgSet = self.getMatSGArr()
		if 'initialShadingGroup' in selSgSet:
		    selSgSet.remove('initialShadingGroup')
		if 'initialParticleSE' in selSgSet:
		    selSgSet.remove('initialParticleSE')
		for i in selSgSet:
			
#            if cmds.getAttr(i+'.rsMaterialId') !=0:
			cmds.setAttr(i+'.rsMaterialId',startVaule)
			mat_IdNumbs.append(startVaule)
			startVaule +=1
                
		return mat_IdNumbs #���ز��ʵĴ�����IDֵ������
        
#ȥ��
	def quchong(self,arr):
		newArr = []
		for i in arr:
			if i not in newArr:
				newArr.append(i)
		return newArr
		
bb = RsAovGenerate()
