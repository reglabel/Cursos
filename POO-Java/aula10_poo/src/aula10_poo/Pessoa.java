package aula10_poo;

public class Pessoa {
	private String nome;
	private int idade;
	private String sexo;
	
	@Override
	public String toString() {
		return "\r\n\t---- Pessoa ----\r\n-> Nome: " + nome +
				"\r\n-> Idade: " + idade +
				"\r\n-> Sexo: " + sexo + "\r\n";
	}

	public void fazerAniv() {
		idade += 1;
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
