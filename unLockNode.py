# -*- coding: utf-8 -*-
# ������������
# designed by Jiaguobao
# QQ:779188083 && Tel:15615026078
# Date:2018��10��28��
# ��������������ɾ�������޷������������������re�������ļ��������������ˣ�ִ�нű���������
import pymel.core as pm
from maya.OpenMaya import MGlobal
def unLock():
	a=pm.ls()
	for i in a:
		i.unlock()
	MGlobal.displayInfo(u'������ϣ�')
if __name__ == '__main__':
	unLock()
