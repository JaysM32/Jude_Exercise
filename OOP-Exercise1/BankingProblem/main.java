package BankingProblem;
import java.util.ArrayList;

public class main {
	public static void main (String args[]) {
		Account A1 = new Account(2000);
		Account A2 = new Account(60000);
		Account A3 = new Account(500);
		Account A4 = new Account(10000);
		
		ArrayList<Account> Accounts1 = new ArrayList();
		
		Accounts1.add(A1);
		Accounts1.add(A2);
		Accounts1.add(A3);
		Accounts1.add(A4);
		
		
		Bank BCA = new Bank("BCA");
		
		BCA.addCustomer("Bernard","Wijaya");
		BCA.addCustomer("Jude","Martinez");
		BCA.addCustomer("Nathanael","Setiawan");
		BCA.addCustomer("Vania","Natalie");
		
		for (int i = 0 ; i < BCA.getNoofcustomer() ; i++) {
			BCA.getCustomers(i).setAccount(Accounts1.get(i));
		}
		
		System.out.println("the number of customer in BCA is " + BCA.getNoofcustomer());
		System.out.println("the customers in BCA are ");
		for (int i = 0 ; i < BCA.getNoofcustomer() ; i++) {
			System.out.println("Name = " + BCA.getCustomers(i).getFirstname() + " " + BCA.getCustomers(i).getLastname() + ", "
					+ "their balance is " + BCA.getCustomers(i).getAccount().getBalance());
		}
		System.out.println("------------------------------------------------------------------------------------");
		System.out.println("Bernard decided to withdraw 500 = " + BCA.getCustomers(0).getAccount().Withdraw(500));
		System.out.println("Vania decided to withdraw 5000 = " + BCA.getCustomers(3).getAccount().Withdraw(5000));
		System.out.println("Jude decided to withdraw 500000 = " + BCA.getCustomers(1).getAccount().Withdraw(500000));
		System.out.println("Nathan decided to deposit 4000 = " + BCA.getCustomers(2).getAccount().Deposit(4000));
		System.out.println("Bernard decided to deposit 40000 = " + BCA.getCustomers(0).getAccount().Deposit(40000));
		System.out.println("------------------------------------------------------------------------------------");
		for (int i = 0 ; i < BCA.getNoofcustomer() ; i++) {
			System.out.println("Name = " + BCA.getCustomers(i).getFirstname() + " " + BCA.getCustomers(i).getLastname() + ", "
					+ "their balance is " + BCA.getCustomers(i).getAccount().getBalance());
		}
		
	}
	
	
}
