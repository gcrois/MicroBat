import os

# I have no real clue what this does yet.
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-the-key'
    
