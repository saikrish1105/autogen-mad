# autogen-mad

A simple experiment with multi-agent interactions using [Autogen](https://github.com/microsoft/autogen), based on the tutorial ["Multi-Agent Interactions with Autogen and Gemini - Part 8: Group Chat"](https://medium.com/google-cloud/tutorial-multi-agent-interactions-with-autogen-and-gemini-part-8-group-chat-511440860129).

## Features
- Multiple agents with different roles.
- Basic group chat interactions.
- Human feedback support via proxy agent.
- Example scripts for jokes, exam checking, and more.

## Installation
```bash
git clone https://github.com/saikrish1105/autogen-mad.git
cd autogen-mad
pip install -r requirements.txt
```

## Usage
Run the main script:
```bash
python main.py
```

Or run individual agents:
```bash
python joke_write.py
python exam_checker.py
python human_feedback.py
```

## Project Structure
```
autogen-mad/
├── main.py              # Entry point
├── joke_write.py        # Joke generator agent
├── exam_checker.py      # Exam checking agent
├── human_feedback.py    # Human feedback agent
├── model_config.json    # LLM configuration
├── requirements.txt     # Dependencies
└── README.md
```

## Acknowledgements
- Inspired by the tutorial by Romin Irani on Medium.
- Built with Autogen + Gemini models.
