package aula10_poo;

public class Funcionario extends Pessoa{
	private String setor;
	private boolean trabalhando;
	
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return super.toString() + "-> Setor: " + setor
				+ "\r\n-> Trabalhando? " + trabalhando;
	}

	public void mudarTrabalho() {
		setTrabalhando(!(isTrabalhando()));
	}

	public String getSetor() {
		return setor;
	}

	public void setSetor(String setor) {
		this.setor = setor;
	}

	public boolean isTrabalhando() {
		return trabalhando;
	}

	public void setTrabalhando(boolean trabalhando) {
		this.trabalhando = trabalhando;
	}
}
