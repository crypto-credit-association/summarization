# summarization
Summarize our talks using GPT's davinci language model.

## Setup

* Create a virtual environment (e.g., ```python3 -m venv venv```)
* Start the the virtual environment (e.g., ```source venv/bin/activate```)
* ```pip install openai```
* Create an OpenAI account if you don't already have one: https://openai.com/api/
* Get an API key: https://beta.openai.com/account/api-keys
* export your key: ```export OPENAI_API_KEY=<your key>```

## Running

This script is very crude. It expects an input file called ```input.txt``` in ```cwd``` and outputs the summary to stdout. I don't do any error checking. Sorry.
