Report Structure and Requirements
Your report must be organised into the following five sections.

1. Project Management & Process (Corresponds to C1)
This section documents your development journey.

1.1. Project Overview: A brief introduction that sets the context for your report.

Explain the overall aim of the blended project (linking the Part A RPG and Part B Robot).

State the specific aim and scope of your Part A RPG.

State the aim of your team's Part B Mechatronics enhancement.

1.2. Logbook Summary: Provide a detailed summary of your dated logbook entries. This should be a narrative of your progress, showing the development timeline, challenges you faced, and how you solved problems for both Part A and Part B.

1.3. Version Control (GitHub): Briefly describe how you used GitHub.

Provide a link to your Part A repository.

Provide a link to your team's Part B repository.

Explain how your commit history shows an iterative process (e.g., "Commits were made after implementing each new feature, such as the examine command...").

1.4. AI Usage Transparency: If you used any AI tools, you must be transparent. For each instance of use, provide:

The prompt you used.

The raw output the AI generated.

A clear analysis of how you verified, adapted, and improved the AI's output to make it your own.

2. System Design & Visualisation (Corresponds to C2)
This section presents the design blueprints for your software. All diagrams must be your own work, use correct conventions, be clearly labelled, and embedded directly into your report.

2.1. Part A: RPG Design Diagrams:

This sub-section requires you to create four distinct types of diagrams to fully document the design, logic, and user experience of your RPG. Each diagram must be your own work, use correct conventions, and be clearly labelled and embedded in your report.

Storyboard (6–8 frames)
Your storyboard must illustrate the User Interface (UI) and User Experience (UX) flow by capturing the "Golden Path"—the successful win sequence from start to finish. Each frame should clearly depict:

The game's textual output to the player.

The specific command the player enters.

The resulting change in game state (e.g., "Score: 50", "Hazard: 1").

UML Class Diagram
Provide a complete and accurate UML diagram for your entire RPG codebase. This diagram shows the static, object-oriented structure of your project. It must clearly show:

All classes you implemented (e.g., Game, Player, Location, the abstract StationItem, and its concrete subclasses like DiagnosticTool).

Attributes and methods for each class.

Relationships between classes, especially Inheritance (e.g., DiagnosticTool inheriting from StationItem) and Composition (e.g., a Player having an inventory of StationItem objects).

Clear indication of abstract classes and overridden methods (e.g., the polymorphic examine() method).

Structure Chart
Create a structure chart that shows the top-down modular design and control flow of your main game loop. Your chart must follow this specific hierarchy:

At the top level: Start Game Loop.

This top module should call two main sub-modules: Process Player Input and Check Win Condition.

The Process Player Input module must, in turn, show calls to the following modules:

Move Player

Collect Item

Repair Droid

Show Status

Attempt Win

Use arrows to illustrate the flow of control from the calling modules to the sub-modules.

Flowcharts (A set of three)
Provide three separate flowcharts that detail the step-by-step logic within specific, critical game mechanics. You must create a flowchart for each of the following processes:

Movement Logic: This flowchart must show how the program checks for valid exits from the player's current location, handles the logic for the blocking droid (i.e., preventing movement until it's repaired), and updates either the player's location or the hazard counter.

'Use Tool' Logic: This flowchart must detail the process of verifying that the player has the DiagnosticTool, checking that they are targeting the DamagedMaintenanceDroid, and then successfully updating the droid's state and the player's score.

Winning Logic: This flowchart must illustrate the final win condition check, showing how the program validates that the player is in the correct location (Bay) AND has the Crystal in their inventory before it awards the score bonus and ends the game.

2.2. Part B: Mechatronics Logic Flowchart:

A single, detailed flowchart that accurately represents the decision-making logic of your team's new hardware feature (e.g., how the robot decides when to turn based on sensor input).

3. Testing & Quality Assurance (Corresponds to C3)
This section provides the evidence that your projects work and documents how you ensured their quality.

3.1. Part A: RPG Test Plan:

Document your test plan for the RPG. Include test cases for the "golden path" (the winning sequence), edge cases (e.g., trying to use an item you don't have), and invalid user inputs.

Provide evidence of your testing, such as annotated screenshots of your terminal showing the tests being performed.

3.2. Part B: Mechatronics Testing Strategy:

Describe the strategy your team used to test the robot enhancement. How did you confirm it was working reliably? (e.g., "We tested the ultrasonic sensor in different lighting conditions..."). You should refer to the "Component Test" video submitted in Part B as evidence of your initial testing.

3.3. Bug Identification & Resolution:

Identify at least one significant bug you encountered in either Part A or Part B.

Explain the bug, how you diagnosed the problem (e.g., "I used print statements to trace the variable's value..."), and the specific steps you took to fix it.

4. Technical Analysis & Explanation (Corresponds to C4)
This section is where you explain the "how" and "why" behind your code.

4.1. Analysis of OOP in Part A (COIPEA):

Provide a detailed explanation of how you applied the principles of Class, Object, Inheritance, Polymorphism, Encapsulation, and Abstraction in your RPG. For each principle, provide a specific code snippet from your project as an example and explain it.

4.2. Analysis of the Part B System:

Explain exactly how your team's Python code interacts with the robot's hardware components (sensors and actuators).

Include annotated "before and after" code snippets to clearly show the key changes your team made to implement the new feature.

4.3. Personal Contribution to Part B:

Provide a specific and detailed description of your personal technical contributions to the group project. What specific parts of the code did you write? What was your role in hardware assembly or testing? Be precise.

5. Critical Reflection & Evaluation (Corresponds to C5)
This final section is your opportunity to reflect on your growth and the project outcomes.

5.1. Reflection on Learning & Challenges:

What was the most difficult technical concept you grappled with during this project, and what did you learn from it?

What are you most proud of accomplishing, and why?

5.2. Reflection on Teamwork & Process:

What was one key takeaway from working in a team on the mechatronics project?

How did your planning (or lack of planning) impact the final outcome of either project?

5.3. Reflection on Future Improvement:

If you had another week, what is one meaningful improvement you would make to either the RPG or the robot?

What would you do differently if you were to start this project again?

