import pytorch_lightning as pl
import torch
import torch.nn as nn

class TokenIdentifier(pl.LightningModule):
    def __init__(self, input_size, hidden_size):
        super().__init__()
        self.input_size = input_size
        self.hidden_size  = hidden_size
        self.activation = torch.nn.GELU()
        self.loss_fn = torch.nn.CosineEmbeddingLoss()
        self.layers = torch.nn.Sequential(
                torch.nn.Linear(self.input_size, self.hidden_size),
                self.activation,
                torch.nn.Linear(self.hidden_size, self.hidden_size),
                self.activation,
                torch.nn.Linear(self.hidden_size, self.input_size),
            )

    def forward(self, x):
        return self.layers(x)
    
    def _shared_eval_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self.layers(x)
        labels = torch.tensor(-1).repeat(x.size(0)) # -1 specifies distance. We want to minimize distance.
        loss = self.loss_fn(y_hat, y, labels) 
        return loss
    
    def training_step(self, batch, batch_idx):
        loss = self._shared_eval_step(batch, batch_idx)
        self.log('train_loss', loss, on_step=True, on_epoch=True)
        return loss
    
    def validation_step(self, batch, batch_idx):
        loss = self._shared_eval_step(batch, batch_idx)
        self.log('val_loss', loss, on_epoch=True)
        return loss
    
    def predict_step(self, batch, batch_idx, dataloader_idx=0):
        y_hat = self.layers(x)
    
    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=0.0001)