package aula14_poo;

public abstract class Pessoa {
	protected String nome;
	protected int idade;
	protected String sexo;
	protected float experiencia;
	
	public Pessoa(String nome, int idade, String sexo) {
		this.nome = nome;
		this.idade = idade;
		this.sexo = sexo;
		this.experiencia = 0f;
	}

	@Override
	public String toString() {
		return "\r\n\t--- Pessoa ---\r\n-> Nome: " + nome +
				"\r\n-> Idade: " + idade +
				"\r\n-> Sexo: " + sexo +
				"\r\n-> Experiencia: " + experiencia;
	}


	protected abstract void ganharExp();

	protected String getNome() {
		return nome;
	}

	protected void setNome(String nome) {
		this.nome = nome;
	}

	protected int getIdade() {
		return idade;
	}

	protected void setIdade(int idade) {
		this.idade = idade;
	}

	protected String getSexo() {
		return sexo;
	}

	protected void setSexo(String sexo) {
		this.sexo = sexo;
	}

	protected float getExperiencia() {
		return experiencia;
	}

	protected void setExperiencia(float experiencia) {
		this.experiencia = experiencia;
	}
}
