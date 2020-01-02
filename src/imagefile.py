from PIL import Image
import random
import itertools

class ImageFile():
    def __init__(self, filePath, fileName):
        self._filePath=filePath
        self._fileName=fileName
        self._file=Image.open(filePath)
        self._file=self._file.convert('RGBA')
        self._EOT_CODE='00000100'
        self._NUL_CODE='11111111'
        self.pix=self._file.load()
        self.avalSpace=(self._file.size[0]*self._file.size[1])/8
        self.Xindex=[x for x in range(0,self._file.size[0])]
        self.Yindex=[x for x in range(0,self._file.size[1])]

    def __del__(self):
        self._file.close()

    def BinaryDecrypt(self, key):
        points=list(itertools.product(self.Xindex, self.Yindex))
        random.Random(key).shuffle(points)
        state=True
        result=[]
        decode=""
        i=0
        while(True):
            point=points[i]
            decode+=str(self.pix[point[0],point[1]][3]-254)
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

    def BinaryEncrypt(self, binary, key):
        points=list(itertools.product(self.Xindex, self.Yindex))
        random.Random(key).shuffle(points)
        binary=binary+self._EOT_CODE
        for i,b in enumerate(binary):
            point=points[i]
            pixel=self.pix[point[0],point[1]]
            if b=='0':
                self.pix[point[0],point[1]]=(pixel[0], pixel[1], pixel[2], 254)
            else:
                self.pix[point[0],point[1]]=(pixel[0], pixel[1], pixel[2], 255)
        self._file.save("./"+self._fileName+"_encrypt.png")
