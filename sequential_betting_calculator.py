def sequential_betting_calculator():
    print("Welcome to the Sequential Betting Calculator (Currency: Rupees)")
    # Get the first bet details
    S_A = float(input("Enter the stake amount in rupees for your first bet on outcome A: "))
    O_A = float(input("Enter the odds for outcome A: "))
    print(f"You have bet {S_A} rupees on outcome A at odds {O_A}.")
    
    # Allow checking hedge bets with new odds
    while True:
        O_B = float(input("Enter the current odds for outcome B to calculate the hedge: "))
        if 1/O_A + 1/O_B < 1:
            S_B = (S_A * O_A) / O_B
            P = S_A * O_A - S_A - S_B
            print(f"Bet {S_B:.2f} rupees on outcome B at odds {O_B} to lock in a profit of {P:.2f} rupees, regardless of the outcome.")
        else:
            print("At the current odds, it is not possible to hedge for a guaranteed profit.")
        cont = input("Do you want to check another odds for outcome B? (yes/no): ")
        if cont.lower() != 'yes':
            print("Thank you for using the Sequential Betting Calculator!")
            break

if __name__ == "__main__":
    sequential_betting_calculator() 