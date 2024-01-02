from parkstargram.settings import MEDIA_ROOT
from config.path_cfg import BackGroundRandomImage

from uuid import uuid4
import os

class ImageController:
    def image_convert(file):
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as upload:
            for chunk in file.chunks():
                upload.write(chunk)
        return uuid_name
    
    def feed_default_random_image_select():
        default_image_path = os.listdir(BackGroundRandomImage)
        import random
        selected_image = default_image_path[random.randint(0,len(default_image_path))]
        return selected_image
    


    