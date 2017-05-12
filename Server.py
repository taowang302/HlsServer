#-*- coding: UTF-8 -*-

import os
import HashManger
from urlparse import urlparse

class HlsServer():
	"""docstring for HlsServer"""
	def __init__(self):
		#self.arg = arg
		#print 'init'
		self.phy_path = ''
		self.proxy_host = ''
		self.host_hash = HashManger.YHash(["127.0.0.1", "192.168.1.1","12.12.12"])  
		self.dir_hash = HashManger.YHash(["1","2","3","4","5","6","7","8","9"])  
		self.content_dic ={}
		self.read_config()
		
	def chose_host(self,contentid):
		return self.host_hash.get_node(contentid)

	def chose_dir(self,contentid):
		return self.dir_hash.get_node(contentid)


	def parse_url(self,url):
		iten = urlparse(url).query.split('&')
		contentid = iten[0].split('=')[1]
		request_file = iten[1].split('=')[1]
		return contentid,request_file


	def check_memory(self,contentid,request_file):
		if contentid in self.content_dic.keys():
			if request_file in self.content_dic.get(contentid).keys():
				return True
			else:
				return False
		else:
			return False

	def check_phy_file(self,filename):
		if os.path.exists(filename):
			return True
		else:
			return False

	def read_config(self):
		self.phy_path = '/Users/wangtao/Documents/Interest/'
		self.content_dic = {'cp001':{'c0_1':{'con':'exists','proxy':1,'hot':1},'c1_2':{'con':'exists','proxy':0,'hot':111}},'cp002':{'c0_1':{'con':'1111','proxy':1,'hot':11111}}}
		self.proxy_host = '192.168.1.1:9090'

	def get_proxy(self,contentid,request_file):
		print 'go to proxy'
		self.content_dic.setdefault(contentid,{})[request_file]={'con':'1122','proxy':1,'hot':1}
		print self.content_dic

	def read_file(self):
		pass

	def write_file(self):
		pass

	def control_center(self,url):
		contentid,request_file = self.parse_url(url)
		filename = '{}/{}/{}.ts'.format(self.phy_path,self.chose_dir(contentid),contentid)
		if self.check_memory(contentid,request_file):
			print 'request file in memory'
		elif self.check_phy_file(filename):
			print 'request fil in phy'
		else:
			self.get_proxy(contentid,request_file)



class LoadProxyFile():
	def __init__(self,content_dic):
		self.content_dic = content_dic

	def sort_for_hot(self):
		hot_list = []
		for item in self.content_dic:
			for itemin in self.content_dic.get(item):
				hot_list.append('{}_{}_{}'.format(item,itemin,self.content_dic.get(item).get(itemin).get(hot)))
		



if __name__ == '__main__':
	hhls = HlsServer()
	hhls.control_center('http://127.0.0.1:8080/cp001?Contentid=cp001&offset=c0_3')

#	for i in range(100):
#		print hhls.chose_host('cp001')
#		print hhls.chose_dir('cp001')
#		print "--------第{}轮----------\n".format(i)



