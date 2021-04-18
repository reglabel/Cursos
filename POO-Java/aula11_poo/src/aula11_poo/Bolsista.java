package aula11_poo;

public class Bolsista extends Aluno{
	private float bolsa;
	
	public void renovarBolsa() {
		System.out.println("\r\nMensalidade de " + nome + " paga com sucesso!");
	}

	@Override
	public void pagarMensalidade() {
		System.out.println("\r\n" + nome + " é bolsista! Pagamento facilitado!");
	}

	public float getBolsa() {
		return bolsa;
	}

	public void setBolsa(float bolsa) {
		this.bolsa = bolsa;
	}
	
	
}
