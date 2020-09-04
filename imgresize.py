"""
imgresize.py 

image resizer that resizes images in a specified folder ...
"""
import os
import glob
from PIL import Image 


class Resizer:
    def __init__(self):
        self.standard_size = [1280, 144]
        self.folder = input("Select input folder: ").strip()
        self.find_image_files()
        print("Found", len(self.files), "in folder", self.folder, ", processing...")
        self.process_files()

    def find_image_files(self):
        files = sorted(glob.glob(os.path.join(self.folder, "*.jpg")))
        files = [filename for filename in files 
           if not filename.endswith('resize.jpg')]
        self.files = files

    def process_files(self):
        for filename in self.files:
            self.process_file(filename)

    def process_file(self, filename):
        img = Image.open(filename)
        width_factor = img.width / self.standard_size[0]
        height_factor = img.height / self.standard_size[1]
        scale = None
        if width_factor > height_factor:
            if height_factor < 1:
                scale = 1 / height_factor
        else:
            if width_factor < 1:
                scale = 1 / width_factor
        if scale is None:
            return

        new_size = [int(scale * img.width) + 1, int(scale * img.height) + 1]

        img = img.resize(new_size)
        img.save("{}_resize.jpg".format(filename))

if __name__ == "__main__":
    Resizer()

     
