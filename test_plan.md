# RPG Test Plan

## 1. Golden Path Testing
### 1.1 Game Initialization
- [ ] Verify game starts correctly
- [ ] Check initial player status (health, score, inventory)
- [ ] Validate starting location description

### 1.2 Movement
- [ ] Test movement in all valid directions (north, south, east, west)
- [ ] Verify location updates correctly after movement
- [ ] Confirm movement to invalid directions is prevented

### 1.3 Item Collection
- [ ] Test collecting available items in each location
- [ ] Verify item is added to player's inventory
- [ ] Check item is removed from location after collection

### 1.4 Droid Interaction
- [ ] Test examining the damaged droid
- [ ] Verify using the diagnostic tool on the droid
- [ ] Confirm droid repair state updates correctly
- [ ] Check score updates after droid repair

### 1.5 Winning Condition
- [ ] Test reaching the final location with all required items
- [ ] Verify win condition triggers correctly
- [ ] Confirm final score calculation

## 2. Edge Case Testing
### 2.1 Inventory Management
- [ ] Attempt to collect non-existent item
- [ ] Test inventory limits (if any)
- [ ] Try using items in wrong contexts

### 2.2 Movement Constraints
- [ ] Test movement when blocked by droid
- [ ] Verify blocked paths remain blocked until droid is repaired
- [ ] Test movement with invalid directions

### 2.3 Game State
- [ ] Test saving and loading game state
- [ ] Verify game state persists correctly
- [ ] Test game over conditions

## 3. Input Validation
### 3.1 Valid Commands
- [ ] Test all valid commands (go, take, use, examine, inventory, etc.)
- [ ] Verify command aliases work as expected

### 3.2 Invalid Inputs
- [ ] Test empty input
- [ ] Test gibberish input
- [ ] Test partially correct commands
- [ ] Test commands with extra whitespace

## 4. Score and Progress Tracking
- [ ] Verify score increments correctly for each action
- [ ] Test score persistence across game sessions
- [ ] Verify progress is tracked accurately

## 5. Documentation
- [ ] Document test results with screenshots
- [ ] Note any bugs found during testing
- [ ] Record test environment details

## Test Evidence
*Attach screenshots of test execution here*
- [ ] Screenshot 1: Game initialization
- [ ] Screenshot 2: Successful item collection
- [ ] Screenshot 3: Droid interaction sequence
- [ ] Screenshot 4: Winning condition triggered
- [ ] Screenshot 5: Error handling examples
