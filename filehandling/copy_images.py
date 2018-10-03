source = '/Users/mehul.chopra/Downloads/sample_img.jpeg'
dest = '/Users/mehul.chopra/Desktop/sample_img_copy.jpeg'

fs = open(source, mode='rb')
fd = open(dest, mode='wb')

fd.write(fs.read())

# avoiding memory leaks
# python program fs, fd -> referencing system resources (files)

# always close file references once work done with them
fs.close()
fd.close()
