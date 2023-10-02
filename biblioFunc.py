def tri(liste):
    x=len(liste)
    for i in range(x):
        for j in range(i, x):
            if liste[j]<liste[i]:
                temp = liste[i]
                liste[i]=liste[j]
                liste[j]=temp
    return liste

def getFileName_2(s):
    r = s[:-4]
    r = r.split(' ')
    n = ''
    for x in range(len(r)):
        if x != 0:
            n = f'{n}_{r[x]}'
        else:
            n=r[0]
    return n


# format filname.extension
def creerImage(filename, path, x):
    import pypdfium2 as pdfium
    from os import chdir, mkdir
    from os.path import join, normpath, expanduser, exists
    pdf = pdfium.PdfDocument(path)
    page = pdf.get_page(0)
    pil_image = page.render(
        scale = 1,
        rotation=0,
        crop=(0,0,0,0),
    )
    out = normpath(expanduser('~/documents/Bibliotheque'))
    
    try:
        chdir(out)
    except FileNotFoundError:
        out = normpath(expanduser('~/documents'))
        chdir(out)
        mkdir('Bibliotheque')
        out = join(out, 'Bibliotheque')
        chdir(out)
    title = f'{getFileName_2(filename)}.png'
    img = pil_image.to_pil()
    if not exists(join(out, title)):
        img.save(title)
    else:
        print('Already exist')
    pat = join(out, title)
    return pat


def createDataSet(path):
    import os
    liste = {}
    for root, dirs, files in os.walk(path):
        for el in files:
            if el.endswith('.pdf'):
                liste[el] = os.path.join(root, el)
    return liste

def getThePath(data, filename):
    path = data.get(filename)
    return path

def getTheFilename(data, path):
    fn = data.get(path)
    return fn

def showAllFiles(data):
    files = []
    for a in data.keys():
        files.append(a)
    return files

def showAll(data):

    allData = {}
    i = 0
    filenames = showAllFiles(data)
    for fn in filenames:
        p = getThePath(data, fn)
        p_i = creerImage(fn, p, i)
        i+=1
        allData[fn] = [p, p_i]
        print(f'===> {i} files analysis on {len(filenames)}')
    print('The analysis files are completed')
#    except FileExistsError:
 #       pass
  #  finally:
    return allData



def lireAudio(path):
    import PyPDF2, pyttsx3
    path = open(path, 'rb')
    pdfReader = PyPDF2.PdfReader(path)
    speak = pyttsx3.init()
    for pages in range(len(pdfReader.pages)):
        text = pdfReader.pages[pages].extract_text()
        speak.say(text)
        speak.runAndWait()
    speak.stop()
    
from os import path

path = path.normpath(path.expanduser("~/desktop"))
data = createDataSet(path)
showAll(data)