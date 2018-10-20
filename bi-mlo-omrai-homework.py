#!/usr/bin/python3
#Omrai David, 15.10.2018
import os, copy, sys
class formulaClass():
    def __init__(self, formula):
        # Nasledujici radek do programu zadava formuli, kterou vyhodnoti
        # Je potreba spravna syntaxe, tedy kazda logicka spojka musi byt v
        # uzavrenych zavorkach '()' a to stejne plati i pro formula A, B, C, D, ...
        # V pridpade negace 'n' je treba ji dat na levou stranu a k formuli nA, nB, nC, nD, ...
        # Napriklad     ((A)e(B))
        #               ((((nA)d(B))e((nC)k(nD)))e(((nA)d(B))e((nC)k(nD))))
        self.formula = "("+formula.replace("\n","")+")"#"(((nA)d(B))e((nC)k(nD)))"
        self.maxColum = 0
        self.countStates = 0
        self.hili = 0
        self.trueTable = list()
        self.outpoleOrigin = list()
        self.seedoftree = str()
        self.helpList = list()
        self.workingList = []
        self.dictList = dict()
        self.output = list()
        self.outValues = list()
        self.logicConstructors = {'e', 'i', 'n', 'd', 'k'} # zde jsou ulozeny reprezentace logickych spojek, jejich pocatecna pismena
        self.formulaControl()
        #self.structureForm()
    def formulaControl(self):
        cerberos=0
        penny=0
        numberofform=0
        saver=set()
        nomis=0
        alert=0
        decide=0
        for item in self.formula:
            if item == "(" or item == ")":
                decide+=1
            else:
                decide+=2
        if decide == len(self.formula):
            decide=1
        else:
            decide = self.structureForm()
        if decide == 0:
            self.printTree()
        print(self.outpoleOrigin)
        countalert=0
        #print(self.outpoleOrigin)
        for character in self.seedoftree:
            if character == '.' or character =='\\n' or character ==' ':
                countme=0
            else:
                countme+=1
            if countme==2:
                countalert=1
        if countalert!=1:
            for item in self.outpoleOrigin:
                if item[0]==nomis:
                    alert=1
                if item[1] not in self.logicConstructors:
                    numberofform+=1
                else:
                    saver.add(item[1])
                if item[0] == self.hili:
                    if item[1] in self.logicConstructors:
                        penny=2
                    cerberos+=1
                else:
                    pass
                nomis=item[0]
        if len(saver)==1 and numberofform>1 and 'n' in saver or alert==1 or countalert==1:
            print(self.outpoleOrigin,"Wrong input")
        elif cerberos==1 and decide == 0 and (penny==2 or len(self.formula)==3 or self.formula[1]=='n' or numberofform==1):
            #try:
            self.boardMaker()
            #except:
            #    print(self.outpoleOrigin,"Wrong input")
            #    print("Wrong input")
        else:
            print("NaLF")
    def printMe(self):
        #print("i should not be there")
        print("Tree Structure")
        print(self.seedoftree)
        print("Truth Table")
        for item in range(0, self.countStates):print(self.outValues[item],"\t", end="")
        print(self.formula.rstrip(), end="\n")
        for t in range(0, 2**self.countStates):
            for q in format(t, '0'+str(self.countStates)+'b'):print(int(q),"\t", end="")
            for i in range(0, len(self.formula)//2):print(" ", end='')
            print(self.output[t], end="\n")
    def giveMeFinal(self, what):
        for i in what:
            if i[0] == self.hili:return i[1]
            else:pass
    def boardMaker(self):
        self.setSave = set(self.logicConstructors)
        for k in self.outpoleOrigin:
            if k[1] not in self.setSave:
                self.countStates += 1
                self.setSave.add(k[1])
            else:pass
        # Building a true table
        for t in range(0, 2**self.countStates):
            for q in format(t, '0'+str(self.countStates)+'b'):
                self.helpList.append(int(q))
            self.trueTable.append(self.helpList)
            self.helpList = list()
        for states in self.trueTable:
            self.workingList = copy.deepcopy(self.outpoleOrigin)
            self.setSave = set(self.logicConstructors)
            for addbin in self.workingList:
                if addbin[1] not in self.setSave:
                    self.setSave.add(addbin[1])
                    self.outValues.append(addbin[1])
                    self.dictList[addbin[1]] = states[0]
                    addbin[1] = states[0]
                    del(states[0])
                elif addbin[1] not in self.logicConstructors:addbin[1] = self.dictList[addbin[1]]
                else: pass
            canIstop = 0
            worklevel = int(self.level)
            while canIstop == 0:
                if worklevel == 0:
                    self.output.append(self.giveMeFinal(self.workingList))
                    canIstop = 1
                else:
                    for i in range(0, len(self.workingList)):
                        if self.workingList[i][0] == worklevel and str(self.workingList[i][1]) in self.logicConstructors:
                            finder = 1
                            A, B = 3, 3
                            while B == 3:
                                if self.workingList[i+finder][0] == worklevel+1:B = self.workingList[i+finder][1]
                                else:finder+=1
                            finder = 1
                            while A == 3:
                                try:
                                    if self.workingList[i-finder][0] == worklevel+1:A = self.workingList[i-finder][1]
                                    else:finder+=1
                                except:A = 0
                            self.workingList[i][1] = self.chooseWhichOne(self.workingList[i][1], A, B)
                        else: pass
                    worklevel-=1
        self.printMe()
    def chooseWhichOne(self, what, A, B):
        if what == 'n':
            if A == 0:return 1
            else:return 0
        if what == 'k':
            if A * B == 1:return 1
            else:return 0
        if what == "d":
            if A + B == 0:return 0
            else:return 1
        if what == "i":
            if A == 1 and B == 0:return 0
            else:return 1
        if what == "e":
            if (A == 1 and B == 1) or (A== 0 and B== 0):return 1
            else:return 0
    def structureForm(self):
        self.width = os.get_terminal_size().columns
        self.colum=0
        columcheck=0
        self.outpole=[]
        for i in range(len(self.formula)):
            if self.formula[i] == "(":self.colum+=1;columcheck+=1
            elif self.formula[i] == ")":self.colum-=1;columcheck-=1
            elif self.formula[i]=="n" and self.formula[i+1]=="(":
                self.colum+=1
                self.outpole.append([self.colum,self.formula[i]])       # For tree construction
                self.outpoleOrigin.append([self.colum,self.formula[i]]) # Same as self.outpole, this one is just original and I will work with it later
            else:
                if self.maxColum < self.colum:self.maxColum = self.colum
                else: pass
                self.outpole.append([self.colum,self.formula[i]])
                self.outpoleOrigin.append([self.colum,self.formula[i]])
                if self.formula[i-1] == "n":self.colum-=1
            if self.formula[i] == "n"and self.formula[i+1]!="(":self.colum+=1
        if columcheck!=0:
            return 1
        else:
            self.emptyId = 1
            self.level = self.outpole[0][0]
            for number in self.outpole:
                if number[0] < self.level:self.level=number[0]
            self.hili = int(self.level)
            return 0
    def printTree(self):
        while self.emptyId != 0:
            self.line = ""
            self.emptyId = 0
            for k in range(len(self.outpole)):
                if self.outpole[k][0] == self.level:
                    self.line+=self.outpole[k][1]
                    self.outpole[k][0] = "."
                    self.outpole[k][1] = 2
                    self.emptyId = 1
                elif self.outpole[k][0] == '.' and self.emptyId !=0:
                    for i in range(self.outpole[k][1]):self.line+="."
                    self.outpole[k][1]+=2
                else:pass
            if self.emptyId != 0:
                self.level+=1
                self.seedoftree+=self.line.center(self.width)+"\n"
for line in sys.stdin:
    formulaClass(line)
