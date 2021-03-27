class Data:
    def __init__(self, img, psnr=None, time=None, ssim=None, mse=None):
        self.img = img
        self.psnr = psnr
        self.time = time
        self.ssim = ssim
        self.mse = mse
