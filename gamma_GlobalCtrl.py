import maya.cmds as cmds
import maya.mel as mel
class GammaCtrl(object):
	
	def __init__(self):
		self.lit = self.getLits() #��֧��mesh��

		if cmds.window('gammaCtrl',exists=1):
			cmds.deleteUI('gammaCtrl')
		cmds.window('gammaCtrl',t='Gamma ����',w=150)
		cmds.columnLayout(adj=1)
		
		cmds.rowLayout(adj=2,nc=2)
		cmds.text(l='�����б�')
		cmds.textField('channel',tx='color;diffuse')
		
		cmds.setParent('..')
		cmds.rowLayout(adj=2,nc=2)
		cmds.text(l='٤��')
		#cmds.floatSliderGrp( label='٤��', field=True, minValue=0, maxValue=1, fieldMinValue=-10, fieldMaxValue=100.0, value=0.4545 )
		cmds.floatField('gammaVaule',v=0.4545)
		cmds.setParent('..')
		
		cmds.radioButtonGrp('type',nrb=3,l='Ӧ�÷�Χ',l1='����',l2='�ƹ�',l3='����',sl=1,columnWidth3=[60,60,60])
		cmds.radioButtonGrp('range',nrb = 2,l='',l1='ȫ��',l2='ѡ��',sl=1,columnWidth2=[20,20])
		cmds.checkBox('globalCtrl',v=1,l='ȫ�ֿ���')
		cmds.button( l="���� and �޸�",c=lambda *args:self.gammaFunc() )
		cmds.button(l='ȫ��ɾ��',c=lambda *args:self.deleteGamma())
		cmds.button(l='�ر�',c="cmds.deleteUI('gammaCtrl')")
		cmds.showWindow()
		
	   # print("="*30)
	   # print(cmds.textField("channel",q=1,tx=1))

	def globalGammaCtrl(self,gammaVaule):
		gg = cmds.createNode('transform',n='globalGammaCtrl' )
		cmds.addAttr(gg,ln='gamma',at='double',dv=gammaVaule)
		cmds.setAttr(gg+'.gamma',e=1,keyable=1)
	def gammaFunc(self):
		#��ȡ�趨ֵ
		tmp = cmds.textField('channel',q=1, tx=1)
		Att = tmp.split(';')
		gammaVaule = cmds.floatField('gammaVaule',q=1,v=1)
		
		#�������� 1���� 2 �ƹ� 3 ȫ��
		cType = cmds.radioButtonGrp('type',q=1,sl=1)
		#������Χ 1 ȫ�� 2 ѡ��
		cRange = cmds.radioButtonGrp('range',q=1,sl=1)
		#��ȡ�Ƿ񴴽�ȫ�ֿ���
		glob = cmds.checkBox('globalCtrl',q=1,v=1)
		if glob ==True and not cmds.objExists('globalGammaCtrl'):
			self.globalGammaCtrl(gammaVaule=0.454)
		#ȫ��
		if cRange  == 1:
			if cType ==1:
				#���ʲ���
				sl = cmds.ls(mat=1)
				for s in sl:
					for attr in Att:
						if mel.eval("attributeExists %s %s"%(attr,s)) and cmds.getAttr(s+'.'+attr,type=1)=='float3':
							myColor = s+'.'+attr
							channel = cmds.listConnections(myColor,p=1)
							if channel == None:
								#cmds.createNode('gammaCorrect')
								c = cmds.getAttr(myColor)
								print c
								gammaNode = cmds.shadingNode('gammaCorrect',asUtility=1)

								cmds.setAttr(gammaNode+'.value',c[0][0],c[0][1],c[0][2],type='double3')
								cmds.connectAttr(gammaNode+'.outValue',myColor)
								if glob==True:
									cmds.connectAttr('globalGammaCtrl'+'.gamma',gammaNode+'.gammaX')
									cmds.connectAttr('globalGammaCtrl'+'.gamma',gammaNode+'.gammaY')
									cmds.connectAttr('globalGammaCtrl'+'.gamma',gammaNode+'.gammaZ')
							else:
								self.linkColor(channel[0],myColor,glob)
			
			if cType ==2:
				#�ƹ����
				sl = cmds.ls(type = self.lit)
				for s in sl:
					for attr in Att:
						if mel.eval("attributeExists %s %s"%(attr,s)) and cmds.getAttr(s+'.'+attr,type=1)=='float3':
							myColor = s+'.'+attr
							channel = cmds.listConnections(myColor,p=1)
							if channel == None:
								#cmds.createNode('gammaCorrect')
								c = cmds.getAttr(myColor)
								print c
								gammaNode = cmds.shadingNode('gammaCorrect',asUtility=1)

								cmds.setAttr(gammaNode+'.value',c[0][0],c[0][1],c[0][2],type='double3')
								cmds.connectAttr(gammaNode+'.outValue',myColor)
								if glob==True:
									cmds.connectAttr('globalGammaCtrl'+'.gamma',gammaNode+'.gammaX')
									cmds.connectAttr('globalGammaCtrl'+'.gamma',gammaNode+'.gammaY')
									cmds.connectAttr('globalGammaCtrl'+'.gamma',gammaNode+'.gammaZ')
							else:
								self.linkColor(channel[0],myColor,glob)
			if cType ==3:
				sl = cmds.ls(type = self.lit,mat=1)
				for s in sl:
					for attr in Att:
						if mel.eval("attributeExists %s %s"%(attr,s)) and cmds.getAttr(s+'.'+attr,type=1)=='float3':
							myColor = s+'.'+attr
							channel = cmds.listConnections(myColor,p=1)
							if channel == None:
								#cmds.createNode('gammaCorrect')
								c = cmds.getAttr(myColor)
								print c
								gammaNode = cmds.shadingNode('gammaCorrect',asUtility=1)

								cmds.setAttr(gammaNode+'.value',c[0][0],c[0][1],c[0][2],type='double3')
								cmds.connectAttr(gammaNode+'.outValue',myColor)
								if glob==True:
									cmds.connectAttr('globalGammaCtrl'+'.gamma',gammaNode+'.gammaX')
									cmds.connectAttr('globalGammaCtrl'+'.gamma',gammaNode+'.gammaY')
									cmds.connectAttr('globalGammaCtrl'+'.gamma',gammaNode+'.gammaZ')
							else:
								self.linkColor(channel[0],myColor,glob)

	def getLits(self):
		lightdict = {
	'redshift4maya':['VRayLightSphereShape','VRayLightDomeShape','VRayLightRectShape','VRayLightIESShape'],
	
	'Mayatomr':['mia_photometric_light','mia_physicalsun','mia_portal_light','mib_blackbody','mib_cie_d','physical_light','user_ibl_env','user_ibl_rect'],
	
	'vrayformaya':['RedshiftPhysicalLight','RedshiftIESLight','RedshiftPortalLight','RedshiftDomeLight'],
	
	'mtoa':['aiSkyDomeLight','aiAreaLight','aiPhotometricLight']
	}
		currentPlugin = cmds.pluginInfo( query=True, listPlugins=True )
		xuanranqi = ['mtoa','redshift4maya','vrayformaya','Mayatomr']
		lits = []
		for i in xuanranqi:
			if i in currentPlugin:
				#print lightdict[i]
				for o in lightdict[i]:
					lits.append(o)
		return lits
	
	def deleteGamma(self):
		if cmds.objExists('globalGammaCtrl'):
			cmds.delete('globalGammaCtrl')
		gammaNodes = cmds.ls(type='gammaCorrect')
		for g in gammaNodes:
			inlink = cmds.listConnections(g+'.value',p=1)
			outlink = cmds.listConnections(g+'.outValue',p=1)
			c = cmds.getAttr(g+'.value')
			cmds.delete(g)
			print "=========="
			print inlink,outlink
			if outlink !=None:
				if inlink != None:
					cmds.connectAttr(inlink[0],outlink[0])
				else:
					cmds.setAttr(outlink[0],c[0][0],c[0][1],c[0][2],type='double3')


	def linkColor(self,channel,c,glob):
		if cmds.nodeType(channel) != 'gammaCorrect':
			gammaNode = cmds.shadingNode('gammaCorrect',asUtility=1)
			cmds.connectAttr(channel,gammaNode+'.value',f=1)
			cmds.connectAttr(gammaNode+'.value',c,f=1)
			if glob==True:
				cmds.connectAttr('globalGammaCtrl'+'.gamma',gammaNode+'.gammaX')
				cmds.connectAttr('globalGammaCtrl'+'.gamma',gammaNode+'.gammaY')
				cmds.connectAttr('globalGammaCtrl'+'.gamma',gammaNode+'.gammaZ')

