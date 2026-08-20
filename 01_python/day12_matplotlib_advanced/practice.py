import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

fig, axes = plt.subplots(2,2, figsize=(10,8))

axes[0,0].plot(
    x,
    y,
    marker='o',
    linewidth=2,
    label='y = 2x'
)
axes[0,0].legend()
axes[0,0].grid()

axes[0,1].bar(x,y)
axes[0,1].set_xlim(0,6)
axes[0,1].set_ylim(0,12)

axes[1,0].scatter(x,y, alpha=0.5)

axes[1,1].hist(y)

axes[0,0].set_title('Line Chart')
axes[0,0].set_xlabel('x')
axes[0,0].set_ylabel('y')

axes[0,1].set_title('Bar Chart')
axes[0,1].set_xlabel('x1')
axes[0,1].set_ylabel('y1')

axes[1,0].set_title('Scatter Chart')
axes[1,0].set_xlabel('x2')
axes[1,0].set_ylabel('y2')

axes[1,1].set_title('Histogram')
axes[1,1].set_xlabel('x3')
axes[1,1].set_ylabel('y3')

fig.suptitle('Matplotlib Multiple Charts')
plt.tight_layout()
plt.show()