from parkstargram.settings import MEDIA_ROOT, STATIC_URL
from uuid import uuid4
import os

from config.path_cfg import BackGroundImageFolder, BackGroundImageFiles


class ImageController:
    def image_convert(file, media_path):
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, media_path, uuid_name)

        with open(save_path, 'wb+') as upload:
            for chunk in file.chunks():
                upload.write(chunk)
        return os.path.join(media_path, uuid_name)
    

    def feed_default_random_image_select():
        from django.core.files.uploadedfile import InMemoryUploadedFile
        from io import BytesIO
        import random
        import sys
        from PIL import Image
        
        selected_image = os.path.join(STATIC_URL, BackGroundImageFolder, 
                                      BackGroundImageFiles[random.randint(0,len(BackGroundImageFiles)-1)])
        selected_image_file = Image.open(selected_image)
        
        output_buffer = BytesIO()
        selected_image_file.save(output_buffer, format='JPEG')
        output_buffer.seek(0)
        
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, BackGroundImageFolder, uuid_name)
        # InMemoryUploadedFile 객체 생성
        processed_image = InMemoryUploadedFile(
            output_buffer,
            'ImageField',  # 필드명
            "%s.jpg" % uuid_name,  # 파일명
            'image/jpeg',  # MIME 타입
            sys.getsizeof(output_buffer),
            None
        )
        
        with open(save_path, 'wb+') as upload:
            for chunk in processed_image.chunks():
                upload.write(chunk)
        return os.path.join(BackGroundImageFolder, uuid_name)
    
    def image_remove(remove_image):
        if os.path.isfile(os.path.join(MEDIA_ROOT, remove_image)):
            os.remove(os.path.join(MEDIA_ROOT, remove_image))