# -*- coding: utf-8 -*-
# ����ģ��ת�����
# designed by Jiaguobao
# QQ:779188083 && Tel:15615026078
# Date:2018��10��14��
# version 1.0

# ��Rs����������ʾΪָ�ϵļ�ģ��ʹ����ģ���Լ�ģ��ʾ����rs����������Ⱦ
# 1.ʰȡ��ģ
# 2.ʰȡĿ�����
# 3.ִ��

import maya.cmds as cmds

globalObj = None
globalProxy = None


class RsMeshConvert(object):
    def __init__(self):
        self.color = [(0.3, 0.39, 0.32),(0.388, 0.29, 0.29),(0.29,0.3,0.388),(0.898,0.412,0.161)]
        if cmds.window('myWindow', q=1, exists=1):
            cmds.deleteUI('myWindow')
        self.myWin = cmds.window('myWindow', t='Rs Shape ת�� v1.0')
        self.myLayout = cmds.formLayout(numberOfDivisions=100)
    
        self.myTex1 = cmds.text('����ģ��')
        cmds.formLayout(self.myLayout, e=1, attachForm=[(self.myTex1, 'top', 20), (self.myTex1, 'left', 10)])

        self.mytf1 = cmds.textField(tx='ʰȡԴ����', enable=0)
        cmds.formLayout(self.myLayout, e=1,
                        attachForm=[(self.mytf1, 'top', 15), (self.mytf1, 'left', 70), (self.mytf1, 'right', 80)])

        self.myBtn1 = cmds.button(l='ʰȡ', c=lambda *args: self.setText())
        cmds.formLayout(self.myLayout, e=1, attachForm=[(self.myBtn1, 'top', 15), (self.myBtn1, 'right', 10)])

        self.myTex2 = cmds.text('Ŀ��ģ��')
        cmds.formLayout(self.myLayout, e=1, attachForm=[(self.myTex2, 'top', 55), (self.myTex2, 'left', 10)])

        self.mytf2 = cmds.textField(tx='ʰȡĿ������', enable=0)
        cmds.formLayout(self.myLayout, e=1,
                        attachForm=[(self.mytf2, 'top', 50), (self.mytf2, 'left', 70), (self.mytf2, 'right', 80)])

        self.myBtn2 = cmds.button(l='ʰȡ', c=lambda *args: self.setRsTex(self.mytf2))
        cmds.formLayout(self.myLayout, e=1, attachForm=[(self.myBtn2, 'top', 50), (self.myBtn2, 'right', 10)])

        self.myCheck = cmds.checkBox(l='��������', v=1, ann='�رպ��Ѿ������Ĵ�������Ͳ����ظ�������ֻ�����δ����\n���Ĵ������壬������Ḳ�Ǵ�������Ĺ���.')
        cmds.formLayout(self.myLayout, e=1, attachForm=[(self.myCheck, 'top', 80), (self.myCheck, 'left', 10)])

        self.myBtn3 = cmds.button(l='ִ��', c=lambda *args: self.myDoIt(self.mytf1, self.mytf2,
                                                                      cmds.checkBox(self.myCheck, q=1, v=1)))
        cmds.formLayout(self.myLayout, e=1,
                        attachForm=[(self.myBtn3, 'top', 80), (self.myBtn3, 'left', 80), (self.myBtn3, 'right', 80)])

        self.jgb = cmds.text('Designed by Jguobao')
        cmds.formLayout(self.myLayout, e=1,
                        attachForm=[(self.jgb, 'bottom', 20), (self.jgb, 'left', 40), (self.jgb, 'right', 40)])

        self.myTex3 = cmds.text('�л������������ʾģʽ')
        cmds.formLayout(self.myLayout, e=1,
                        attachForm=[(self.myTex3, 'top', 120), (self.myTex3, 'left', 60), (self.myTex3, 'right', 60)])

        self.myRowLayout = cmds.rowLayout(nc=4, cw4=[80, 80, 80, 80])
        cmds.formLayout(self.myLayout, e=1, attachForm=[(self.myRowLayout, 'top', 140), (self.myRowLayout, 'left', 20),
                                                        (self.myRowLayout, 'right', 20)])
        cmds.button(l='����', w=120, c=lambda *args: self.myBox(0), bgc=self.color[0])
        cmds.button(l='Ԥ��', w=120, c=lambda *args: self.myBox(1), bgc=self.color[1])
        cmds.button(l='����', w=120, c=lambda *args: self.myBox(2), bgc=self.color[0])
        cmds.button(l='����', w=120, c=lambda *args: self.myBox(3), bgc=self.color[1])
        cmds.setParent('..')
        # self.myRowLayout2 = cmds.rowLayout(nc=3,cw3=[100,100,100])
        self.myCol2 = cmds.columnLayout( adj=1,rs=5)
        # cmds.formLayout(self.myLayout,e=1,attachForm = [(self.myRowLayout2,'top',175),(self.myRowLayout2,'left',20),(self.myRowLayout2,'right',20) ] )
        cmds.formLayout(self.myLayout, e=1,
                        attachForm=[(self.myCol2, 'top', 175), (self.myCol2, 'left', 20), (self.myCol2, 'right', 20)])
        # cmds.text('�����������Ը���',al='left')

        cmds.separator( style='doubleDash',h=15 )

        self.myCheck2 = cmds.checkBoxGrp( l='Create Layer Overrde', cal=[1, 'left'], columnWidth2=[150, 165], v1=1)
        
        cmds.rowLayout( nc=3,cw3=[100,100,100])
        cmds.text( 'Object ID')
        cmds.button(l='on',w=100,c=lambda *args: self.proxSet(0, 1),bgc=self.color[0])
        cmds.button(l='off',w=100,c=lambda *args: self.proxSet(0, 0),bgc=self.color[1])
        cmds.setParent('..')
        
        cmds.rowLayout(nc=3,cw3=[100,100,100])
        cmds.text( 'Visibility & Matte')
        cmds.button(l='on',w=100,c=lambda *args: self.proxSet(2, 1),bgc=self.color[0])
        cmds.button(l='off',w=100,c=lambda *args: self.proxSet(2, 0),bgc=self.color[1])
        cmds.setParent('..')
        
        cmds.rowLayout(nc=4,cw4=[100,100,120,120])
        cmds.text( 'Material Mode')
        cmds.button(l='From Proxy',w=100,c=lambda *args: self.proxSet(1, 0),bgc=self.color[0])
        cmds.button(l='From Scene(ass..)',w=120,c=lambda *args: self.proxSet(1, 1),bgc=self.color[1])
        cmds.button(l='From Scene(name.)',w=120,c=lambda *args: self.proxSet(1, 2),bgc=self.color[2])
        cmds.setParent('..')  
        
        '''
        cmds.radioButtonGrp(l='Object ID', labelArray2=['on', 'off'], numberOfRadioButtons=2,
                            on1=lambda *args: self.proxSet(0, 1), on2=lambda *args: self.proxSet(0, 0))
        cmds.radioButtonGrp(l='Material Mode', labelArray3=['From Proxy', 'From Scene(1)', 'From Scene(2)'],
                            numberOfRadioButtons=3, on1=lambda *args: self.proxSet(1, 0),
                            on2=lambda *args: self.proxSet(1, 1), on3=lambda *args: self.proxSet(1, 2))
        cmds.radioButtonGrp(l='Visibility & Matte', labelArray2=['on', 'off'], numberOfRadioButtons=2,
                            on1=lambda *args: self.proxSet(2, 1), on2=lambda *args: self.proxSet(2, 0))'''
        cmds.showWindow(self.myWin)
        cmds.window(self.myWin, e=1, w=560, h=440,sizeable=False)

    def proxSet(self, mode, value):
        over = cmds.checkBoxGrp(self.myCheck2, q=1, v1=1)
        user_attr = ['.idm', '.mm', '.visibilityMode']
        tmp = cmds.ls(sl=1, dag=1, type='mesh')
        if tmp == []:
            #cmds.confirmDialog(m='δѡ������', button='ȷ��')
            cmds.warning('δѡ������')
            return
        rsProxys = cmds.listConnections(tmp, type='RedshiftProxyMesh')
        for i in rsProxys:
            if over == 1:
                if 'defaultRenderLayer' != cmds.editRenderLayerGlobals (q=1, currentRenderLayer=1):
                    cmds.editRenderLayerAdjustment(i + user_attr[mode])
            cmds.setAttr(i + user_attr[mode], value)

    def mySelShape(self, globalObj):
        tmp = cmds.ls(sl=1, dag=1, type='mesh')
        if len(tmp) == 1:
            globalObj = tmp[0]
            return tmp
        else:
            return None

    def setText(self):
        tmp = self.mySelShape(globalObj)
        if tmp != None:
            cmds.textField(self.mytf1, edit=1, tx=tmp[0])
        else:
            cmds.confirmDialog(m='��ѡ��һ��poly����\n  ��Ҫ��ѡ!!!', button='ȷ��')

    def myRsProxy(self):
        tmp = cmds.ls(sl=1, dag=1, type='mesh')
        rsProxys = cmds.listConnections(tmp, type='RedshiftProxyMesh')
        arr = ''
        for i in rsProxys:
            arr += ' %s' % i
        return arr

    def setRsTex(self, txname):
        cmds.textField(txname, e=1, tx=self.myRsProxy())

    def myDoIt(self, txt1, txt2, check):
        source = cmds.textField(txt1, q=1, tx=1)
        target = cmds.textField(txt2, q=1, tx=1)
        target = target.strip().split(' ')
        for i in target:

            if cmds.isConnected(source + '.outMesh', i + '.inMesh'):
                cmds.warning(i + u'�Ѿ�����')

            else:
                try:
                    cmds.connectAttr(source + '.outMesh', i + '.inMesh', f=check)
                except RuntimeError as e:
                    cmds.warning(str(e))

    def myBox(self, value):
        for i in cmds.ls(type='RedshiftProxyMesh'):
            cmds.setAttr(i + '.dm', value)


RsMeshConvert()


