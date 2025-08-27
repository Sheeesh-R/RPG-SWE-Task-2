# Space Station Emergency

A text-based adventure game where you must navigate a failing space station, solve puzzles, and restore power before it's too late!

## 🚀 Features

- **Immersive Text-Based Adventure**: Navigate through the space station using simple text commands
- **Multiple Locations**: Explore different areas of the station, each with unique descriptions and challenges
- **Interactive Items**: Find and use items to solve puzzles and progress through the game
- **Scoring System**: Earn points for successful actions and completing objectives
- **Hazard System**: Be careful! Incorrect actions will increase your hazard count

## 🎮 How to Play

### Commands
- `move <direction>` - Move to an adjacent location (e.g., 'move east')
- `pick up <item>` - Pick up an item (e.g., 'pick up tool')
- `use tool` - Use the diagnostic tool on the maintenance droid
- `status` - View your current status and inventory
- `win` - Attempt to complete the mission (must be in Docking Bay with crystal)
- `help` - Show available commands
- `quit` - Exit the game

### Game Objective
Your mission is to restore power to the space station by finding the energy crystal and bringing it to the Docking Bay. But beware - the maintenance droid is damaged and blocking your path!

## 🛠️ Installation

1. Make sure you have Python 3.8 or higher installed
2. Clone this repository:
   ```bash
   git clone https://github.com/Sheeesh-R/RPG-SWE-Task-2.git
   cd RPG-SWE-Task-2
   ```
3. Run the game:
   ```bash
   python main.py
   ```

## 📁 Project Structure

- `main.py` - Entry point of the application
- `game.py` - Main game controller and logic
- `player.py` - Player class and inventory management
- `location.py` - Location and map management
- `items.py` - Item definitions and interactions
- `droid.py` - Maintenance droid NPC implementation


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🙏 Acknowledgements

- Created as part of a software engineering task
- Inspired by classic text adventure games
