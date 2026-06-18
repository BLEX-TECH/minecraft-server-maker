# Minecraft Server Maker

A professional GUI-based tool for hosting and managing Minecraft servers on your local device. Inspired by Squid Servers, this tool provides an intuitive interface for server configuration, management, and monitoring.

## Features

- 🎨 **Modern GUI Interface** - Clean, user-friendly dashboard
- ⚙️ **Server Configuration** - Easy settings management
- 📊 **Real-time Monitoring** - Track server performance and players
- 🔧 **Server Control** - Start, stop, restart servers
- 👥 **Player Management** - View and manage connected players
- 💾 **Backup Management** - Automated backups
- 🌐 **Network Configuration** - Port and connection settings
- 📝 **Logs Viewer** - Real-time server logs

## Requirements

- Python 3.9+
- Java 17+ (for Minecraft Server)
- 2GB RAM minimum
- 5GB storage minimum

## Installation

```bash
git clone https://github.com/BLEX-TECH/minecraft-server-maker.git
cd minecraft-server-maker
pip install -r requirements.txt
python main.py
```

## Usage

Run the application:

```bash
python main.py
```

The GUI will open, allowing you to:
1. Configure server settings
2. Start/stop the server
3. Monitor performance
4. Manage players and world

## Directory Structure

```
├── main.py
├── requirements.txt
├── src/
│   ├── gui/
│   │   ├── main_window.py
│   │   ├── settings_panel.py
│   │   ├── dashboard.py
│   │   └── styles.py
│   ├── server/
│   │   ├── server_manager.py
│   │   ├── server_process.py
│   │   └── config.py
│   └── utils/
│       ├── logger.py
│       ├── backup.py
│       └── system_monitor.py
└── assets/
    └── icons/
```

## License

MIT License
