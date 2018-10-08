from glob import glob

basepath = '/home/mehul/Documents/training/python/yannick'
alljpgfiles = glob(basepath + '/*.jpg')
print(alljpgfiles)

allnumberfiles = glob(basepath + '/[0-9]*')
print(allnumberfiles)

alltxtfiles = glob(basepath + '/**/*.txt', recursive=True)
print(alltxtfiles)
