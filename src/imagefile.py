from PIL import Image
import random

class ImageFile():
    def __init__(self, filePath, fileName):
        self._filePath=filePath
        self._fileName=fileName
        self._file=Image.open(filePath)
        self._file=self._file.convert('RGBA')
        self._EOT_CODE='00000100'
        self._NUL_CODE='00000000'
        self.pix=self._file.load()
        self.avalSpace=(self._file.size[0]*(self._file.size[1]))/8

    def __del__(self):
        self._file.close()

    def BinaryEncrypt(self, binary, keyX, keyY):
        Xindex=[x for x in range(0,self._file.size[0])]
        Yindex=[x for x in range(0,self._file.size[1])]
        random.Random(keyX).shuffle(Xindex)
        random.Random(keyY).shuffle(Yindex)
        result=[]
        decode=''
        for i,b in enumerate(binary):
            decode.join(str(self.pix[Xindex[i],Yindex[i]][3]-254))
            self.pix[Xindex[i],Yindex[i]]=(pixel[0], pixel[1], pixel[2], 255-ord(b)+49);
        self._file.save("./"+self._fileName+"_encrypt.png")

    def BinaryEncrypt(self, binary, keyX, keyY):
        Xindex=[x for x in range(0,self._file.size[0])]
        Yindex=[x for x in range(0,self._file.size[1])]
        random.Random(keyX).shuffle(Xindex)
        random.Random(keyY).shuffle(Yindex)
        binary=binary+self._EOT_CODE
        for i,b in enumerate(binary):
            pixel=self.pix[Xindex[i],Yindex[i]]
            self.pix[Xindex[i],Yindex[i]]=(pixel[0], pixel[1], pixel[2], 254+ord(b)-49);
        self._file.save("./"+self._fileName+"_encrypt.png")
