package aula12_poo;

public class Ave extends Animal{
	private String corPena;
	
	public Ave(String corPena, float peso, int idade, int membros) {
		super(peso, idade, membros);
		this.corPena = corPena;
	}

	public String toString(String especie) {
		return "\r\n\t--- " + especie + " ---\r\n-> CorPena: " + corPena +
				"\r\n-> Peso: " + peso +
				"\r\n-> Idade: " + idade +
				"\r\n-> Membros: " + membros + "\r\n";
	}
	
	@Override
	public String toString() {
		return "\r\n\t--- Ave ---\r\n-> CorPena: " + corPena +
				"\r\n-> Peso: " + peso +
				"\r\n-> Idade: " + idade +
				"\r\n-> Membros: " + membros + "\r\n";
	}
	
	public void fazerNinho() {
		System.out.println("\r\nQue lindo! Fazendo um ninho...");
	}

	@Override
	public void locomover() {
		System.out.println("\r\nVoando! I belive I can fly...");		
	}

	@Override
	public void alimentar() {
		System.out.println("\r\nComendo sementes...");		
	}

	@Override
	public void emitirSom() {
		System.out.println("\r\nÉ música! Sons de ave...");		
	}

	public String getCorPena() {
		return corPena;
	}

	public void setCorPena(String corPena) {
		this.corPena = corPena;
	}
	
	
}
