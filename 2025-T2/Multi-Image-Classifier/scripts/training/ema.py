import copy, torch

class ModelEMA:
    def __init__(self, model, decay=0.9998, device=None):
        self.ema = copy.deepcopy(model).eval()
        for p in self.ema.parameters(): p.requires_grad_(False)
        self.decay = decay
        if device is not None: self.ema.to(device=device)
    @torch.no_grad()
    def update(self, model):
        d = self.decay
        for ema_p, p in zip(self.ema.parameters(), model.parameters()):
            if ema_p.dtype.is_floating_point:
                ema_p.copy_(ema_p * d + p.detach() * (1. - d))
        for ema_b, b in zip(self.ema.buffers(), model.buffers()):
            ema_b.copy_(b)
