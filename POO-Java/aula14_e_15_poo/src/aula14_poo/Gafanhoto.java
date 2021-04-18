package aula14_poo;

public class Gafanhoto extends Pessoa{
	private String login;
	private int totAssistido;
	
	public Gafanhoto(String nome, int idade, String sexo, String login) {
		super(nome, idade, sexo);
		this.login = login;
		totAssistido = 0;
	}
	
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return super.toString() + "\r\n-> Login: " + login +
				"\r\n-> TotAssistido: " + totAssistido;
	}

	public void viuMaisUm() {
		
	}

	@Override
	protected void ganharExp() {
		
	}

	public int getTotAssistido() {
		return totAssistido;
	}

	public void setTotAssistido(int totAssistido) {
		this.totAssistido = totAssistido;
	}
}
