package BankingProblem;

public class Customer {
	private final String Firstname, Lastname;
	private Account account;
	
	public Customer(String firstname, String lastname) {
		this.Firstname = firstname;
		this.Lastname = lastname;
	}

	public String getFirstname() {
		return Firstname;
	}

	public String getLastname() {
		return Lastname;
	}

	public Account getAccount() {
		return account;
	}

	public void setAccount(Account account) {
		this.account = account;
	}
	
	
}
