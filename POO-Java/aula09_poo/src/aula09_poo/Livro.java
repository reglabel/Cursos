package aula09_poo;

public class Livro implements Publicacao {
	private String titulo;
	private String autor;
	private int totPaginas;
	private int pagAtual;
	private boolean aberto;
	private Pessoa leitor;
	
	public Livro(String titulo, String autor, int totPaginas, Pessoa leitor) {
		this.titulo = titulo;
		this.autor = autor;
		this.aberto = false;
		this.pagAtual = 0;
		this.totPaginas = totPaginas;
		this.leitor = leitor;
	}

	public String detalhes() {
		return "\t--- Livro ---\r\n-> Titulo: " + titulo +
				"\r\n-> Autor: " + autor +
				"\r\n-> TotPaginas: " + totPaginas +
				"\r\n-> PagAtual: " + pagAtual +
				"\r\n-> Aberto: " + aberto +
				"\r\n-> Leitor: " + leitor.getNome() +
				"\r\n-> Sexo: " + leitor.getSexo() + "\r\n";
	}


	@Override
	public void abrir() {
		if(!(this.isAberto())){
			this.setAberto(true);
		}
	}

	@Override
	public void fechar() {
		if(this.isAberto()) {
			this.setAberto(false);
		}
	}

	@Override
	public void folhear(int p) {
		if(this.isAberto()) {
			if(p > this.getTotPaginas()) {
				this.setPagAtual(0);
			} else {
				this.setPagAtual(p);
			}
		}
	}

	@Override
	public void avancarPag() {
		if (this.isAberto()) {
			if (this.getPagAtual() < this.getTotPaginas()) {
				this.setPagAtual(getPagAtual() + 1);
			}
		}
	}

	@Override
	public void voltarPag() {
		if (this.isAberto()) {
			if (this.getPagAtual() >= 1) {
				this.setPagAtual(getPagAtual() - 1);
			}
		}
	}

	private int getTotPaginas() {
		return totPaginas;
	}

	private int getPagAtual() {
		return pagAtual;
	}

	private void setPagAtual(int pagAtual) {
		this.pagAtual = pagAtual;
	}

	private boolean isAberto() {
		return aberto;
	}

	private void setAberto(boolean aberto) {
		this.aberto = aberto;
	}
}
