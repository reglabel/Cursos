package aula12_poo;

public class Peixe extends Animal{
	private String corEscama;

	public Peixe(String corEscama, float peso, int idade, int membros) {
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
		return "\r\n\t--- Peixe ---\r\n-> CorEscama: " + corEscama +
				"\r\n-> Peso: " + peso +
				"\r\n-> Idade: " + idade +
				"\r\n-> Membros: " + membros + "\r\n";
	}
	
	public void soltarBolhas() {
		System.out.println("\r\nGlub! Glub! Soltando bolhas...");
	}
	
	@Override
	public void locomover() {
		System.out.println("\r\nNadando...continue a nadar...nadar...nadar...");
	}

	@Override
	public void alimentar() {
		System.out.println("\r\nTá flutuando, bicho! Comendo substâncias aquáticas...");		
	}

	@Override
	public void emitirSom() {
		System.out.println("\r\nSons de...PERA AÍ! Peixe não faz som, doido...");		
	}

	public String getCorEscama() {
		return corEscama;
	}

	public void setCorEscama(String corEscama) {
		this.corEscama = corEscama;
	}
	
	
}
