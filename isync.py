#!/usr/bin/python3.7
from sys import stdin,stderr,stdout
from string import ascii_uppercase,ascii_lowercase,digits
from random import choice
from argparse import ArgumentParser
from time import time
 
 
p=ArgumentParser()
p.add_argument('-S', '--orig', help='Servidor de origen', default=False)
p.add_argument('-D', '--dest', help='Servidor de destino', default=False)
p.add_argument('-p', '--pswd', help='Longitud de la password generada. Por def. 15',default=15, type=int)
p.add_argument('-P', '--origenp', help='Se utiliza la misma password en destino que en origen', action='store_true')
p.add_argument('-c', '--cliente', help='Deprecated',action='store_true')
pa=p.parse_args()
start = time()
CHARS=ascii_lowercase+digits+ascii_uppercase
 
def parseIn():
    #arr=open('prueba.txt', 'r').readlines()
    arr=stdin.readlines()
    if len(arr[0].split('|'))==1:
        p=genPass(pa.pswd)
        return [f'{l}|{p}' for l in arr]
    return arr
 
def genPass(l):
    return ''.join([choice(CHARS) for x in range(l)])
 
def main():
    r=[[j.strip() for j in i.split('|') if j and j.strip()!='']+[genPass(pa.pswd)]for i in parseIn()]
    ix=1
    if not pa.origenp:
        ix=2
    sc='\n\n'.join([f'Email: {k[0]}\nContraseña: {k[ix]}' for k in r])
    if pa.cliente:
        return sc
    else:
        sc+='\n\n-----------------------------------IMAPSYNC-------------------------------\n\n'
        if not pa.orig or not pa.dest:
            return 'Falta origen y/o destino'
        return sc+'\n'.join([f'{pa.orig};{k[0]};{k[1]};{pa.dest};{k[0]};{k[ix]};'for k in r])
 
if __name__ == "__main__":
    stdout.write(main()+'\n')
    print(time()-start)