GammaCtrl()











cmds.setAttr('gammaCorrect3.value',0.5,0.5,0.5 ,type='double3')

cmds.ls(type=lit)
a = cmds.ls( sl=1,st=1)

'RedshiftPhysicalLight','RedshiftIESLight','RedshiftPortalLight','RedshiftDomeLight'

'VRayLightSphereShape','VRayLightDomeShape','VRayLightRectShape','VRayLightIESShape'

lit = ['light','aiSkyDomeLight','aiAreaLight','aiPhotometricLight','RedshiftPhysicalLight','RedshiftIESLight','RedshiftPortalLight','RedshiftDomeLight','VRayLightSphereShape','VRayLightDomeShape','VRayLightRectShape','VRayLightIESShape'] #��֧��mesh��

a='color;diffuse'
a.split(';')
def gammaFunc():
	#��ȡ�趨ֵ
	tmp = cmds.textField('channel',q=1, tx=1)
	Att = tmp.split(';')
	gammaVaule = cmds.floatField('gammaVaule',q=1,v=1)
	
	#�������� 1���� 2 �ƹ� 3 ȫ��
	cType = cmds.radioButtonGrp('type',q=1,sl=1)
	#������Χ 1 ȫ�� 2 ѡ��
	cRange = cmds.radioButtonGrp('range',q=1,sl=1)
	#��ȡ�Ƿ񴴽�ȫ�ֿ���
	glob = cmds.checkBox('globalCtrl',q=1,v=1)
	if glob ==True and not cmds.objExists('globalGammaCtrl'):
		globalGammaCtrl(gammaVaule=0.454)
	#ȫ��
	if cRange  == 1:
		if cType ==1:
			#���ʲ���
			sl = cmds.ls(mat=1)
			for s in sl:
				for attr in Att:
					if mel.eval("attributeExists %s %s"%(attr,s)) and cmds.getAttr(s+'.'+attr,type=1)=='float3':
						myColor = s+'.'+attr
						channel = cmds.listConnections(myColor,p=1)
						if channel = None:
							#cmds.createNode('gammaCorrect')
							c = cmds.getAttr(myColor)
							gammaNode = cmds.shadingNode('gammaCorrect',asUtility=1)
							cmds.setAttr(gammaNode,c)
							cmds.connectAttr(gammaNode+'.outValue',myColor)
							if glob==True:
								cmds.connectAttr('globalGammaCtrl'+'.gamma',gammaNode+'.gammaX')
								cmds.connectAttr('globalGammaCtrl'+'.gamma',gammaNode+'.gammaY')
								cmds.connectAttr('globalGammaCtrl'+'.gamma',gammaNode+'.gammaZ')

		if cType ==2:
			#�ƹ����
			sl = cmds.ls(type = lit)
		if cType ==3:
			sl = cmds.ls(type = lit,mat=1)
			
def globalGammaCtrl(gammaVaule):
	gg = cmds.createNode('transform',n='globalGammaCtrl' )
	cmds.addAttr(gg,ln='gamma',at='double',dv=gammaVaule)
	cmds.setAttr(gg+'.gamma',e=1,keyable=1)

globalGammaCtrl(100)

for i in sl:
	for attr in textBuffer:
		if mel.attributeExists 
#�ж������Ƿ���� �����Ǹ�����ֵ
mel.eval("attributeExists color rsPhysicalLightShape1") and cmds.getAttr('rsPhysicalLightShape1'+'.color',type=1)=='float3'

jieruzhi = cmds.listConnections('rsPhysicalLightShape1'+'.color',p=1)

if jieruzhi ==None:
	cmds.createNode('gammaCorrect')
	cmds.shadingNode('gammaCorrect',asUtility=1)
	cmds.setAttr()



window = cmds.window(title='floatSliderGrp Example')
cmds.columnLayout()
cmds.floatSliderGrp( label='Group 1', field=True )
cmds.floatSliderGrp( label='Group 2', field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0, fieldMaxValue=100.0, value=0 )
cmds.showWindow( window )




