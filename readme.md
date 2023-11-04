# Chess Engine Project

## Overview
This project is an implementation of a chess engine using Python-chess and Flask. It provides a local server that allows you to play chess against an AI opponent.

## Setup

### Prerequisites
- Python 3.x
- Flask
- Python-chess
- 3-4-5 moves Syzygy table bases
- Komodo Polyglot opening book

### Installation
1. Clone the repository
```
git clone https://github.com/plewanda/chess.git
```
2. Navigate to the project directory
```
cd chess
```
3. Install the dependencies
```
pip install -r requirements.txt
```
4. Download the 3-4-5 moves Syzygy table bases and add them to `resources/tablebases/3-4-5`.
5. Download the Komodo Polyglot opening book and add `komodo.bin` file to `resources`.

## Usage 
To start the server, run the following command:
```
python app.py
```
Then, open your preferred web browser and visit `http://localhost:5000` to start playing.

## Chess Piece Images
Chess piece images are stored in the `static/img/chesspieces/wikipedia` directory. The file naming convention is `{color (b/w)}{piece type (B/K/N/P/Q/R)}`. For example, the black king piece image would be named `bK.png`.

Please ensure that you have all necessary images in the correct format and in the specified directory.

## Contributing 
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgements
- Python-chess for providing the chess logic
- Flask for providing the web server framework