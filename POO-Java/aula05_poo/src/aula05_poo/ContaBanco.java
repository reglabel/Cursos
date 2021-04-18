package aula05_poo;

//import java.util.Scanner;

public class ContaBanco {
	public int numConta;
	protected String tipo;
	private String dono;
	private double saldo;
	private boolean status;
	
	public ContaBanco() {
		this.setStatus(false);
		this.setSaldo(0);
	}
	
	/*
	public ContaBanco(int numConta, String tipo, String dono) {
		this.setStatus(false);
		this.setDono(dono);
		
		while (!tipo.contentEquals("cc") & !tipo.contentEquals("cp")) {
			Scanner ler = new Scanner(System.in);
			System.out.print("O tipo da conta deve ser 'cc' ou 'cp'. \r\nDigite uma opção válida: ");
			tipo = ler.nextLine();
			
			if(tipo.contentEquals("cc") || tipo.contentEquals("cp")) {
				ler.close();
			}
		}
		
		if (tipo.contentEquals("cc")) {
			this.setSaldo(50);
		} else {
			this.setSaldo(150);
		}
		
		this.setTipo(tipo);
		this.setNumConta(numConta);
	}
	*/
	
	public void abrirConta(String tipo) {
		this.setTipo(tipo);
		if (this.getTipo().contentEquals("cc") || this.getTipo().contentEquals("cp")) {
			this.setStatus(true);
			System.out.println("\r\nConta de " + this.getDono() + " aberta com SUCESSO!");
			if (this.getTipo().contentEquals("cc")) {
				this.setSaldo(50);
			} else {
				this.setSaldo(150);
			}
		} else {
			System.out.println("\r\nDefina um tipo válido para abrir conta de " + this.getDono() + ".");
		}
		
	}
	
	public void fecharConta() {
		if (this.getSaldo() == 0) {
			System.out.println("\r\nConta de " + this.getDono() + " fechada com SUCESSO!");
			this.setStatus(false);
		} else if (this.getSaldo() > 0){
			System.out.println("\r\nSaldo " + this.getDono() + " POSITIVO.\r\nZere seu saldo para poder encerrar a conta.");
		} else {
			System.out.println("\r\nSaldo " + this.getDono() + " NEGATIVO.\r\nRegularize seu saldo para poder encerrar a conta.");
		}
	}
	
	public void depositar(double valor) {
		if (this.isStatus()) {
			this.setSaldo(this.getSaldo() + valor);
			System.out.println("\r\nDepósito de " + this.getDono() + " efetuado com SUCESSO!");
		} else {
			System.out.println("\r\nNecessário abrir a conta de " + this.getDono() + " para realizar esta operação.");
		}
	}
	
	public void sacar(double valor) {
		if (this.isStatus()) {
			if (this.getSaldo() >= valor) {
				this.setSaldo(this.getSaldo() - valor);
				System.out.println("\r\nSaque de " + this.getDono() + " efetuado com SUCESSO!");
			} else {
				System.out.println("\r\nSaldo de " + this.getDono() + " insuficiente para realizar esta operação.");
			}
		} else {
			System.out.println("\r\nNecessário abrir a conta de" + this.getDono() + " para realizar esta operação.");
		}
	}
	
	public void pagarMensal() {
		if (this.isStatus()) {
			if (this.tipo.contentEquals("cc")) {
				if (this.getSaldo() >= 12.0) {
					System.out.println("\r\nPagamento de " + this.getDono() + " efetuado com SUCESSO!");
					this.setSaldo(this.getSaldo() - 12.0);
				} else {
					System.out.println("\r\nSaldo de " + this.getDono() + " insuficiente para realizar tal operação.");
				}
			} else if (this.tipo.contentEquals("cp")) {
				if (this.getSaldo() >= 20.0) {
					System.out.println("\r\nPagamento de " + this.getDono() + " efetuado com SUCESSO!");
					this.setSaldo(this.getSaldo() - 20.0);
				} else {
					System.out.println("\r\nSaldo de " + this.getDono() + " insuficiente para realizar tal operação.");
				}
			}
		} else {
			System.out.println("\r\nNecessário abrir a conta de " + this.getDono() + " para realizar esta operação.");
		}
	}
	
	public int getNumConta() {
		return numConta;
	}
	
	public void setNumConta(int numConta) {
		this.numConta = numConta;
	}
	
	public String getTipo() {
		return tipo;
	}
	
	public void setTipo(String tipo) {
		this.tipo = tipo;
	}
	
	public String getDono() {
		return dono;
	}
	
	public void setDono(String dono) {
		this.dono = dono;
	}
	
	public double getSaldo() {
		return saldo;
	}
	
	public void setSaldo(double saldo) {
		this.saldo = saldo;
	}
	
	public boolean isStatus() {
		return status;
	}
	
	public void setStatus(boolean status) {
		this.status = status;
	}
	
	public void perfil() {
		System.out.println("\r\nPERFIL DA CONTA: ");
		System.out.println("Número: " + this.getNumConta());
		System.out.println("Tipo: " + this.getTipo());
		System.out.println("Dono: " + this.getDono());
		System.out.println("Saldo: R$" + this.getSaldo());
		System.out.println("Status: " + this.isStatus());
	}
}
