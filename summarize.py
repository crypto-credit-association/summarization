#!/usr/bin/env python3

import openai
import sys
import os

MAX_TOKENS = 4097
MAX_OUTPUT_TOKENS = 1400
MAX_INPUT_TOKENS = MAX_TOKENS - MAX_OUTPUT_TOKENS
INPUT_FILE = 'input.txt'

def chunk(filename):
    buffer = 20
    result = []

    # Read our input file.
    lines = open(filename).readlines()

    # Break it up into chunks with an allowable number of input tokens.
    next_result = ''
    for line in lines:
        next_result += line
        if (len(next_result) / 4)  >= (MAX_INPUT_TOKENS - buffer):
            result.append(next_result + '\n\nTl;dr\n')
            next_result = ''

    # Deal with any leftover.
    if next_result != '':
        result.append(next_result + '\n\nTl;dr\n')

    return result

if __name__ == '__main__':

    openai.api_key = os.environ['OPENAI_API_KEY']

    chunks = chunk(INPUT_FILE)
    for chunk in chunks:
        response = openai.Completion.create(model='text-davinci-003',
                                            prompt=chunk,
                                            temperature=0.7,
                                            max_tokens=MAX_OUTPUT_TOKENS,
                                            top_p=1,
                                            frequency_penalty=0,
                                            presence_penalty=0)
        print(response['choices'][0]['text'] + '\n')
