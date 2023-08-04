#all requests for GIT which we will use for testing
import requests

class GitHub:
     
    def get_user(self, username):
         r = requests.get(f'https://api.github.com/users/{username}')
         body = r.json()
         return body
     
    def search_repo(self, name):
        r = requests.get ("https://api.github.com/search/repositories?q=Q", params = {"q":name}) 
        body = r.json()
        return body
    
    #my_code
    
    def get_emoji(self, emo_name):
        r = requests.get("https://api.github.com/emojis")
        body = r.json()
        return body
    
    def get_body_emoji(self):
        r = requests.get("https://api.github.com/emojis")
        body = r.json()
        return body
        
    def count_by_part_of_emoji(self, part_of_name):
        emoji_dict = self.get_body_emoji()
        count = 0
        for i in emoji_dict:
            if part_of_name in i:
                count +=1
        return count
                    
           
    
    
    
