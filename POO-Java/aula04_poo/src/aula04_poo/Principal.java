package aula04_poo;
public class Principal {
	public static void main(String[] args) {
		Caneta c1 = new Caneta();
		Caneta c2 = new Caneta("BIC", "Preta", 0.8f, true);
		
		c1.status();
		c2.status();
	}
}
