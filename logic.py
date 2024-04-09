import os
import numpy as np
from PIL import Image


# Grayscale Image Creation 
def createGrayImage(input_file, output_dir, imgFormat='png', imageSize=128, resampling_filter='BICUBIC'):
    """Creates a gray-level image from file and saves the image in specified folder"""
    try:
        with open(input_file, 'rb') as file:
            file_content = file.read()
            data = np.frombuffer(file_content, dtype=np.uint8)
            image_size = int(np.ceil(np.sqrt(len(data))))
            data = np.pad(data, (0, image_size**2 - len(data)), 'constant')
            data = data.reshape((image_size, image_size))
            image = Image.fromarray(data, 'L')
            resized_image = image.resize((imageSize, imageSize), getattr(Image, resampling_filter.upper()))
            
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            output_file_path = os.path.join(output_dir, os.path.splitext(os.path.basename(input_file))[0] + "." +imgFormat)
            resized_image.save(output_file_path)

            return output_file_path

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Coloured Image Creation
def createColorImage(input_file, output_dir, imgFormat='png', imageSize=128, resampling_filter='BICUBIC'):
    """Creates a coloured image from file and saves the images in specified folder"""
    try:
        with open(input_file, 'rb') as file:
            file_content = file.read()
            data = np.frombuffer(file_content, dtype=np.uint8)
            image_size = int(np.ceil(np.sqrt(len(data) / 3)))
            data = np.pad(data, (0, image_size**2 * 3 - len(data)), 'constant')
            data = data.reshape((image_size, image_size, 3))
            image = Image.fromarray(data, 'RGB')
            resized_image = image.resize((imageSize, imageSize), getattr(Image, resampling_filter.upper()))
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            output_file_path = os.path.join(output_dir, os.path.splitext(os.path.basename(input_file))[0] + "." + imgFormat)
            resized_image.save(output_file_path)

            return output_file_path

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def list_files(root_folder):
    """ Recursively list all files in a directory and its subdirectories."""
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            file_path = os.path.join(root, file)
            yield file_path
        

# Convert the files into images
def convert_files(payload):
    """It takes a list of input files, creates images, and returns the file path"""
    input_dir = payload['input_dir']
    output_dir = payload['output_dir']
    mode = payload['mode']
    imgFormat = payload['imgFormat']
    imageSize = payload['imageSize']
    resampling_filter = payload['resampling_filter']
    
    print("Started...")
    
    try:
        for file_path in list_files(input_dir):
            if (mode == 'grayscale'):
                resultant_image = createGrayImage(file_path, output_dir, imgFormat, imageSize, resampling_filter)
            elif (mode == 'color'):
                resultant_image = createColorImage(file_path, output_dir, imgFormat, imageSize, resampling_filter)

            if resultant_image is None:
                print(f"Error creating image for {file_path}")

        print("Conversion Completed Successfully!!")
        return 
            
    except Exception as e:
        print(f"An error occurred: {e}")

