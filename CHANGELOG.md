# Changelog

All notable changes to the Text-Based RPG Game project.

## [1.1.0] - 2025-08-27
### Removed
- Removed 'examine' command and related functionality
- Removed examine methods from item classes
- Cleaned up related documentation and help text

### Fixed
- Fixed indentation issues in game.py
- Resolved merge conflicts from recent updates
- Improved code consistency and formatting

## [1.0.0] - 2025-07-30
### Added
- Core game classes:
  - `StationItem` - Base class for all in-game items
  - `DiagnosticTool` - Item for repairing droids
  - `EnergyCrystal` - Key mission item
  - `Location` - Manages game locations and their properties
  - `DamagedMaintenanceDroid` - Interactive NPC that blocks progress
  - `Player` - Tracks player state and inventory
  - `GameController` - Manages game flow and logic

### Features
- Two main locations: Maintenance Tunnels and Docking Bay
- Interactive items that can be picked up and used
- Point-based scoring system
- Hazard counter for incorrect actions
- Win condition detection

## [0.1.0] - 2025-07-29
### Added
- Initial project structure
- Basic command-line interface
- Placeholder classes for game objects
- Basic movement system between locations
