import matplotlib.pyplot as plt

x=[x for x in range(-10,10)]
y=[2*t for t in x]

plt.plot(x,y,marker='o') #x,y로 만들어라
plt.axis([-20,20,-20,20]) #간격
plt.show()