package aula14_poo;

public class Video implements AcoesVideo {
	private String titulo;
	private int avaliacao;
	private int views;
	private int curtidas;
	private boolean reproduzindo;

	public Video(String titulo) {
		this.titulo = titulo;
		avaliacao = 1;
		views = 0;
		curtidas = 0;
		reproduzindo = false;
	}

	@Override
	public String toString() {
		return "\r\n\t--- Video ---\r\n-> Titulo: " + titulo +
				"\r\n-> Avaliacao: " + avaliacao +
				"\r\n-> Views: " + views +
				"\r\n-> Curtidas: " + curtidas +
				"\r\n-> Reproduzindo: " + reproduzindo + "\r\n";
	}

	@Override
	public void play() {
		setReproduzindo(true);
	}

	@Override
	public void pause() {
		setReproduzindo(false);
	}

	@Override
	public void like() {
		setCurtidas(getCurtidas() + 1);
	}

	public void setAvaliacao(int avaliacao) {
		int nova;
		nova = (this.avaliacao + avaliacao) / views;
		this.avaliacao = nova;
	}

	public int getViews() {
		return views;
	}

	public void setViews(int views) {
		this.views = views;
	}

	private int getCurtidas() {
		return curtidas;
	}

	private void setCurtidas(int curtidas) {
		this.curtidas = curtidas;
	}

	private void setReproduzindo(boolean reproduzindo) {
		this.reproduzindo = reproduzindo;
	}

}
