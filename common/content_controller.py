from parkstargram.settings import MEDIA_ROOT
from config.path_cfg import BackGroundImageFiles
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
        import random
        selected_image = os.path.join(media_path, BackGroundImageFiles[random.randint(0,len(BackGroundImageFiles)-1)])
        return selected_image
    
    def image_remove(remove_image, media_path):
        except_list = [os.path.join(media_path, default_image) for default_image in BackGroundImageFiles]
        if remove_image not in except_list:
            os.remove(os.path.join(MEDIA_ROOT, remove_image))