import random
class leage:
    def __init__(self,list_club):
        self.list_club=list_club
        
    def Premier_League(self):
        random_list=random.sample(self.list_club,10)    
        number=0
        for i in random_list:
           number+=1
           print(f'{number}-{i}')
     
premier_league_teams = ["Manchester City","Liverpool","Arsenal","Manchester United",
"Chelsea","Tottenham Hotspur"
,"Newcastle United","Aston Villa",
"Brighton & Hove Albion",
"West Ham United"]
             
leage_1=leage(premier_league_teams) 
print(leage_1.Premier_League())
    