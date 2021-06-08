package MovingObjects;

import java.util.ArrayList;

import aggregationtest.Author;

public class main {
	public static void main (String [] args) {
		PoliceCar cruiser1 = new PoliceCar(2);
		
		ArrayList<PoliceCar> myArray = new ArrayList();
		
		myArray.add(cruiser1);
		
		System.out.println(myArray);
		
	}
}
