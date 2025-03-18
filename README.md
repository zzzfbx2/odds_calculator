# Sequential Betting Calculator

This is an AI agent designed to assist with sequential betting odds calculations, with all amounts in rupees. The agent remembers your initial bet and calculates the optimal amount to bet when odds change, guaranteeing a profit regardless of the outcome whenever possible.

## Available Versions

This calculator comes in two versions:
1. **Command Line Interface** - Simple text-based calculator
2. **Graphical User Interface** - Modern, user-friendly interface with betting history and advanced features

## How It Works

The agent operates for a two-outcome betting scenario (e.g., a tennis match with outcomes A and B):

1. You input the stake amount in rupees and the odds for your initial bet on outcome A
2. When the odds for outcome B change, you provide the current odds
3. The agent checks if a guaranteed profit is possible
4. If possible, it calculates the optimal hedge bet amount
5. It tells you exactly how much to bet on outcome B and the profit you'll secure

## How to Use the Command Line Version

1. Run the script: `python sequential_betting_calculator.py`
2. Enter your stake and odds for outcome A when prompted
3. Input new odds for outcome B as they change
4. Choose to check more odds or exit

## How to Use the GUI Version

1. Run the script: `python betting_calculator_gui.py`
2. The application offers two tabs:

### Hedge Betting Tab
1. Enter your stake amount for outcome A
2. Enter the odds for outcome A
3. Enter the current odds for outcome B
4. Click "Calculate Hedge Bet"
5. View the results and any profit potential
6. The application will keep a history of your recent calculations

### Favorite Betting Tab (NEW!)
1. Enter your stake amount for the favorite
2. Enter the current odds for the favorite
3. Specify your target profit amount
4. Click "Find Target Odds"
5. The agent will calculate what odds you need to look for on the underdog
6. It will show exactly how much to bet when those odds are available

## Example Interaction (Command Line)

```
Welcome to the Sequential Betting Calculator (Currency: Rupees)
Enter the stake amount in rupees for your first bet on outcome A: 100
Enter the odds for outcome A: 2.0
You have bet 100.0 rupees on outcome A at odds 2.0.
Enter the current odds for outcome B to calculate the hedge: 3.0
Bet 66.67 rupees on outcome B at odds 3.0 to lock in a profit of 33.33 rupees, regardless of the outcome.
Do you want to check another odds for outcome B? (yes/no): yes
Enter the current odds for outcome B to calculate the hedge: 1.5
At the current odds, it is not possible to hedge for a guaranteed profit.
Do you want to check another odds for outcome B? (yes/no): no
Thank you for using the Sequential Betting Calculator!
```

## GUI Features

- Modern, user-friendly interface
- Input validation to prevent errors
- Clear results display with profit indicators
- History of recent betting calculations
- Instant calculations without needing to restart for new scenarios
- Tabbed interface with specialized betting calculators:
  - Hedge betting calculator for existing bets
  - Favorite betting calculator for planning future bets

## Requirements

- Python 3.6 or higher
- Tkinter (included with most Python installations)

## Key Features

- Remembers your first bet until you exit
- Only suggests a hedge bet when a profit is assured
- Provides clear instructions in plain language
- Allows testing multiple odds without re-entering the first bet
- Calculates target odds to achieve a specific profit goal
- Recommends exactly how much to bet on the underdog when target odds are available 