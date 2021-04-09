package BankingProblem;

public class Account {
	private double Balance;

	public Account(double balance) {
		Balance = balance;
	}

	public double getBalance() {
		return Balance;
	}

	public boolean Deposit(double amount) {
		if (amount >= 0) {
			this.Balance += amount;
			return true;
		}else {
			return false;
		}
	}
	
	public boolean Withdraw(double amount) {
		if (this.Balance >  amount && amount > 0 ) {
			this.Balance -= amount;
			return true;
		}else {
			return false;
		}
	}
	
}
