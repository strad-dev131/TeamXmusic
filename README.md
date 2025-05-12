<h1 align="center">🎵 TeamX Music Bot</h1>

<p align="center">
  <img src="https://files.catbox.moe/hxzqbf.jpg" alt="TeamX Music Logo" width="600" height="400">
</p>

<h3 align="center">Delivering Superior Music Experience to Telegram</h3>

<p align="center">
  <a href="https://t.me/TeamsXchat"><img src="https://img.shields.io/badge/Support-Group-blue?style=for-the-badge&logo=telegram"></a>
  <a href="https://t.me/TeamXUpdate"><img src="https://img.shields.io/badge/Updates-Channel-blue?style=for-the-badge&logo=telegram"></a>
  <a href="https://github.com/informasgher89745/TeamX2/blob/main/LICENSE"><img src="https://img.shields.io/github/license/informasgher89745/TeamX2?style=for-the-badge"></a>
</p>

---

## 📚 Table of Contents

- [🛠 YouTube Fix](#-youtube-fix)
- [🌟 Features](#-features)
- [🚀 Deploy on Heroku](#-deploy-on-heroku)
- [⚙️ Quick Setup](#️-quick-setup)
- [🎛 Commands](#-commands)
- [🔄 Updates & Support](#-updates--support)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 🛠 YouTube Fix

Due to YouTube blocking VPS IPs, we’ve implemented a workaround:

1. **Join the [Support Group](https://t.me/TeamsXchat)** and type `#script` to get the script.
2. **Run the script** on your Windows desktop via VS Code (or similar) to generate cookies.
3. **Fork this repository**.
4. **Paste the cookies** into the `cookies/` folder.
5. **Deploy** the bot as shown in the instructions below.

This bypass ensures smooth music playback even with YouTube restrictions.

---

## 🌟 Features

- 🎧 **Multi-Source Streaming** – Play from YouTube, Telegram, and more.
- 🎶 **Queue Support** – Add multiple tracks for seamless listening.
- 🔁 **Playback Controls** – Skip, pause, resume, repeat, and shuffle.
- 📢 **High-Quality Audio** – Crystal-clear sound output.
- ⚙️ **Custom Settings** – Equalizer, volume control, and more.

---

## 🚀 Deploy on Heroku

Click the button below to deploy the bot on Heroku instantly:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https://github.com/strad-dev131/TeamXmusic)

---

## ⚙️ Quick Setup

```bash
# Step 1: Update your system
sudo apt-get update && sudo apt-get upgrade -y

# Step 2: Install required packages
sudo apt-get install python3-pip ffmpeg -y

# Step 3: Upgrade pip
sudo pip3 install -U pip

# Step 4: Install Node.js via NVM
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
source ~/.bashrc && nvm install v18

# Step 5: Clone the repo
git clone https://github.com/informasgher89745/TeamX2 && cd TeamX2

# Step 6: Install Python requirements
pip3 install -U -r requirements.txt

# Step 7: Create your .env file
cp sample.env .env

# Step 8: Edit your environment variables
vi .env
# Press 'I' to insert, edit your values, then ':wq' to save and exit

# Step 9: (Optional) Use tmux
sudo apt install tmux -y && tmux

# Step 10: Start the bot
bash start
