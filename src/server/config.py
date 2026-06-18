"""Server Configuration Defaults"""

DEFAULT_CONFIG = {
    # Basic Settings
    "server_name": "My Minecraft Server",
    "description": "A fun place to play!",
    
    # Network Settings
    "port": 25565,
    "max_players": 20,
    "online_mode": True,
    
    # Game Settings
    "gamemode": "Survival",  # Survival, Creative, Adventure, Spectator
    "difficulty": "Normal",  # Peaceful, Easy, Normal, Hard
    "pvp": True,
    "spawn_protection": 16,
    
    # Performance Settings
    "ram_gb": 2,
    "view_distance": 10,
    "simulation_distance": 10,
    
    # Features
    "enable_command_block": False,
    "enable_query": True,
    "query_port": 25565,
}

MOTD_PRESETS = [
    "Welcome to my server!",
    "A fun place to play!",
    "Let's build together!",
    "Adventure awaits!",
    "Creative freedom here!",
]

GAMEMODES = {
    "Survival": 0,
    "Creative": 1,
    "Adventure": 2,
    "Spectator": 3,
}

DIFFICULTIES = {
    "Peaceful": 0,
    "Easy": 1,
    "Normal": 2,
    "Hard": 3,
}
