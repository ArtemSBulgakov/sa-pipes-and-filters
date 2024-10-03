# Video processor

This is a Python application which takes a video file as input and processes it using defined filters.

You can change the filters by editing the `filters` list in the `main.py` file.

## Running

1. Install [Python 3.12](https://www.python.org/downloads/) or later.
2. Install [Poetry](https://python-poetry.org/) package manager.
3. Install dependencies:
   ```bash
   poetry install
   ```
4. Run the application:
   ```bash
   poetry run python3 -m src.main data/video.mp4
   ```
5. You will see the processed video frames in separate windows.
