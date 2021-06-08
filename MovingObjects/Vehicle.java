package MovingObjects;

public abstract class Vehicle implements LandVehicle, SeaVessel{
	
	private String name;
	private int maxPassangers;
	private float maxSpeed;
	private int numWheels;
	private int displacement;
	
	public abstract void drive();
	public abstract void launch();
}
