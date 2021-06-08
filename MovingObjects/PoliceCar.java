package MovingObjects;

public class PoliceCar implements LandVehicle, IsEmergency{
	private int numOfWeapons;
	
	public PoliceCar(int numOfWeapons) {
		super();
		this.numOfWeapons = numOfWeapons;
	}

	public int getNumOfWeapons() {
		return numOfWeapons;
	}

	public void setNumOfWeapons(int numOfWeapons) {
		this.numOfWeapons = numOfWeapons;
	}

	@Override
	public void soundSiren() {
		// TODO Auto-generated method stub
		System.out.println("Wiii Wooo Wiii Wooo!");
	}

	@Override
	public void drive() {
		// TODO Auto-generated method stub
		System.out.println("Vrooom!");
	}
	
	public void shineSearchlight() {
		System.out.println("Shiin!");
	}
}
