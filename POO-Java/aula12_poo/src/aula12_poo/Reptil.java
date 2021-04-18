package aula12_poo;

public class Reptil extends Animal{
	private String corEscama;

	public Reptil(String corEscama, float peso, int idade, int membros) {
		super(peso, idade, membros);
		this.corEscama = corEscama;
	}

	public String toString(String especie) {
		return "\r\n\t--- " + especie + " ---\r\n-> CorEscama: " + corEscama +
				"\r\n-> Peso: " + peso +
				"\r\n-> Idade: " + idade +
				"\r\n-> Membros: " + membros + "\r\n";
	}
	
	@Override
	public String toString() {
		return "\r\n\t--- Reptil ---\r\n-> CorEscama: " + corEscama +
				"\r\n-> Peso: " + peso +
				"\r\n-> Idade: " + idade +
				"\r\n-> Membros: " + membros + "\r\n";
	}

	@Override
	public void locomover() {
		System.out.println("\r\nEi, aqui embaixo! Rastejando...");
	}

	@Override
	public void alimentar() {
		System.out.println("\r\nVocê nem me viu! Comendo vegetais...");
	}

	@Override
	public void emitirSom() {
		System.out.println("\r\nBaixinho agora...sons de réptil...");		
	}

	public String getCorEscama() {
		return corEscama;
	}

	public void setCorEscama(String corEscama) {
		this.corEscama = corEscama;
	}
	
	
}
