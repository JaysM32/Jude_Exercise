package MovingObjects;

public class Hovercraft extends Vehicle{
	public void enterLand() {
		System.out.println("Changing mode to land ...");
	}
	
	public void enterSea() {
		System.out.println("Changing mode to sea ...");
	}
	@Override
	public void drive() {
		// TODO Auto-generated method stub
		System.out.println("Vrooom!");
	}

	@Override
	public void launch() {
		// TODO Auto-generated method stub
		System.out.println("Vroom!");
	}

}
