import tkinter as tk
from tkinter import ttk, messagebox
import re

class BettingCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Betting Agent")
        self.root.geometry("600x550")
        self.root.resizable(False, False)
        
        # Set color scheme
        self.bg_color = "#f0f0f0"
        self.accent_color = "#4a6fa5"
        self.root.configure(bg=self.bg_color)
        
        # Variables
        self.stake_a = tk.DoubleVar(value=100.0)
        self.odds_a = tk.DoubleVar(value=2.0)
        self.odds_b = tk.DoubleVar(value=3.0)
        self.bet_history = []
        
        # Favorite betting variables
        self.fav_stake = tk.DoubleVar(value=100.0)
        self.fav_odds = tk.DoubleVar(value=1.5)
        self.target_profit = tk.DoubleVar(value=20.0)
        
        # Title
        title_frame = tk.Frame(self.root, bg=self.bg_color)
        title_frame.pack(pady=10)
        
        title_label = tk.Label(
            title_frame, 
            text="Sequential Betting Calculator",
            font=("Arial", 18, "bold"),
            bg=self.bg_color,
            fg=self.accent_color
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame, 
            text="All amounts in Rupees",
            font=("Arial", 12),
            bg=self.bg_color
        )
        subtitle_label.pack()
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=20, pady=5)
        
        # Create tabs
        self.hedge_tab = tk.Frame(self.notebook, bg=self.bg_color)
        self.favorite_tab = tk.Frame(self.notebook, bg=self.bg_color)
        
        self.notebook.add(self.hedge_tab, text="Hedge Betting")
        self.notebook.add(self.favorite_tab, text="Favorite Betting")
        
        # Setup Hedge Betting Tab
        self.setup_hedge_tab()
        
        # Setup Favorite Betting Tab
        self.setup_favorite_tab()
        
        # Footer
        footer_frame = tk.Frame(self.root, bg=self.bg_color)
        footer_frame.pack(pady=5)
        
        footer_label = tk.Label(
            footer_frame, 
            text="AI Betting Agent",
            font=("Arial", 9),
            bg=self.bg_color,
            fg="gray"
        )
        footer_label.pack()
    
    def setup_hedge_tab(self):
        # Input frame
        input_frame = tk.LabelFrame(
            self.hedge_tab, 
            text="Initial Bet Details",
            font=("Arial", 12, "bold"),
            padx=10, 
            pady=10,
            bg=self.bg_color
        )
        input_frame.pack(fill="x", padx=10, pady=10)
        
        # Stake A
        stake_a_label = tk.Label(
            input_frame, 
            text="Stake Amount (₹):",
            font=("Arial", 11),
            bg=self.bg_color
        )
        stake_a_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        # Only allow numeric input with decimal point
        vcmd = (self.root.register(self.validate_numeric_input), '%P')
        
        stake_a_entry = tk.Entry(
            input_frame, 
            textvariable=self.stake_a,
            font=("Arial", 11),
            width=10,
            validate="key", 
            validatecommand=vcmd
        )
        stake_a_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        # Odds A
        odds_a_label = tk.Label(
            input_frame, 
            text="Odds for Outcome A:",
            font=("Arial", 11),
            bg=self.bg_color
        )
        odds_a_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        
        odds_a_entry = tk.Entry(
            input_frame, 
            textvariable=self.odds_a,
            font=("Arial", 11),
            width=10,
            validate="key", 
            validatecommand=vcmd
        )
        odds_a_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        # Odds B
        odds_b_label = tk.Label(
            input_frame, 
            text="Current Odds for Outcome B:",
            font=("Arial", 11),
            bg=self.bg_color
        )
        odds_b_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        
        odds_b_entry = tk.Entry(
            input_frame, 
            textvariable=self.odds_b,
            font=("Arial", 11),
            width=10,
            validate="key", 
            validatecommand=vcmd
        )
        odds_b_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        # Calculate button
        calculate_button = tk.Button(
            input_frame,
            text="Calculate Hedge Bet",
            font=("Arial", 11, "bold"),
            bg=self.accent_color,
            fg="white",
            padx=10,
            command=self.calculate_hedge
        )
        calculate_button.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Results frame
        self.results_frame = tk.LabelFrame(
            self.hedge_tab, 
            text="Results",
            font=("Arial", 12, "bold"),
            padx=10, 
            pady=10,
            bg=self.bg_color
        )
        self.results_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Results text widget
        self.results_text = tk.Text(
            self.results_frame,
            font=("Arial", 11),
            height=8,
            width=60,
            wrap=tk.WORD,
            bg="white"
        )
        self.results_text.pack(fill="both", expand=True, padx=5, pady=5)
        self.results_text.config(state=tk.DISABLED)
        
        # History frame
        history_frame = tk.LabelFrame(
            self.hedge_tab, 
            text="Betting History",
            font=("Arial", 12, "bold"),
            padx=10, 
            pady=10,
            bg=self.bg_color
        )
        history_frame.pack(fill="x", padx=10, pady=10)
        
        # History list
        self.history_listbox = tk.Listbox(
            history_frame,
            font=("Arial", 10),
            height=4
        )
        self.history_listbox.pack(fill="both", expand=True)
    
    def setup_favorite_tab(self):
        # Input frame
        fav_input_frame = tk.LabelFrame(
            self.favorite_tab, 
            text="Favorite Betting Details",
            font=("Arial", 12, "bold"),
            padx=10, 
            pady=10,
            bg=self.bg_color
        )
        fav_input_frame.pack(fill="x", padx=10, pady=10)
        
        # Validate command for numeric entry
        vcmd = (self.root.register(self.validate_numeric_input), '%P')
        
        # Stake
        fav_stake_label = tk.Label(
            fav_input_frame, 
            text="Stake Amount (₹):",
            font=("Arial", 11),
            bg=self.bg_color
        )
        fav_stake_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        fav_stake_entry = tk.Entry(
            fav_input_frame, 
            textvariable=self.fav_stake,
            font=("Arial", 11),
            width=10,
            validate="key", 
            validatecommand=vcmd
        )
        fav_stake_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        # Current Odds
        fav_odds_label = tk.Label(
            fav_input_frame, 
            text="Current Favorite Odds:",
            font=("Arial", 11),
            bg=self.bg_color
        )
        fav_odds_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        
        fav_odds_entry = tk.Entry(
            fav_input_frame, 
            textvariable=self.fav_odds,
            font=("Arial", 11),
            width=10,
            validate="key", 
            validatecommand=vcmd
        )
        fav_odds_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        # Target Profit
        profit_label = tk.Label(
            fav_input_frame, 
            text="Target Profit (₹):",
            font=("Arial", 11),
            bg=self.bg_color
        )
        profit_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        
        profit_entry = tk.Entry(
            fav_input_frame, 
            textvariable=self.target_profit,
            font=("Arial", 11),
            width=10,
            validate="key", 
            validatecommand=vcmd
        )
        profit_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        # Calculate button
        fav_calculate_button = tk.Button(
            fav_input_frame,
            text="Find Target Odds",
            font=("Arial", 11, "bold"),
            bg=self.accent_color,
            fg="white",
            padx=10,
            command=self.calculate_favorite_target
        )
        fav_calculate_button.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Results frame
        self.fav_results_frame = tk.LabelFrame(
            self.favorite_tab, 
            text="Recommended Betting Strategy",
            font=("Arial", 12, "bold"),
            padx=10, 
            pady=10,
            bg=self.bg_color
        )
        self.fav_results_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Results text widget
        self.fav_results_text = tk.Text(
            self.fav_results_frame,
            font=("Arial", 11),
            height=12,
            width=60,
            wrap=tk.WORD,
            bg="white"
        )
        self.fav_results_text.pack(fill="both", expand=True, padx=5, pady=5)
        self.fav_results_text.config(state=tk.DISABLED)
    
    def validate_numeric_input(self, new_value):
        """Validate that input is numeric, allowing decimals"""
        if new_value == "":
            return True
        try:
            return bool(re.match(r'^\d*\.?\d*$', new_value))
        except:
            return False
        
    def calculate_hedge(self):
        """Calculate and display the hedge bet"""
        try:
            stake_a = self.stake_a.get()
            odds_a = self.odds_a.get()
            odds_b = self.odds_b.get()
            
            if stake_a <= 0 or odds_a <= 1 or odds_b <= 1:
                messagebox.showerror("Invalid Input", "Please enter valid values. Stake must be positive and odds must be greater than 1.")
                return
            
            # Calculate hedge bet
            result_text = f"Initial bet: ₹{stake_a:.2f} on outcome A at odds {odds_a:.2f}\n\n"
            
            if 1/odds_a + 1/odds_b < 1:
                stake_b = (stake_a * odds_a) / odds_b
                profit = stake_a * odds_a - stake_a - stake_b
                
                result_text += f"✅ Profitable hedge bet possible!\n\n"
                result_text += f"Bet ₹{stake_b:.2f} on outcome B at odds {odds_b:.2f}\n\n"
                result_text += f"Guaranteed profit: ₹{profit:.2f} regardless of outcome"
                
                # Add to history
                history_entry = f"A: ₹{stake_a:.2f} @ {odds_a:.2f}, B: ₹{stake_b:.2f} @ {odds_b:.2f}, Profit: ₹{profit:.2f}"
                self.bet_history.append(history_entry)
                self.update_history()
            else:
                result_text += f"❌ At the current odds of {odds_b:.2f} for outcome B, it is not possible to hedge for a guaranteed profit."
            
            # Update results text
            self.results_text.config(state=tk.NORMAL)
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, result_text)
            self.results_text.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def calculate_favorite_target(self):
        """Calculate and display target odds for betting on the favorite"""
        try:
            stake = self.fav_stake.get()
            current_odds = self.fav_odds.get()
            target_profit = self.target_profit.get()
            
            if stake <= 0 or current_odds <= 1 or target_profit <= 0:
                messagebox.showerror("Invalid Input", "Please enter valid values. Stake and target profit must be positive, and odds must be greater than 1.")
                return
            
            # Calculate the required underdog odds to guarantee the target profit
            # First, calculate what our potential return would be if favorite wins
            potential_return = stake * current_odds
            
            # Target odds needed for underdog to guarantee profit
            target_odds = potential_return / (stake + target_profit)
            
            # Calculate the stake needed on underdog if those odds are found
            underdog_stake = (stake * current_odds) / target_odds
            
            # Calculate the guaranteed profit
            guaranteed_profit = stake * current_odds - stake - underdog_stake
            
            # Calculate how much the current odds need to change
            required_odds_shift = ((1/current_odds + 1/target_odds) - 1) * 100
            
            # Prepare result text
            result_text = f"Initial bet on favorite: ₹{stake:.2f} at odds {current_odds:.2f}\n\n"
            result_text += f"📊 Target Odds Analysis:\n\n"
            result_text += f"To guarantee a profit of ₹{target_profit:.2f}, you need:\n\n"
            result_text += f"1. Wait for underdog odds to reach at least {target_odds:.2f}\n"
            result_text += f"2. Then bet ₹{underdog_stake:.2f} on the underdog\n\n"
            
            if 1/current_odds + 1/target_odds < 1:
                result_text += f"✅ This strategy would generate ₹{guaranteed_profit:.2f} profit\n"
                result_text += f"regardless of which outcome occurs."
            else:
                result_text += f"⚠️ At the current favorite odds, you need a market inefficiency\n"
                result_text += f"of at least {required_odds_shift:.2f}% to guarantee your target profit."
            
            # Update results text
            self.fav_results_text.config(state=tk.NORMAL)
            self.fav_results_text.delete(1.0, tk.END)
            self.fav_results_text.insert(tk.END, result_text)
            self.fav_results_text.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def update_history(self):
        """Update the history listbox"""
        self.history_listbox.delete(0, tk.END)
        for i, entry in enumerate(reversed(self.bet_history[-5:])):  # Show most recent 5 entries
            self.history_listbox.insert(tk.END, f"{i+1}. {entry}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BettingCalculatorGUI(root)
    root.mainloop() 