#!/usr/bin/env python3

import os
import random
import re
import argparse

def read_sentences_from_file(file_path):
    """Read sentences from a text file."""
    with open(file_path, 'r') as file:
        text = file.read()
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    return [sentence.strip() for sentence in sentences if sentence.strip()]

def replace_comments_in_file(code_file_path, sentences):
    """Replace comments in a code file with random sentences."""
    with open(code_file_path, 'r') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        if '#' in line:  # Adjust this for different comment styles
            line = re.sub(r'#.*', lambda x: f'# {random.choice(sentences)}', line)
        new_lines.append(line)

    return new_lines

def main():
    parser = argparse.ArgumentParser(description="Replace comments in a code file with random sentences from a text file.")
    parser.add_argument('text_file', help="Path to the text file containing sentences.")
    parser.add_argument('code_file', help="Path to the code file to process.")
    parser.add_argument('-o', '--output-file', required=True, help="File to save the modified code.")
    args = parser.parse_args()

    sentences = read_sentences_from_file(args.text_file)
    if not sentences:
        print("No sentences found in the text file.")
        return

    if not os.path.isfile(args.code_file):
        print(f"File not found: {args.code_file}")
        return

    modified_lines = replace_comments_in_file(args.code_file, sentences)

    with open(args.output_file, 'w') as file:
        file.writelines(modified_lines)

    print(f"Processed {args.code_file} and saved to {args.output_file}.")

if __name__ == "__main__":
    main()
