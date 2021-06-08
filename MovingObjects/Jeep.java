package MovingObjects;

public class Jeep extends Vehicle{
	
	
	public void soundHorn() {
		System.out.println("Honk!");
	}
	
	@Override
	public void launch() {
		// TODO Auto-generated method stub
		System.out.println("Vroom!");
	}

	@Override
	public void drive() {
		// TODO Auto-generated method stub
		System.out.println("Vrooom!");
	}
	
}
