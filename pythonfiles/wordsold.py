import os

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
notes = ['a', 'bes', 'b', 'c', 'des', 'd', 'ees', 'e', 'f', 'fis', 'g', 'gis']
translatedText = ""
lilyPondText = """\version "2.16.0"  % necessary for upgrading to future LilyPond versions.

\header{
  title = "Your Text Translated"
  subtitle = 
}

\c' {"""
#======================

#for letter, val in enumerate(alpha):

#Translates letter into notes
def translateLetterToNote(letter):
	letterIndex = ord(letter) - ord('a')
	letter = letterIndex

	numberOfNotes = len(notes)
	octave = letter / numberOfNotes
	note = letter - (numberOfNotes * octave) 
	note = notes[note]
	if octave == 1:
		note += "'"
	elif octave == 2:
		note += str("''")
	return note

# Takes text and runs it through translateLetterToNote to output notes for lilypond
def textToNote(text):
	global translatedText
#text = raw_input("Type a sentence to translate: ").lower()
	for letter in text.replace(" ", ""):		
		translatedText += translateLetterToNote(letter)
		translatedText += " "
	print translatedText
	
def writeToFile(file):
	writeFile = open("Output.ly", "w")
	writeFile.write(lilyPondText)
	writeFile.write(file)
	writeFile.write("}")
	writeFile.close()
	
#================

textToNote(raw_input("text to translate: ").lower())
writeToFile(translatedText)

lily = "C:\Users\Solomon\Documents\pythonfiles\Output.ly"
os.startfile(lily)



