
import torch.nn as nn
import torch.nn.functional as F


class MLP(nn.Module):
    def __init__(self, num_in, num_out):
        super(MLP, self).__init__()
        
        # Define layers
        self.fc1 = nn.Linear(num_in, 32)
        self.fc2 = nn.Linear(32, 64)
        self.fc3 = nn.Linear(64, 64)
        self.fc4 = nn.Linear(64, num_out)
        
        # Define dropout layer
        self.dropout = nn.Dropout(p=0.2)
        
    def forward(self, x):
        # Forward pass through layers
        x = F.relu(self.fc1(x))
        # x = self.dropout(x)
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        # x = nn.Softmax(x)
        return x


# class MLP(nn.Module):

#     def __init__(self, num_in, num_out):
#         super().__init__()
        
#         self.network = nn.Sequential(nn.Linear(num_in, 32),
#                                      nn.ReLU(),
#                                      nn.Linear(32, 64),
#                                      nn.ReLU(),
#                                      nn.Linear(64, 64),
#                                      nn.ReLU(),
#                                      nn.Linear(64, num_out),
#                                      nn.Softmax())


#     def forward(self, x):
#         return self.network(x)
    
