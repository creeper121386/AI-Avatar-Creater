import os
if __package__:
    from . import model64
else:
    import model64
import torch
import torchvision
cuda = True
device = torch.device(
    'cuda') if torch.cuda.is_available() and cuda else torch.device('cpu')
nz = 100
choose = 8
'''model=3 for soft , 4 for normal'''
#########################    
# mode = 0   # '0 for normal style, 1 for soft style, -1 to debug')
# tune = False
# out_num = 1       #'num of output images.'
# batch_size = 1       #how many figures in a output image.')
# modelNum = [x*10+1 for x in range(10)]+[100]

#workDir = os.getcwd()
# modelPath = '/run/media/why/DATA/why的程序测试/AI_Lab/AI-Avatar-Creater/demo_AnimeGAN/model_normal'
basedir = os.path.dirname(__file__)
modelPath = basedir + '/../models/demo_AnimeGAN/model_normal'
if __name__ =='__main__':
        modelPath = '/run/media/why/DATA/why的程序测试/AI_Lab/AI-Avatar-Creater/hackweek/app/models/demo_AnimeGAN/model_normal'
# savePath = workDir + '/output'
# batchSize = opt.batch_size
#################################################

class TestNet(object):
    def __init__(self, out_path, mode, modelNum, img_num, batch_size, tune):
        self.G = model64.G().to(device)
        self.mode = mode
        self.out_path = out_path
        self.modelNum = modelNum
        self.img_num = img_num
        self.batch_size = batch_size
        self.tune = tune

################ init noise code z: #################

    def init(self):
        if self.tune:
            self.img_num = 1
            tmp = torch.randn(nz, 1, 1)
            initZ = torch.randn(self.batch_size, nz, 1, 1)
            for i in range(nz-5):
                for j in range(self.batch_size):
                    initZ[j][i] = tmp[i]
            self.initZ = initZ.to(device)

###################### test:#########################
    def test(self):
        for n in self.modelNum:
            GmodelPath = modelPath + '/Gnn-epoch{}.pkl'.format(n)
            self.G.load_state_dict(torch.load(GmodelPath))
            for i in range(self.img_num):
                if self.tune:
                    z = self.initZ
                else:
                    z = torch.randn(self.batch_size, nz, 1, 1).to(device)
                torchvision.utils.save_image(self.G(z).detach(
                ), self.out_path, normalize=True)
        print('\033[1;36;40m  generate over! \033[0m')

    # 忘记保存辨别器的模型了QAQ...结果新功能用不了...太惨了
    # def test_choose(self):
    #     self.D = model64.D().to(device)
    #     self.tune = False
    #     for n in self.modelNum:
    #         GmodelPath = modelPath + '/Gnn-epoch{}.pkl'.format(n)
    #         DmodelPath = modelPath + '/Dnn-epoch{}.pkl'.format(n)
    #         self.G.load_state_dict(torch.load(GmodelPath))
    #         self.D.load_state_dict(torch.load(DmodelPath))
    #         for i in range(self.img_num):
    #             tmp = z = torch.randn(self.batch_size, nz, 1, 1).to(device)
    #             for j in range(self.batch_size):
    #                 z = torch.randn(self.choose, nz, 1, 1).to(device)
    #                 out = self.G(z).detach()
    #                 score = self.D(out)
    #                 ix = int(torch.argmax(score))
    #                 tmp[j] = out[ix]
    #             
    #             torchvision.utils.save_image(tmp, self.out_path, normalize=True)
    #     print('\033[1;36;40m  generate over! \033[0m')

############## load model: ###############
#Dnn = D()
# Dnn.load_state_dict(torch.load(modelPath))

def main(out_path, mode, model_num=0, img_num=4, batch_size=1, tune=False):
    modelNum = [41, 61, 81, '20_1'] if mode==4 else [31, 71, '_origin']
    modelNum = [modelNum[model_num], ]
    testNet = TestNet(out_path, mode, modelNum, img_num, batch_size, tune)
    testNet.init()
    testNet.test()
    #testNet.test_choose()

if __name__ == '__main__':
    main(out_path='./test.jpg', mode=4, model_num=3, img_num=1, batch_size=8, tune=0)
