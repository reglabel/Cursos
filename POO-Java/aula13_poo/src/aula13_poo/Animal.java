package aula13_poo;

public abstract class Animal {
	protected float peso;
	protected int idade;
	protected int membros;
	
	public Animal(float peso, int idade, int membros) {
		this.peso = peso;
		this.idade = idade;
		this.membros = membros;
	}

	@Override
	public String toString() {
		return "\r\n--- Animal ---\r\n-> Peso: " + peso +
				"\r\n-> Idade: " + idade +
				"\r\n-> Membros: " + membros + "\r\n";
	}

	public String toString(String especie) {
		return "\r\n--- " + especie + " ---\r\n-> Peso: " + peso +
				"\r\n-> Idade: " + idade +
				"\r\n-> Membros: " + membros + "\r\n";
	}

	public abstract void emitirSom();
}
