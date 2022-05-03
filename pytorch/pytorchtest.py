import torch;
import numpy as np;

data = [[1, 2], [3, 4]];
x_data = torch.tensor(data);

shape = (2, 3,);
rand_tensor = torch.rand(shape);
ones_tensor = torch.ones(shape);
zeros_tensor = torch.zeros(shape);

print(f"Random Tensor: \n {rand_tensor} \n");
print(f"Ones Tensor: \n {ones_tensor} \n");
print(f"Zeros Tensor: \n {zeros_tensor}");


import torchvision;


model = torchvision.models.resnet18(pretrained=True);
data = torch.rand(1, 3, 64, 64);
labels = torch.rand(1, 1000);

prediction = model(data);

loss = (prediction - labels).sum();
loss.backward(); # backward pass

optim = torch.optim.SGD(model.parameters(), lr=1e-2, momentum=0.9);

optim.step(); #gradient descent


a = torch.tensor([2., 3.], requires_grad=True);
b = torch.tensor([6., 4.], requires_grad=True);

Q = 3*a**3 - b**2;

external_grad = torch.tensor([1., 1.]);
Q.backward(gradient=external_grad);



model = torchvision.models.resnet18(pretrained=True);
for param in model.parameters():
    param.requires_grad = False;

model.fc = torch.nn.Linear(512, 10);
optim = torch.optim.SGD(model.parameters(), lr=1e-2, momentum=0.9);





