
# -*- coding: utf-8 -*-
# ����ѡ������������������
# designed by Jiaguobao
# QQ:779188083 && Tel:15615026078
# Date:2018��10��14��
# version 1.0

# 
# 1.ѡ������
# 2.ִ�нű�
# 3.����ѡ����ȫ����͵��������y�����


from maya.OpenMaya import MGlobal
#������������
def doit():
	tr = cmds.ls(sl=1,dag=1,tr=1)
	for i in tr:
		bb = cmds.xform(i,q=1,bb=1)
		cmds.xform(i,r=1,t=[0,-bb[1],0])
MGlobal.displayInfo(u'ִ�����')

if __name__ == '__main__':
	doit()

