# Pervonah Telegram

This repository contains a Pervonah to telegram implemented using the `pyrogram` library. The bot listens for messages in specific Telegram channels and replies with predefined comments.

## Prerequisites

Before running the code, ensure you have the following installed:

- Python 3.6+
- `pyrogram` library
- `tgcrypto` library
- `python-dotenv` library

Install command:

```bash
pip install -r requirements.txt
```

## Configuration

The code requires some configuration variables, which are stored in a `.env` file. Create a `.env` file in the root directory of the project with the following content:

```
App_api_id=your_api_id
App_api_hash=your_api_hash
My_number=your_phone_number
```

Replace `your_api_id`, `your_api_hash`, and `your_phone_number` with your actual Telegram API ID, API hash, and phone number.
Use https://my.telegram.org/ to get them.

## Channels and Comments

These are configured in the `config.py` file:

```python
channels = {
    'durov': 'comment_1',
    'your_channel': 'comment_2',
    # Add more channels and comments as needed
}
```

## Running the Code

To run the code, execute the `main.py` script:

```bash
python main.py
```
This code will post comments on behalf of your account, no other natros are required