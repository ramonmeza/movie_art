import os

import cv2
import numpy as np

from movie_art.config import Config
from movie_art.generators import generate

TEST_CONFIG: Config = Config(
    'test_video.mp4',
    'test_output.jpg',
    512,
    128
)


def generate_test_video():
    '''
    Generates a video with 512 frames at 24 FPS that linearly fades from black
    to white. Resulting image should be a gradient once processed.
    '''
    # video properties
    width, height = 640, 480
    fps = 24
    frame_count = 512

    # create video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')    # pylint: disable=no-member
    out = cv2.VideoWriter(TEST_CONFIG.input, fourcc, fps, (width, height), isColor=False) # pylint: disable=no-member

    for frame_number in range(frame_count):
        grayscale_value = int((255 * frame_number) / frame_count)
        frame = np.full((height, width), grayscale_value, dtype=np.uint8)
        out.write(frame)
        print(f"Frame {frame_number + 1}/{frame_count}", end='\r')

    out.release()


def test_generate():
    # generate test video and process it
    generate_test_video()
    result = generate(
        TEST_CONFIG.input,
        TEST_CONFIG.output,
        TEST_CONFIG.width,
        TEST_CONFIG.height
    )

    # ensure function returns successfully
    assert result == 0, 'Failed to generate image'

    # delete test artifacts
    # os.remove(TEST_CONFIG.input)
    # os.remove(TEST_CONFIG.output)
