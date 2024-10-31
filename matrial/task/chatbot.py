import random
class bot:
    def __init__(self,responses):
        self.responses=responses
        
        
     
    def get_response(self,user_input):
       for key in self.responses:
          if key in user_input:
              return random.choice(self.responses[key])
    
       return random.choice(self.responses["default"])

    def chatbot(self):
        print("Chatbot: Hi! How can I assist you today?")
    
        while True:
          user_input = input("User: ").lower()
          self.response = self.get_response(user_input)
          print("Chatbot:", self.response)
        
          if user_input == "goodbye":
            break
        
responses = {
"hello": ["Hello!", "Hi there!", "Greetings!"],
"how are you": ["I'm doing well, thank you!", "I'm fine, how about you?"],
"goodbye": ["Goodbye!", "See you later!", "Farewell!"],
"default": ["I'm sorry, I didn't understand.", "Could you please rephrase that?"] }

c1=bot(responses)
c1.chatbot()

