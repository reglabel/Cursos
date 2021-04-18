package aula10_poo;

public class Professor extends Pessoa{
	private String especialidade;
	private float salario;
	
	public void receberAum(float aumento) {
		setSalario(getSalario() + aumento);
	}
	
	public String getEspecialidade() {
		return especialidade;
	}

	public void setEspecialidade(String especialidade) {
		this.especialidade = especialidade;
	}

	public float getSalario() {
		return salario;
	}

	public void setSalario(float salario) {
		this.salario = salario;
	}
}
