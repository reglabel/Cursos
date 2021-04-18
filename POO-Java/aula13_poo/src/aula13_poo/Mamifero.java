package aula13_poo;

public class Mamifero extends Animal{
	
	public Mamifero(String corPelo, float peso, int idade, int membros) {
		super(peso, idade, membros);
		this.corPelo = corPelo;
	}

	protected String corPelo;
	
	@Override
	public String toString() {
		return "\r\n--- Mamífero ---\r\n-> Peso: " + peso +
				"\r\n-> Idade: " + idade +
				"\r\n-> Membros: " + membros +
				"\r\n-> CorPelo: " + corPelo + "\r\n";
	}
	
	@Override
	public String toString(String especie) {
		return "\r\n--- " + especie + " ---\r\n-> Peso: " + peso +
				"\r\n-> Idade: " + idade +
				"\r\n-> Membros: " + membros +
				"\r\n-> CorPelo: " + corPelo + "\r\n";
	}

	@Override
	public void emitirSom() {
		System.out.println("Sons de Mamífero...");		
	}
}
