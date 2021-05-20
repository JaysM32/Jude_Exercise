package Forum1;

import java.util.LinkedList;

public class Specimen {
	private String name;
    private int cageNumber;
    private Species toa; // "Type Of Animal"
    public Specimen( String a, int c, Species s)
    {
        setName(a);
        setCage(c);
        setTOA(s);
    }
    
    public void setName(String a){ 
    	name = a; 
    }
    
    public void setCage(int c){ 
    	cageNumber = c; 
    }
    
    public void setTOA(Species s){ 
    	toa = s; 
    }
    
    public String getName(){ 
    	return name; 
    }
    
    public int getCage(){ 
    	return cageNumber; 
    }
    
    public Species getTOA(){ 
    	return toa; 
    }
    
    public String toString()
    {
        return name + " is a " + toa + " in cage " + cageNumber;
    }

    public int countSpecimens (Specimen[] animals, String s){
        int count = 0;
        for (int i = 0; i < animals.length; i++){
            if (animals[i].getTOA().getSpeciesName().equals(s)){
                count++;
            }
        }
        return count;
    }

    public LinkedList<Specimen> makeList( Specimen[] animals ) {
        LinkedList<Specimen> List = new LinkedList<Specimen>();
        for (int i = 0; i < animals.length; i++){
        	List.add(animals[i]);
        }
        return List;
    }

    public LinkedList<Species> makeSpeciesList(LinkedList<Specimen> animals){
        LinkedList<Species> List = new LinkedList<Species>();
        for (int i = 0; i < animals.size(); i++){
        	List.add(animals.get(i).getTOA());
        }
        return List;
    }

    public LinkedList<Species> makeSpeciesListUnique(LinkedList<Specimen> allSpecies){
        LinkedList<Species> List = new LinkedList<Species>();
        for (int i = 0; i < allSpecies.size(); i++){
            if (List.contains(allSpecies.get(i).getTOA().getSpeciesName()) == false){
            	List.add(allSpecies.get(i).getTOA());
            }
        }
        return List;
    }
}
