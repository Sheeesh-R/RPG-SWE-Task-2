"""
Main entry point for the Space Station Emergency game.
"""

def main():
    """
    Main function to start the game.
    Entry point for the application.
    """
    try:
        # Import the GameController class
        from game import GameController
        
        # Create and start the game
        game = GameController()
        game.start()
    except ImportError as e:
        print(f"Error importing game modules: {e}")
        print("Please make sure all required files are in the correct location.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please restart the game.")

if __name__ == "__main__":
    main()
