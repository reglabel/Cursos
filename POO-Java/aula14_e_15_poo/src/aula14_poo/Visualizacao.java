package aula14_poo;

public class Visualizacao {
	private Gafanhoto espectador;
	private Video filme;
	
	public Visualizacao(Gafanhoto espectador, Video filme) {
		this.espectador = espectador;
		this.filme = filme;
		espectador.setTotAssistido(espectador.getTotAssistido() + 1);
		filme.setViews(filme.getViews() + 1);
	}
	
	@Override
	public String toString() {
		return "\r\n\t=-=- VISUALIZAÇÃO -=-=-\r\n** Video: \t" + filme.toString() +
				"\r\n** Espectador: \t" + espectador.toString() + "\r\n";
	}

	public void avaliar() {
		filme.setAvaliacao(5);
	}
	
	public void avaliar(int nota) {
		filme.setAvaliacao(nota);
	}
	
	public void avaliar(float porc) {
		int tot = 0;
		if (porc <= 20) {
			tot = 3;
		} else if (porc <= 50) {
			tot = 5;
		} else if (porc <= 90) {
			tot = 8;
		} else {
			tot = 10;
		}
		filme.setAvaliacao(tot);
	}
}
