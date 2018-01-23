import warnings

from builtins import str

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
# import warnings
# warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import gensim
import sys



try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import MusicTitleEstimator_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel_1 (root)
    MusicTitleEstimator_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel_1 (w)
    MusicTitleEstimator_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:

    def generate(self):
        text = self.Text1.get("1.0","end-1c")
        #self.showLabel.configure(text=text)


        tokenizer = RegexpTokenizer(r'\w+')
        en_stop = get_stop_words('en')
        p_stemmer = PorterStemmer()
        doc_set = [text]
        texts = []
        for i in doc_set:
            raw = i.lower()
            tokens = tokenizer.tokenize(raw)
            stopped_tokens = [i for i in tokens if not i in en_stop]
            texts.append(stopped_tokens)
        dictionary = corpora.Dictionary(texts)
        corpus = [dictionary.doc2bow(text) for text in texts]
        ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=1, id2word=dictionary, passes=20)
        value = ldamodel.print_topics(num_topics=1, num_words=1)
        mystring = ' '.join(str(v) for v in value)
        rafa = ''.join(e for e in mystring if e.isalnum())
        result = ''.join(i for i in rafa if not i.isdigit())
        #with text as f:
        #for line in text:
        #       if result in line:
        #           break
        #print(result)

        for line in text.split('\n'):
            if result in line:
                self.showLabel.configure(text=line)
                break





        #self.showLabel.configure(text=line)


    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font10 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 1 -overstrike 0"
        font9 = "-family {Segoe UI} -size 20 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 11 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("736x617+376+3")
        top.title("Music Title Estimation")
        top.configure(background="#d9d9d9")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.24, rely=0.05, height=61, width=384)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Music Title Estimation''')
        self.Label1.configure(width=384)

        #self.txtLabel = Entry(top)
        #self.txtLabel.place(relx=0.12, rely=0.23, relheight=0.41, relwidth=0.75)
        #self.txtLabel.configure(background="white")
        #self.txtLabel.configure(disabledforeground="#a3a3a3")
        #self.txtLabel.configure(font=font10)
        #self.txtLabel.configure(foreground="#000000")
        #self.txtLabel.configure(insertbackground="black")
        #self.txtLabel.configure(show="Put your lyrics here")
        #self.txtLabel.configure(width=554)

        #self.Entry1 = Entry(top)
        #self.Entry1.place(relx=0.26, rely=0.21, relheight=0.03, relwidth=0.22)
        #self.Entry1.configure(background="white")
        #self.Entry1.configure(disabledforeground="#a3a3a3")
        #self.Entry1.configure(font="TkFixedFont")
        #self.Entry1.configure(foreground="#000000")
        #self.Entry1.configure(insertbackground="black")
        #self.Entry1.configure(justify=CENTER)

        self.Text1 = Text(top)
        self.Text1.place(relx=0.12, rely=0.19, relheight=0.53, relwidth=0.75)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=554)
        self.Text1.configure(wrap=WORD)



        self.btnGenerate = Button(top)
        self.btnGenerate.place(relx=0.41, rely=0.89, height=34, width=147)
        self.btnGenerate.configure(activebackground="#d9d9d9")
        self.btnGenerate.configure(activeforeground="#000000")
        self.btnGenerate.configure(background="#d9d9d9")
        self.btnGenerate.configure(disabledforeground="#a3a3a3")
        self.btnGenerate.configure(foreground="#000000")
        self.btnGenerate.configure(highlightbackground="#d9d9d9")
        self.btnGenerate.configure(highlightcolor="black")
        self.btnGenerate.configure(pady="0")
        self.btnGenerate.configure(text='''Generate''')
        self.btnGenerate.configure(width=147)
        self.btnGenerate.configure(command=self.generate)

        self.showLabel = Label(top)
        self.showLabel.place(relx=0.14, rely=0.79, height=21, width=544)
        self.showLabel.configure(background="#d9d9d9")
        self.showLabel.configure(disabledforeground="#a3a3a3")
        self.showLabel.configure(foreground="#000000")
        self.showLabel.configure(text='''Show Title''')
        self.showLabel.configure(width=544)
        self.showLabel.configure(font=font13)

        self.Label2 = Label(top)
        self.Label2.place(relx=0.14, rely=0.75, height=21, width=514)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Estimated Title For This Song''')
        self.Label2.configure(width=514)
        self.Label2.configure(font=font10)






if __name__ == '__main__':
    vp_start_gui()



