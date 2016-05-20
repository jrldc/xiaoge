#!/usr/bin/python
# -*- coding:utf8 -*-
import re
import urllib
import string
import time
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()


#获取页面代码
def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html


#创建抓取报纸路径以及期次文件夹
def getdir(dirs,papername,html):
	todays = time.strftime('%Y-%m-%d')
	if not os.path.exists(dirs+papername):
		os.mkdir(dirs+papername)
		os.chdir(dirs+papername)
		os.mkdir(todays)
		os.chdir(todays)
		reb = u'\d{3}版'
		html = html.decode('utf8')
		pre =re.compile(reb)
		erlist = re.findall(pre,html)
		for purl in perlist:
			purl = purl.replace('版','')
			print purl
			if not os.path.exists(purl):
				os.mkdir(purl)
	
	else:
		os.chdir(dirs+papername)
		if not os.path.exists(todays):
			os.mkdir(todays)
			os.chdir(todays)
			reb = u'\d{3}版'
			html = html.decode('utf8')
			pre =re.compile(reb)
			perlist = re.findall(pre,html)
			for purl in perlist:
				purl = purl.replace('版','')
				print purl
				if not os.path.exists(purl):
					os.mkdir(purl)
		
	os.chdir(dirs+papername)
	print os.getcwd()


#获取期次图片
def getPage(html,url):
	#创建期次文件夹
	reg = r'node_\d{1,2}\.htm'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	print imglist
	for imgurl in imglist:
		print imgurl
		imgurl=url + 'html/'+time.strftime('%Y-%m/%d/')+imgurl
		html2=getHtml(imgurl)
		reg2=r'img src=.*?\.jpg'
		imgre2 = re.compile(reg2)
		imglist2=re.findall(imgre2,html2)
		for imgurl2 in imglist2:
			jpgname = imgurl2.replace('img src=../../../page/1/','')
			imgurl2=url + imgurl2.replace('img src=../../../','')
			print imgurl2
			print jpgname
			try:				
				urllib.urlretrieve(imgurl2,jpgname)
			except:
				print "Unexcepted error:",sys.exc_info()[0]  


#获取pdf		
def getPdf(html,url):
	reg = r'right> <a href=.*?\.pdf'
	pdfre = re.compile(reg)
	pdflist = re.findall(pdfre,html)
	print pdflist
	for pdfurl in pdflist:
		pdfname = pdfurl.replace('right> <a href=../../../page/1/','')
		pdfurl = url + pdfurl.replace('right> <a href=../../../','')
		print pdfurl
		print pdfname
		try:
			urllib.urlretrieve(pdfurl,pdfname)
		except:
			print "Unexcepted error:",sys.exc_info()[0]  

html = getHtml("http://www.cqwb.com.cn/cqwb/html/2015-01/12/node_2.htm")
getdir("d:\\",unicode("重庆晚报",'utf-8'),html)
getPage(html,"http://www.cqwb.com.cn/cqwb/")
#getPdf(html,"http://www.cqwb.com.cn/cqwb/")

