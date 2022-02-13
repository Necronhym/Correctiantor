import pandas
from tkinter import filedialog as fd
import ctypes

ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )

dictionary = {
    'А':'A',
    'а':'a',
    'Е':'E',
    'е':'e',
    'К':'K',
    'к':'k',
    'Ј':'J',
    'ј':'j',
    'М':'M',
    'м':'m',
    'О':'O',
    'о':'o',
    'Б':'B',
    'б':'b',
    'В':'V',
    'в':'v',
    'Г':'G',
    'г':'g',
    'Д':'D',
    'д':'d',
    'Ж':'Z',
    'ж':'z',
    'З':'Z',
    'з':'z',
    'И':'I',
    'и':'i',
    'Л':'L',
    'л':'l',
    'Н':'N',
    'н':'n',
    'П':'P',
    'п':'p',
    'Р':'R',
    'р':'r',
    'С':'S',
    'с':'s',
    'Т':'T',
    'т':'t',
    'У':'U',
    'у':'u',
    'Ф':'F',
    'ф':'f',
    'Х':'H',
    'х':'h',
    'Ц':'C',
    'ц':'c',
    'Ч':'C',
    'ч':'c',
    'Ш':'S',
    'ш':'s',
    'Љ':"Lj",
    'љ':"lj",
    'Њ':"Nj",
    'њ':"nj",
    'Ћ':'C',
    'ћ':'c',
    'Ђ':'D',
    'ђ':'d',
    'Џ':'Dz',
    'џ':'dz',
    'Č':'C',
    'č':'c',
    'Ć':'C',
    'ć':'c',
    'Đ':'D',
    'đ':'d',
    'Š':'S',
    'š':'s',
    'Ž':'Z',
    'ž':'z',
    '„':",,",
    '”':"\'\'",
    '–':'-',
    '“':"\'\'",
    "…":"...",
    '’':"\'"
}
filename = fd.askopenfilename()
df = pandas.read_excel(filename, index_col=False)
for i in df.columns:
    j = i
    for k in dictionary:
        i = i.replace(k, dictionary[k])
    df.rename(columns={j:i}, inplace=True)
df.replace(dictionary, regex=True, inplace=True)
df.to_csv(filename.rsplit(".", 1)[0] + ".csv", index=False)
