package aula04_poo;
public class Caneta {
	private String modelo;
	private String cor;
	private float ponta;
	private boolean tampada;
	
	public Caneta() {
		this.tampar();
	}
	
	public Caneta(String modelo, String cor, float ponta, boolean tampada) {
		this.setModelo(modelo);
		this.setCor(cor);
		this.setPonta(ponta);
		if (tampada) {
			this.tampar();
		} else {
			this.destampar();
		}
	}
	
	public String getCor() {
		return cor;
	}

	public void setCor(String cor) {
		this.cor = cor;
	}

	public boolean isTampada() {
		return tampada;
	}

	public void tampar() {
		this.tampada = true;
	}
	
	public void destampar() {
		this.tampada = false;
	}

	public String getModelo() {
		return this.modelo;
	}
	
	public void setModelo(String modelo) {
		this.modelo = modelo;
	}
	
	public float getPonta() {
		return this.ponta;
	}
	
	public void setPonta(float ponta) {
		this.ponta = ponta;
	}
	
	public void status() {
		System.out.println("SOBRE A CANETA: ");
		System.out.println("Modelo: " + this.getModelo());
		System.out.println("Ponta: " + this.getPonta());
		System.out.println("Cor: " + this.getCor());
		System.out.println("Tampada: " + this.isTampada() + "\r\n");
	}
}
