# Word Cloud Generator

A small Python tool that turns any text file into a word cloud image. Common words (the, and, is...) are removed automatically, so the most meaningful words stand out.

## Requirements

- Python 3.8+
- `wordcloud`
- `matplotlib`

## Installation

```bash
pip install wordcloud matplotlib
```

## Usage

1. Save some text (a speech, article, or book chapter) in a file, e.g. `speech.txt`.
2. Run:

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
2. Removes English stop words using the built-in `STOPWORDS` list.
3. Counts word frequencies; more frequent words appear larger.
4. Draws the cloud, saves it as a PNG, and displays it with matplotlib.

## Customization Ideas

- Change `background_color` (e.g. `"black"`) or `colormap` (e.g. `"viridis"`) in `WordCloud(...)`.
- Add your own stop words: `STOPWORDS.update({"said", "also"})`.
- Change `max_words` to show more or fewer words.
- Use a mask image to shape the cloud (a heart, a logo, etc.).

## Project Structure

```
.
├── wordcloud_generator.py
├── README.md
└── speech.txt        # your input text
```

## License

Free to use and modify.
