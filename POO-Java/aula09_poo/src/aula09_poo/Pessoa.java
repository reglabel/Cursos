package aula09_poo;

public class Pessoa {
	private String nome;
	private int idade;
	private String sexo;
	
	public Pessoa(String nome, int idade, String sexo) {
		this.nome = nome;
		this.idade = idade;
		this.sexo = sexo;
	}

	public void fazerAniver() {
		this.setIdade(this.getIdade() + 1);
	}

	public String getNome() {
		return nome;
	}

	private int getIdade() {
		return idade;
	}

	private void setIdade(int idade) {
		this.idade = idade;
	}

	public String getSexo() {
		return sexo;
	}
}
