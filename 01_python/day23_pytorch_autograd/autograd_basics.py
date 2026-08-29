import torch
import torch.optim as optim

x = torch.tensor(2.0, requires_grad=True)
y = x ** 2
print('x:',x)
print('y:',y)

y.backward()
print('x的梯度：',x.grad)

x = torch.tensor(3.0, requires_grad=True)
y = x*2
z = y ** 2
print('x:',x)
print('y:',y)
print('z:',z)

z.backward()
print('x的梯度：',x.grad)

x = torch.tensor(2.0, requires_grad=True)
y = x ** 2
y.backward()
print('第一次梯度：',x.grad)

y = x ** 2
y.backward()
print('第二次之后的梯度：',x.grad)

x.grad.zero_()
print('清零后的梯度：',x.grad)



# w = torch.tensor(0.0, requires_grad=True)
# learning_rate = 0.1

# for epoch in range(30):
#     loss = (w - 3) ** 2

#     if w.grad is not None:
#         w.grad.zero_()

#     loss.backward()

#     with torch.no_grad():
#         w -= learning_rate * w.grad

#     print('epoch:', epoch,'w:',w.item(),'loss:',loss.item())



w = torch.tensor(0.0,requires_grad=True)
optimizer = optim.SGD([w],lr=0.1)

for epoch in range(10):
    loss = (w - 3) ** 2
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    print('epoch:',epoch,'w:',w.item(),'loss:',loss.item())