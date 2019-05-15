#! /usr/bin/python3
# -*- coding: utf-8 -*-
__author__    = "Pierre Etheve"
__email__  = "pierre.etheve.lfdv@gmail.com"

import urllib.request as rq
import sys

unique_pins = []
start = 0
folder = "pins"
source = "estampe_pinimg.txt"

def getOptions() :
	global folder, start, source
	args = sys.argv
	option = ""
	for el in sys.argv :
		if el[0] != "-" :
			if option == "path" :
				folder = el
				print("Setting path to %s"%folder)
			elif option == "start" :
				start = int(el)
				print("Setting start to %d"%start)
			elif option == "source" :
				source = el
				print("Setting start to %s"%source)

			option = ""

		else :
			option = el[1:]

def getPins() :
	for i in range(start, len(unique_pins)) :
		link = unique_pins[i]
		rq.urlretrieve(link, "%s/%05d.jpg"%(folder, i))
		print("Saving to %s/%05d.jpg"%(folder,i))

if len(sys.argv) == 1 :
	print("./pin_dl.py -path [DESTINATION FOLDER] -start [SKIP TO # PIN] -source [xxx_pinimg.txt]")
	sys.exit()

getOptions()

with open(source) as infile : 
	for line in infile :
		if "4x" in line :
			link = line.split(", ")[-1][:-3]
			if link not in unique_pins :
				unique_pins.append(link)
print("Found %d unique pins"%len(unique_pins))

getPins();