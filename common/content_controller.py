from parkstargram.settings import MEDIA_ROOT, MEDIA_DEFAULT_IMAGE
from config.path_cfg import BackGroundRandomImage
from uuid import uuid4
import os


class ImageController:
    def image_convert(file, media_path):
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, media_path, uuid_name)

        with open(save_path, 'wb+') as upload:
            for chunk in file.chunks():
                upload.write(chunk)
        return os.path.join(media_path, uuid_name)
    

    def feed_default_random_image_select(media_path):
        default_image_path = os.listdir(os.path.join(MEDIA_ROOT, BackGroundRandomImage))
        import random
        selected_image = os.path.join(media_path, default_image_path[random.randint(0,len(default_image_path)-1)])
        return selected_image
    
    def image_remove(remove_image, media_path):
        except_list = [os.path.join(media_path, default_image) for default_image in MEDIA_DEFAULT_IMAGE]
        if remove_image not in except_list:
            os.remove(os.path.join(MEDIA_ROOT, remove_image))