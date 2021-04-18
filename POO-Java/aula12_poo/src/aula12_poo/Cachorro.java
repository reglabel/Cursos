package aula12_poo;

public class Cachorro extends Mamifero{

	public Cachorro(String corPelo, float peso, int idade, int membros) {
		super(corPelo, peso, idade, membros);
		// TODO Auto-generated constructor stub
	}

	public void enterrarOsso() {
		System.out.println("\r\nQue felicidade! Enterrando o osso com orgulho...");
	}
	
	public void abanarRabo() {
		System.out.println("\r\nMas é fofo! Abanando o rabo alegremente...");
	}

	@Override
	public void emitirSom() {
		System.out.println("\r\nEle é um bom garoto! AU! AU! AU!");
	}
	
	
}
