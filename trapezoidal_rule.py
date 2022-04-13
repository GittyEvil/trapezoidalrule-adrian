import matplotlib.pyplot as plt
import numpy as np
#våran f(x)=y och a,b,n värden
f = lambda x : 1/(1 + x**2)
a = 0; b = 5; N = 10


x = np.linspace(a,b,N+1)
y = f(x)


X = np.linspace(a,b,100)
Y = f(X)
plt.plot(X,Y)
#själva trapetsregel formeln
for i in range(N):
    xs = [x[i],x[i],x[i+1],x[i+1]]
    ys = [0,f(x[i]),f(x[i+1]),0]
    plt.fill(xs,ys,'b',edgecolor='b',alpha=0.2)
#titel och show för att visa grafen
plt.title('Trapezoid Rule, N = {}'.format(N))
plt.show()
