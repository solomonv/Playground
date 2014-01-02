__author__ = 'Sol'
from melopy import Melopy
from random import *
m = Melopy("testSong13", 20, 120)

# c major
#melodyNotes = 'CDEFGA'
#bassNotes = 'CFGA'

#other
# melodyNotes = 'CDEFGA'
# bassNotes = 'GAE'

melodyNotes = 'CDEAG'
bassNotes = 'CDEFG'
#range of even numbered notes available to choose per bar
#bar = randrange(16,32,2)
bar = 8

#melody = []
#bassMelody = []
#print "\n"+str(bar)

#chooses random note for the number of beats in the bar
#for i in range(bar):
    #melody += choice(melodyNotes)

##chooses random note for half of the number of beats in the bar
#for i in range(bar/2):
    #bassMelody += choice(bassNotes)

#formatted string to be parsed by melopy
#formatted = ''.join(melody) + "&&&" + '3' + '[' + "".join(bassMelody) + ']'

formatted = ''

def melodyMaker():
    global formatted, bar
    formatted += "" + "5"
    for i in range(bar):
        rander = randrange(0,8)

        if rander == 5:
            formatted += "(" + choice(melodyNotes) + choice(melodyNotes) + ")"

        elif rander == 7:
                formatted += "((" + choice(melodyNotes) + choice(melodyNotes) + choice(melodyNotes) + choice(melodyNotes) + "))"

        else:
            formatted += choice(melodyNotes)

def bassMaker():
    global formatted, bar, bassNotes
    formatted += '3' + '['
    rander = randrange(0,8)
    for i in range(bar/2):
        print rander
        if rander > 3:
            formatted += choice(bassNotes)
        else:
            formatted += "(" + choice(bassNotes) + choice(bassNotes) + ")"
    formatted += ']'

def blankBar():
    global formatted, bar
    for i in range(bar/2):
        formatted += "[_]"

melodyMaker()
melodyMaker()
melodyMaker()
melodyMaker()
melodyMaker()
melodyMaker()
melodyMaker()
melodyMaker()
#
formatted +="&&&"
#
#blankBar()
bassMaker()
bassMaker()
bassMaker()
bassMaker()
bassMaker()
bassMaker()
bassMaker()
bassMaker()
#############################


print "note list:  " + formatted

#string to be parsed by melopy
m.parse(formatted)

#renders .wav file set as Melopy init
m.render()
