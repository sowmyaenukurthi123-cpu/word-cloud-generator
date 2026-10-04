"""Simple Word Cloud Generator

Usage:
    python wordcloud_generator.py input.txt
    python wordcloud_generator.py input.txt -o my_cloud.png
"""

import argparse

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def generate_wordcloud(text, output_file="wordcloud.png"):
    # Built-in English stop words (the, and, is, ...) are removed
    cloud = WordCloud(
        width=1000,
        height=500,
        background_color="white",
        stopwords=STOPWORDS,
        max_words=150,
    ).generate(text)

    # Save the image
    cloud.to_file(output_file)
    print(f"Saved word cloud to {output_file}")

    # Show it on screen
    plt.figure(figsize=(10, 5))
    plt.imshow(cloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="Generate a word cloud from a text file.")
    parser.add_argument("file", help="path to a .txt file")
    parser.add_argument("-o", "--output", default="wordcloud.png", help="output image name")
    args = parser.parse_args()

    with open(args.file, "r", encoding="utf-8") as f:
        text = f.read()

    if not text.strip():
        print("The file is empty.")
        return

    generate_wordcloud(text, args.output)


if __name__ == "__main__":
    main()
