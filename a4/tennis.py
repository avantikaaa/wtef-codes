p1 = 'A'
p2 = 'B'
class player:
	sets = 0
	games = 0
	score = 0
	def addscore(self, score):
		if(self.score<30):		#0, 15
			self.score+=15
		elif(self.score==30):	#30
			self.score += 10
		elif(self.score>30)	#40
			self.score+=5
			return 1
		return 0

def score(string):
	a = player()
	b = player()
	deuce = False
	for i in string:
		if(i==p1):
			k = a.addscore(a.score)
			if(k==1):
				if(a.score==b.score):
					deuce = True
				elif(a.score>b.score and deuce = True):
					a.addgames
