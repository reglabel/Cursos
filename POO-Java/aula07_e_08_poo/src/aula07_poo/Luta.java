package aula07_poo;

public class Luta {
	private Lutador desafiado;
	private Lutador desafiante;
	//private int rounds;
 	private boolean aprovada;
	
	public void marcarLuta(Lutador desafiante, Lutador desafiado) {
		if (desafiante.getCategoria().equals(desafiado.getCategoria()) && !(desafiado.equals(desafiante))) {
			this.setAprovada(true);
			this.setDesafiante(desafiante);
			this.setDesafiado(desafiado);
		} else {
			this.setAprovada(false);
			this.setDesafiado(null);
			this.setDesafiante(null);
		}
	}
	
	public int lutar() {
		int resultado = -1;
		if (this.isAprovada()) {
			System.out.println("\r\n\t### DESAFIANTE ###");
			desafiante.apresentar();
			System.out.println("\r\n\t### DESAFIADO ###");
			desafiado.apresentar();
			
			float valorDoDesafiante = desafiante.chanceDeVencer();
			float valorDoDesafiado = desafiado.chanceDeVencer();
			
			if(valorDoDesafiante > valorDoDesafiado) {
				resultado = 1;
				desafiante.ganharLuta();
				desafiado.perderLuta();
			} else if (valorDoDesafiante < valorDoDesafiado) {
				resultado = 2;
				desafiante.perderLuta();
				desafiado.ganharLuta();
			} else {
				resultado = 0;
				desafiante.empatarLuta();
				desafiado.empatarLuta();
			}
		} else {
			System.out.println("Essa luta não pode acontecer...");
		}
		return resultado;
	}
	
	public void resultado(int resultado, Lutador l1, Lutador l2) {
		if(aprovada) {
			System.out.println("\r\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-");
			switch(resultado) {
				case 0:
					System.out.println("A luta empatou!");
					break;
				case 1:
					System.out.println("VENCEDOR: " + l1.getNome());
					System.out.println("PERDEDOR: " + l2.getNome());
					break;
				case 2:
					System.out.println("VENCEDOR: " + l2.getNome());
					System.out.println("PERDEDOR: " + l1.getNome());
					break;
			}
			System.out.println("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-");
		}
	}
	
	public void placarzinho(Lutador a, Lutador b) {
		System.out.print("\r\n" + a.getNome() + ", peso " + a.getCategoria() + " VS ");
		System.out.println(b.getNome() + ", peso " + b.getCategoria() + "\r\n");
	}

	private void setDesafiado(Lutador desafiado) {
		this.desafiado = desafiado;
	}

	private void setDesafiante(Lutador desafiante) {
		this.desafiante = desafiante;
	}

	private boolean isAprovada() {
		return aprovada;
	}

	private void setAprovada(boolean aprovada) {
		this.aprovada = aprovada;
	}
}
