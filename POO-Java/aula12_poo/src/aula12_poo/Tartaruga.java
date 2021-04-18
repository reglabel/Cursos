package aula12_poo;

public class Tartaruga extends Reptil{

	public Tartaruga(String corEscama, float peso, int idade, int membros) {
		super(corEscama, peso, idade, membros);
		// TODO Auto-generated constructor stub
	}

	@Override
	public void locomover() {
		System.out.println("\r\nSem pressa! A n d a n d o   b e e e m   d e v a g a r . . .");
	}
	
	
}
