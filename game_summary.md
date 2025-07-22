# Text-Based RPG Game Summary

## Game Overview
A text-based RPG game where players follow a specific path to earn points. The game has two main locations: Maintenance Tunnels and Docking Bay.

## Golden Path (Required Sequence)
1. Start in Maintenance Tunnels
2. Pick up Diagnostic Tool (+10 points)
3. Repair Damaged Maintenance Droid (+20 points)
4. Move to Docking Bay
5. Pick up Energy Crystal (+50 points)
6. Type "win" to complete mission (+30 points)

## Core Classes

### 1. StationItem (Parent Class)
- Base class for items
- Attributes: _name, _description
- Methods: examine()

### 2. DiagnosticTool (inherits from StationItem)
- Used to repair droid
- Methods: examine() - gives hint about droid repair

### 3. EnergyCrystal (inherits from StationItem)
- Vital game item
- Methods: examine() - describes crystal's unstable energy

### 4. Location
- Represents game locations
- Attributes: name, description, exits, has_tool, has_crystal, droid_present
- Methods: 
  - add_exit()
  - describe()
  - remove_tool()
  - remove_crystal()
  - set_droid_present()

### 5. DamagedMaintenanceDroid
- Blocks passage until repaired
- Attributes: blocking
- Methods: repair(), is_blocking()

### 6. Player
- Tracks player state
- Attributes: current_location, has_tool, has_crystal, score, hazard_count
- Methods:
  - move()
  - pick_up_tool()
  - use_tool_on_droid()
  - pick_up_crystal()
  - get_status()

### 7. GameController
- Manages game flow
- Attributes: maintenance_tunnels, docking_bay, droid

## Game Setup
- Create two locations:
  - Maintenance Tunnels (has_tool=True, droid_present=True)
  - Docking Bay (has_crystal=True)

## Scoring System
- Points awarded for:
  - Picking up Diagnostic Tool: +10
  - Repairing Droid: +20
  - Picking up Energy Crystal: +50
  - Completing mission: +30
- Hazard counter increases if player tries to move past blocking droid
