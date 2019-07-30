'''
Crie um programa que leia um valor em metros e mostre sua conversão em centímetros e milímetros.
'''
n = float(input('Uma distncia em metros: '))
km = n/1000
hm = n/100
dam = n/10
dm = n*10
cm = n*100
mm = n*1000
print('A medida de {}m corresponde a {}km, {}hm, {}dam, {:.0f}dm, {:.0f}cm e {:.0f}mm'.format(n,km,hm,dam,dm,cm,mm))