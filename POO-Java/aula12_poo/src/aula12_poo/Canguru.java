package aula12_poo;

public class Canguru extends Mamifero{

	public Canguru(String corPelo, float peso, int idade, int membros) {
		super(corPelo, peso, idade, membros);
		// TODO Auto-generated constructor stub
	}

	public void usarBolsa() {
		System.out.println("\r\nIsso mesmo! Um canguru usa sua bolsa...");
	}

	@Override
	public void locomover() {
		System.out.println("\r\nPelo campo ensolarado, o canguru vai pulando...");
	}
}
