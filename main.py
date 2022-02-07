import requests 
from bs4 import BeautifulSoup 
    
class DataGetter:

    def __init__(self):
        pass

    def get_images_from_kw(self, kw, num_image, classifier=None):

        