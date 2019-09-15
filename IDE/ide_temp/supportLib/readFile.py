def writeFile(text, className):
    file = open('ide_temp/source/' + className + '.java', 'w')
    file.write(text)
    file.close()


if __name__ == '__main__':
    writeFile('default', 'Raze')
