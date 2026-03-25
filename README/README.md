# 🤖 Telegram Multi-Function Bot

A multifunctional Telegram bot written in Python with support for image generation, ASCII art conversion, jokes, and animal APIs.

---

## 🚀 Features

- 🔁 Reverse text
- 🖼 Generate images from text (AI)
- 🐱 Get random cat images
- 🐶 Get random dog images
- 😂 Generate jokes
- 🔤 Convert images to ASCII art
- 📊 User info lookup

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
````

### 2. Install dependencies

```bash
pip install pyTelegramBotAPI pillow requests fal-client
```

---

## 🔑 Configuration

Open `TG_BOT.py` and replace:

```python
bot = telebot.TeleBot('TG_BOT')
```

with your Telegram bot token.

Also set your API key:

```python
os.environ['FAL_KEY'] = "YOUR_FAL_KEY"
```

---

## ▶️ Run

```bash
python TG_BOT.py
```

---

## 📜 Commands

### 🔹 Basic

| Command     | Description                |
| ----------- | -------------------------- |
| `/start`    | Greeting                   |
| `/rev text` | Reverse input text         |
| `/gen text` | Generate image from prompt |
| `/info`     | Show help                  |

---

### 🔹 API Commands

| Command   | Description          |
| --------- | -------------------- |
| `/cat`    | Random cat image     |
| `/cat N`  | N cat images         |
| `/dog`    | Random dog image     |
| `/dog N`  | N dog images         |
| `/joke N` | Get joke by category |

#### Joke categories:

```
1 - Jokes
2 - Stories
3 - Poems
4 - Aphorisms
5 - Quotes
6 - Toasts
8 - Statuses
```

---

### 🔹 Fun

| Command | Description                                  |
| ------- | -------------------------------------------- |
| `/lol`  | Infinite random text spam (use carefully ⚠️) |

---

### 🔹 Image Processing

Send any photo to the bot and it will:

* process the image
* convert it to ASCII art
* send it back

---

### 🔹 User Info

Send one of the following messages:

```
id
is_bot
first_name
last_name
username
is_premium
```

---

## 🧠 Project Structure

```
.
├── TG_BOT.py   # Main bot logic
├── api.py      # API handlers (cats, dogs, jokes)
└── img/        # Saved images
```

---

## ⚠️ Notes

* `/lol` runs an infinite loop and may spam the chat
* Telegram message limit is 4096 characters (handled in ASCII conversion)
* Image generation requires a valid API key

---

## 🛠 Tech Stack

* Python
* pyTelegramBotAPI
* Pillow (PIL)
* requests
* fal.ai API

---

## 📄 License

Free for personal and educational use.

---

## 💡 Ideas for Improvement

* Add inline buttons
* Implement anti-spam protection for `/lol`
* Add logging
* Docker support
* Switch to webhooks instead of polling
