#!/usr/bin/python3.7
from sys import stdin, stdout

l=[[j.strip() for j in i.split('|') if j.strip()!=''] for i in stdin.readlines()]
d=["\n".join([i[0]+","+j.strip()for j in i[1].split(',')]) for i in l]
stdout.write("Source,Target\n")
stdout.write("\n".join(d))
	
