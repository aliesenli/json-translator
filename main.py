import os
import re
import sys
import json
import errno
import codecs
import argparse

from deep_translator import GoogleTranslator

translated_elements = {}
ignored_expressions = []
detect_pattern, restore_pattern = re.compile(r"{{\s*(\w+).(\w+)\s*}}"), re.compile(r'_(\d+)_')


def detect(match_object) -> str:
    ignored_expressions.append(match_object.group())
    return '_%d_' % (len(ignored_expressions) - 1)


def restore(match_object) -> str:
    return ignored_expressions[int(match_object.group(1))]


def translate(translation_client, source_file, destination_file) -> None:
    try:
        with open(source_file, encoding='utf-8') as source:
            data = json.load(source)

        for count, key in enumerate(data):
            original_text = detect_pattern.sub(detect, data[key])
            translated_text = translation_client.translate(original_text)
            translated_text = restore_pattern.sub(restore, translated_text)
            translated_elements[key] = translated_text
            print(f'{count + 1}: {data[key]:<35} -> {translated_text}')

        with codecs.open(destination_file, 'w', 'utf-8') as destination:
            json.dump(translated_elements, destination, indent=3, ensure_ascii=False)
    except KeyboardInterrupt:
        sys.exit(os.strerror(errno.ECANCELED))


def main():
    parser = argparse.ArgumentParser(description='Translate JSON file to another language.')
    parser.add_argument('-s', help='Path to the source file', required=True)
    parser.add_argument('-d', help='Path to the destination file', required=True)
    parser.add_argument('-l', help='Target Language to be translated into. Allowed values are: ' + ', '.join(
        GoogleTranslator().get_supported_languages()), choices=GoogleTranslator().get_supported_languages(),
                        metavar='', type=str.lower, required=True)
    args = parser.parse_args()

    source_file = args.s
    destination_file = args.d
    target_language = args.l

    if os.path.exists(source_file):
        if not destination_file.endswith('.json'):
            destination_file += '.json'

        translation_client = GoogleTranslator(source='auto', target=target_language)
        translate(translation_client, source_file, destination_file)
    else:
        sys.exit(FileNotFoundError(os.strerror(errno.ENOENT), source_file))


if __name__ == '__main__':
    main()
