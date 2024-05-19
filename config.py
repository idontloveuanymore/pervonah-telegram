import os 
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# https://t.me/durov -> durov
channels = {
    'durov': 'comment_1',
    'your_channel': "comment_2",
    # etc
}

App_api_id = os.getenv('App_api_id')
App_api_hash = os.getenv('App_api_hash')
My_number = os.getenv('My_number')

