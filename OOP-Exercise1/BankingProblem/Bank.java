package BankingProblem;
import java.util.ArrayList;


public class Bank {
	private ArrayList<Customer> customers = new ArrayList();
	private int noofcustomer = 0;
	private final String bankName;

	public Bank(String bankName) {
		this.bankName = bankName;
	}
	
	public void addCustomer (String firstName, String lastName) {
		customers.add(new Customer(firstName,lastName));
		noofcustomer++;
		
	}
	
	public Customer getCustomers(int index) {
		return customers.get(index);
	}

	public int getNoofcustomer() {
		return noofcustomer;
	}
	
	
	
	
	
	
	
}
