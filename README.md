# ☁️ Word Cloud Generator

A simple Python tool that turns any text file into a word cloud image. Common words like "the", "and", and "is" are removed automatically, so the most meaningful words stand out.

## Features

- Reads any `.txt` file
- Removes English stop words automatically
- Saves the word cloud as a PNG image
- Displays the result on screen
- Custom output filename through a command-line option

## Requirements

- Python 3.8 or higher
- [wordcloud](https://pypi.org/project/wordcloud/)
- [matplotlib](https://pypi.org/project/matplotlib/)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/word-cloud-generator.git
cd word-cloud-generator
```

2. Install the dependencies:

```bash
pip install wordcloud matplotlib
```

## Usage

1. Put your text in a file, for example `speech.txt`.
2. Run the script:

```bash
python wordcloud_generator.py speech.txt
```

3. A window shows the word cloud, and the image is saved as `wordcloud.png`.

### Custom output name

```bash
python wordcloud_generator.py speech.txt -o my_cloud.png
```

## How It Works

1. Reads the text file.
2. Removes stop words using the built-in `STOPWORDS` list.
3. Counts word frequencies. More frequent words appear larger.
4. Draws the word cloud, saves it as a PNG, and displays it with matplotlib.

## Customization

- Change `background_color` (e.g. `"black"`) or `colormap` (e.g. `"viridis"`) inside `WordCloud(...)`.
- Add your own stop words: `STOPWORDS.update({"said", "also"})`.
- Change `max_words` to show more or fewer words.
- Use a mask image to shape the cloud (a heart, a logo, etc.).

## Project Structure

```
.
├── wordcloud_generator.py
├── README.md
└── speech.txt
```

## Contributing

Contributions are welcome. Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
