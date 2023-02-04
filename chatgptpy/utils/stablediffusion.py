
import time
import os
from time import sleep
import random

def dictionary_of_image_paths():
    """
    Return a dictionary with the names of the folders as keys and the list of image file paths as values.
    :param image_folder_path: (string) folder path that contains the sub-folders of images
    :return: (dictionary) dictionary with the names of the folders as keys and the list of image file paths as values
    """
    folder_names = ['Angry', 'Unfriendly', 'Terrified', 'Cheerful', 'Sad', 'Excited', 'Chat']
    image_folder_path = '/Users/bread/Documents/anime-chatgptchan 2/chatgptpy/anime_expressions'

    image_paths = {}

    for folder in folder_names:
        folder_path = os.path.join(image_folder_path, folder)
        images = [os.path.join(folder_path, image) for image in os.listdir(folder_path)]
        image_paths[folder] = images

    return image_paths

def get_random_image(image_list):
    """
    Return a random image file path from the list of image file paths.
    :param image_list: (list) list of image file paths
    :return: (string) a random image file path
    """
    return random.choice(image_list)