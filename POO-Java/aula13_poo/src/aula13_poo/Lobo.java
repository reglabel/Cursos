package aula13_poo;

public class Lobo extends Mamifero {

	public Lobo(String corPelo, float peso, int idade, int membros) {
		super(corPelo, peso, idade, membros);
	}

	@Override
	public void emitirSom() {
		System.out.println("Aaauuuuuuuuuuuuuu!");
	}

	@Override
	public String toString() {
		return "\r\n--- Lobo ---\r\n-> Peso: " + peso +
				"\r\n-> Idade: " + idade +
				"\r\n-> Membros: " + membros +
				"\r\n-> CorPelo: " + corPelo + "\r\n";
	}
}
