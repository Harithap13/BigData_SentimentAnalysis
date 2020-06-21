# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:17:52 2020

@author: admin
"""

from tkinter import *
import tkinter.messagebox
import nltk
import pandas
import csv
import re
import string

nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
list_comments=[]
class analysis_text():
        # Main function in program
    def center(self, toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

    def callback(self):
        if tkinter.messagebox.askokcancel("Quit", "Do you really wish to quit?"):
            self.main.destroy()

    def setResult(self, type, res):
        if (type == "neg"):
            self.negativeLabel.configure(text = "Negative : " + str(res) + " % \n")
        if (type == "neu"):
            self.neutralLabel.configure( text = "Neutral : " + str(res) + " % \n")
        if (type == "pos"):
            self.positiveLabel.configure(text = "Posetive : " + str(res) + " % \n")

    def runAnalysis(self):
        sentences = []
        sentences.append(self.line.get())
        sid = SentimentIntensityAnalyzer()
        dataframe ={}
        for sentence in sentences:
            dataframe["Comment"] = sentence
            ss = sid.polarity_scores(sentence)
            for k in sorted(ss):
                self.setResult(k, ss[k])
                if (k == "neg"):
                    dataframe["neg"] = ss[k]
                if (k == "neu"):
                    dataframe["neu"] = ss[k]
                if (k == "pos"):
                    dataframe["pos"] = ss[k]
                print()
        list_comments.append(dataframe)
        print()

    def editedText(self, event):
        self.typedText.configure(text = self.line.get() + event.char)

    def runByEnter(self, event):
        self.runAnalysis()

    def __init__(self):
        self.main = Tk()
        self.main.title("Sentiment Analyzer")
        self.main.geometry("700x400")
        self.main.resizable(width=True, height=True)
        self.main.protocol("WM_DELETE_WINDOW", self.callback)
        self.main.focus()
        self.center(self.main)

        self.label1 = Label(text = "Add a comment:")
        self.label1.pack()

        self.line = Entry(self.main, width=70)
        self.line.pack()

        self.textLabel = Label(text = "\nYour comment as posted:", font=("Helvetica", 15))
        self.textLabel.pack()
        self.typedText = Label(text = "", fg = "green", font=("Helvetica", 20))
        self.typedText.pack()

        self.line.bind("<Key>",self.editedText)
        self.line.bind("<Return>",self.runByEnter)


        self.result = Label(text = "Sentiment analysis on your comment:", font=("Helvetica", 15))
        self.result.pack()
        self.negativeLabel = Label(text = "", font=("Helvetica", 20))
        self.negativeLabel.pack()
        self.neutralLabel  = Label(text = "", font=("Helvetica", 20))
        self.neutralLabel.pack()
        self.positiveLabel = Label(text = "", font=("Helvetica", 20))
        self.positiveLabel.pack()
        # Run program

myanalysis = analysis_text()
mainloop()

df = pandas.DataFrame(list_comments)
df.to_csv("Sentiments2.csv")

print(list_comments)
