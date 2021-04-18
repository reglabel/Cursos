package aula13_poo;

public class Principal {

	public static void main(String[] args) {
		Mamifero m = new Mamifero("Marrom", 23f, 13, 2);
		Lobo l = new Lobo("Preto", 10f, 15, 4);
		Cachorro c = new Cachorro("Gold", 8.5f, 5, 4);
		
		System.out.println(m.toString());
		m.emitirSom();
		
		System.out.println(l.toString());
		l.emitirSom();
		
		System.out.println(c.toString());
		c.emitirSom();
		
		c.reagir("ola");
		c.reagir("toma comida");
		c.reagir("vai apanhar");
		c.reagir(11, 45);
		c.reagir(15, 20);
		c.reagir(21, 00);
		c.reagir(true);
		c.reagir(false);
		c.reagir(3, 5.2f);
		c.reagir(2, 12.5f);
		c.reagir(17, 4.5f);
		c.reagir(11, 20.5f);
	}
}
