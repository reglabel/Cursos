package aula11_poo;

public abstract class Pessoa {
	protected String nome;
	protected int idade;
	protected String sexo;
	
	
	
	@Override
	public String toString() {
		return "\r\n\t--- Dados ---\r\n-> Nome: " + nome +
				"\r\n-> Idade: " + idade +
				"\r\n-> Sexo: " + sexo + "\r\n";
	}

	public final void fazerAniv() {
		idade++;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public int getIdade() {
		return idade;
	}

	public void setIdade(int idade) {
		this.idade = idade;
	}

	public String getSexo() {
		return sexo;
	}

	public void setSexo(String sexo) {
		this.sexo = sexo;
	}
	
	
}
