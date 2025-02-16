import difflib

import pygame
import sys
import threading
import io
import signal
from flask import Flask, Response, request, jsonify

from src.line import Line
from src.train import Train
from src.resources.berlin_stations import *

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1600, 900
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FPS = 60

# Create Screen
screen = pygame.Surface((WIDTH, HEIGHT))
clock = pygame.time.Clock()


# Create trains
s2 = Line("S2", [blankenfelde, mahlow, lichtenrade, schichaueweg, buckower_chaussee, marienfelde, attilastrasse, priesterweg, suedkreuz])
s25 = Line("S25", [teltow_stadt, lichterfelde_sued, osdorfer_str, lichterfelde_ost, lankwitz, suedende, priesterweg, suedkreuz])

lines = [s2, s25]

trains = [
    Train(s2, BLUE, 5, 0, True),
    Train(s25, RED, 5, 0, False)
]


# Flask app
app = Flask(__name__)


# Game Loop
def generate_frames():
    while running:
        screen.fill(WHITE)

        # Draw lines
        for line in lines:
            line.draw(screen)
            for station in line.stations:
                station.draw(screen)

        # Update and draw trains
        for train in trains:
            train.update()
            train.draw(screen)

        img_io = io.BytesIO()
        pygame.image.save(screen, img_io, "JPEG")
        img_io.seek(0)
        frame = img_io.read()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        # clock.tick(FPS)


@app.route('/')
def index():
    return "<img src='/video_feed' style='width:100%'>"


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


def run_flask():
    app.run(host='0.0.0.0', port=5934, debug=False, use_reloader=False)


def signal_handler(sig, frame):
    global running
    print("\nShutting down...")
    running = False
    pygame.quit()
    sys.exit(0)


# Register signal handlers
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

if __name__ == "__main__":
    running = True
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    try:
        while running:
            clock.tick(FPS)
    except KeyboardInterrupt:
        signal_handler(None, None)

