from tutorial_1 import *

theta=np.linspace(0, 10, 100)
nu=np.linspace(0, 10, 100)
N=3
M=7
plt.figure(figsize=(8,6))

theta_grid, nu_grid = np.meshgrid(theta, nu)

L_ex = L(theta_grid, nu_grid, N, M)

low = 0
high=10
N_live_points = 30
live_points = np.random.uniform(low,high,size=(N_live_points,2))
L_live = L(live_points[:,0],live_points[:,1],N,M)



plt.scatter(live_points[:,0],live_points[:,1],c=L_live,cmap='magma', label='live points')


plt.contour(theta_grid, nu_grid, L_ex, cmap='magma')  
#cmaps: 'magma', 'inferno', 'cividis', 




plt.colorbar(label='Likelihood')
plt.xlabel('theta')
plt.ylabel('nu') 
plt.title('Likelihood Heatmap')
plt.legend()
plt.show()
