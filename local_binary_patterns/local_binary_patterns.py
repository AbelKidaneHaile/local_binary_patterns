import os
import glob2 as glob
import cv2
import numpy as np

from skimage.transform import rotate
from skimage.feature import local_binary_pattern
from skimage import data
from skimage.color import label2rgb
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import classification_report

from .chi_square_distance import *

# Absolute path to dataset folder
dataset_folder = os.path.join(os.path.dirname(__file__), '..', 'dataset')


def calculate_lbp(image): # custom implementation based on the adjacent negighbours
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Initialize the LBP image
    lbp_image = np.zeros_like(gray)
    pad_width = 1
    gray = np.pad(gray, pad_width, mode='constant', constant_values=0)
    
    # Define 8 neighbors for each pixel
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    
    # Iterate over each pixel in the image
    for i in range(1, gray.shape[0] - 1):
        for j in range(1, gray.shape[1] - 1):
            # Get the binary pattern
            binary_pattern = ''
            center_value = gray[i, j]
            for dy, dx in neighbors:
                neighbor_value = gray[i + dy, j + dx]
                binary_pattern += '1' if neighbor_value >= center_value else '0'
            
            # Convert binary pattern to decimal
            lbp_value = int(binary_pattern, 2)
            
            # Assign LBP value to corresponding pixel in LBP image
            lbp_image[i-1, j-1] = lbp_value
    
    return lbp_image


def find_minimum_distance(image_hist, train_class_path, representations):
    distances = []
    train_files_path = glob.glob(os.path.join(train_class_path, "*"))
    for train_image_path in train_files_path:

        train_image_hist = representations[train_image_path]

        distance = chi_square_distance(image_hist, train_image_hist)
        distances.append(distance)

    distances = np.array(distances)
    index_of_min = np.argmin(distances)
    file_min = train_files_path[index_of_min]
    return distances.min(), file_min


def classify_image(image_path, train_classes_path, representations, representations_val):

    image_hist = representations_val[image_path]

    minimum_distances = []
    file_mins = []

    for train_class_path in train_classes_path:
        min_distance_from_class, file_min = find_minimum_distance(image_hist, train_class_path, representations)
        minimum_distances.append(min_distance_from_class)
        file_mins.append(file_min)

    minimum_distances = np.array(minimum_distances)
    
    file_mins = np.array(file_mins) # the files that are most similar among the class members in the training set

    class_index = np.argmin(minimum_distances)

    return file_mins[class_index]


def generate_lpb_representations(train_classes_path1):
    representations = {}

    for train_class_path in train_classes_path1:
        train_files_path = glob.glob(os.path.join(train_class_path, "*"))
        for train_image_path in train_files_path: 
            # read image
            train_image = cv2.imread(train_image_path)
            # compute the LBP for the two images
            train_image_lbp = calculate_lbp(train_image).ravel()

            representations[train_image_path] = train_image_lbp

    return representations


