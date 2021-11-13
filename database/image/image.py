from model import preprocess_image
from server import session
import numpy as np
import os.path

from sqlalchemy import Column, Integer, String
from database.base import Base


class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    line_width = Column(Integer)
    right_number = Column(Integer)
    image_name = Column(String)

    def __init__(self, line_width: int, right_number: int, image_name: str):
        self.line_width = line_width
        self.right_number = right_number
        self.image_name = image_name


class ImageService:
    __image_id = 1
    __images_path = './images'

    def __init__(self):
        # Getting id
        try:
            ImageService.__image_id = session.query(Image.id).order_by(Image.id.desc()).first()[0]+1
        except TypeError:
            __image_id = 1

    def __save_img_file(self, img) -> str:
        """Preprocess and save img to images directory."""
        img = preprocess_image(img)

        img_name = f"img_{ImageService.__image_id}"
        img_path = os.path.abspath(os.path.join(self.__images_path, img_name))

        np.save(img_path, img)
        return img_name

    def insert_image(self, img, line_width: int, right_number: int):
        """Insert image in database."""
        img_name = self.__save_img_file(img)

        # Create image instance
        image = Image(line_width, right_number, img_name)
        ImageService.__image_id += 1

        # Add image instance to database
        session.add(image)
        session.commit()


class ImageRepository:
    __images_path = './images'

    @staticmethod
    def get_images() -> str:
        """Getting all images."""
        table_size = session.query(Image.id).order_by(Image.id.desc()).first()[0]
        images = np.empty((table_size, 28, 28), dtype="float32")
        right_numbers = np.array([0 for x in range(table_size)])
        line_widths = np.array([0 for x in range(table_size)])

        # Getting images from database.
        response = session.query(Image).all()

        i = 0
        for row in response:
            # Add parts of dataset to total arrays.
            image = np.load(os.path.join(ImageRepository.__images_path, row.image_name+".npy"), allow_pickle=True)
            images[i] = np.array(image, copy=True)

            right_numbers[i] = row.right_number
            line_widths[i] = row.line_width
            i += 1

        # Creating total dataset.
        dataset_path = os.path.join(ImageRepository.__images_path, "dataset.npz")
        np.savez(dataset_path, images, right_numbers, line_widths)
        return dataset_path
