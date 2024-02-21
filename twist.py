"""
From Genius_um. Under the name of MazeGroup (https://mazegroup.org/)
2024
"""

import requests
import sys
import time

class TwistAPI():
    def __init__(self):
        self.api_url = "https://twist.mazegroup.org/api/"
    
    def p_getUserInfo(self):
        return "get_user_info.php"
    
    def p_getPostInfo(self):
        return "get_post_info.php"
    
    def p_getInsightInfo(self):
        return "get_insight_info.php"
    
    def p_getUsersList(self):
        return "get_users_list.php"
    
    def p_getPostsList(self):
        return "get_posts_list.php"
    
    def p_getInsightsList(self):
        return "get_insights_list.php"

    def getParsedUrl(self, page:str, args:dict={}):
        args_text = ""
        page = page.replace(".php", "")
        if len(args):
            args_text = "?"
            for param, value in args.items():
                args_text += f"{param}={value}&"
        args_text = args_text[:-1]
        return f"{self.api_url}{page}.php{args_text}"
    
    def request(self, url:str):
        response = requests.get(url)

        if response.status_code == 200:
            text = response.text
            text = text.replace("\r", "\n")
            text = text.replace("\n", "")
            return dict(eval(text))
        else:
            sys.exit('The request was failed with code error ' + str(response.status_code))
    
    def getUserInfo(self, id:int): # For later : , picture:bool=False):
        start_time = time.time()
        #picture = int(picture)
        response = self.request(self.getParsedUrl(self.p_getUserInfo(), {
            "id": id,
            "picture": 0 #picture
        }))
        end_time = time.time()
        request_info = {
            "time": round(end_time - start_time, 6)
        }
        return response, request_info
    
    def getPostInfo(self, id:int):
        start_time = time.time()
        response = self.request(self.getParsedUrl(self.p_getPostInfo(), {
            "id": id
        }))
        end_time = time.time()
        request_info = {
            "time": round(end_time - start_time, 6)
        }
        return response, request_info
    
    def getInsightInfo(self, id:int):
        start_time = time.time()
        response = self.request(self.getParsedUrl(self.p_getInsightInfo(), {
            "id": id
        }))
        end_time = time.time()
        request_info = {
            "time": round(end_time - start_time, 6)
        }
        return response, request_info
    
    def getUsersList(self):
        start_time = time.time()
        response = self.request(self.getParsedUrl(self.p_getUsersList(), {
            "id": id
        }))
        end_time = time.time()
        request_info = {
            "time": round(end_time - start_time, 6)
        }
        return response, request_info
    
    def getPostsList(self):
        start_time = time.time()
        response = self.request(self.getParsedUrl(self.p_getPostsList(), {
            "id": id
        }))
        end_time = time.time()
        request_info = {
            "time": round(end_time - start_time, 6)
        }
        return response, request_info
    
    def getInsightsList(self):
        start_time = time.time()
        response = self.request(self.getParsedUrl(self.p_getInsightsList(), {
            "id": id
        }))
        end_time = time.time()
        request_info = {
            "time": round(end_time - start_time, 6)
        }
        return response, request_info