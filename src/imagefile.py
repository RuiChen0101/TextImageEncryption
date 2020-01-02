from PIL import Image
import random

class ImageFile():
    def __init__(self, filePath, fileName):
        self._filePath=filePath
        self._fileName=fileName
        self._file=Image.open(filePath)
        self._file=self._file.convert('RGBA')
        self._EOT_CODE='00000100'
        self._NUL_CODE='11111111'
        self.pix=self._file.load()
        self.avalSpace=(self._file.size[0]*(self._file.size[1]))/8

    def __del__(self):
        self._file.close()

    def BinaryDecrypt(self, keyX, keyY):
        Xindex=[x for x in range(0,self._file.size[0])]
        Yindex=[x for x in range(0,self._file.size[1])]
        random.Random(keyX).shuffle(Xindex)
        random.Random(keyY).shuffle(Yindex)
        state=True
        result=[]
        decode=""
        i=0
        while(True):
            decode+=str(self.pix[Xindex[i],Yindex[i]][3]-254)
            print(decode)
            if len(decode)==8:
                if decode==self._EOT_CODE:
                    break
                elif decode==self._NUL_CODE:
                    state=False
                    break
                else:
                    result.append(decode)
                    decode=""
            i+=1
        return state, result


    def BinaryEncrypt(self, binary, keyX, keyY):
        Xindex=[x for x in range(0,self._file.size[0])]
        Yindex=[x for x in range(0,self._file.size[1])]
        random.Random(keyX).shuffle(Xindex)
        random.Random(keyY).shuffle(Yindex)
        binary=binary+self._EOT_CODE
        for i,b in enumerate(binary):
            pixel=self.pix[Xindex[i],Yindex[i]]
            if b=='0':
                self.pix[Xindex[i],Yindex[i]]=(pixel[0], pixel[1], pixel[2], 254)
            else:
                self.pix[Xindex[i],Yindex[i]]=(pixel[0], pixel[1], pixel[2], 255)
        self._file.save("./"+self._fileName+"_encrypt.png")
