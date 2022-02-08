class Game():

	def __init__(self,word):

		self.chosenWord= word
		self.gameWon = False

	def SetWord(self,newWord):
		self.chosenWord = newWord


	def ValidateGuess(self,guess):
		r = []
	
		for it in range(0,len(guess)):
			
			if guess[it] == self.chosenWord[it]:
				r.append('Green')
			elif guess[it] in self.chosenWord:
				r.append('Yellow')
			else:
				r.append('Grey')
		return r


	def TakeGuess(self,numberOfGuesses):
		guess = input('Enter Guess (5 characters) :')
		guess = guess[:5].lower()
		print(guess)
		reply = self.ValidateGuess(guess)
		print(reply)
		if reply == ['Green','Green','Green','Green','Green']:
			self.gameWon = True

		else:
			numberOfGuesses = numberOfGuesses - 1
		return numberOfGuesses

	def Main(self):
		numberOfGuesses=6
		while numberOfGuesses > 0 and self.gameWon == False : 
			numberOfGuesses = self.TakeGuess(numberOfGuesses)
		if self.gameWon:
			print('You Won!')
		else:
			print('You ran out of Guesses!')
			print('The word was: '+self.chosenWord)

g = Game('hello')
g.Main()
