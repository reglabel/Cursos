package aula07_poo;

import java.util.Random;

public class Lutador {
	private String nome;
	private String nacionalidade;
	private int idade;
	private float altura;
	private float peso;
	private String categoria;
	private int vitorias;
	private int derrotas;
	private int empates;
	
	public Lutador(String no, String na, int id, float al, float pe, int vi, int de, int em) {
		this.nome = no;
		this.nacionalidade = na;
		this.idade = id;
		this.altura = al;
		this.setPeso(pe);
		this.setVitorias(vi);
		this.setDerrotas(de);
		this.setEmpates(em);
	}
	
	public void apresentar() {
		System.out.println("------------- GHEGOU A HORA!! -------------\r\nApresentamos o lutador: ");
		System.out.print(this.getNome() + ", diretamente de ");
		System.out.print(this.getNacionalidade() + "!!");
		System.out.print("\r\nCom " + this.getIdade() + " anos, ");
		System.out.print(this.getAltura() + "m de altura e pesando ");
		System.out.print(this.getPeso() + "kg!\r\nEsse lutador possui incríveis:\r\n");
		System.out.println("* " + this.getVitorias() + " vitória(s), ");
		System.out.println("** " + this.getDerrotas() + " derrota(s) e ");
		System.out.println("*** " + this.getEmpates() + " empate(s)!");
		System.out.println("Uma grande salva de palmas para ele!!");
		System.out.println("-----------------------------------------------");
	}

	public void status() {
		System.out.print("\r\n" + this.getNome());
		System.out.println(" é um peso " + this.getCategoria() + ".\r\nPossui: ");
		System.out.println("-> " + this.getVitorias() + " VITÓRIA(S)");
		System.out.println("-> " + this.getDerrotas() + " DERROTA(S)");
		System.out.println("-> " + this.getEmpates() + " EMPATE(S)");
	}
	
	public void ganharLuta() {
		this.setVitorias(this.getVitorias() + 1);
	}
	
	public void perderLuta() {
		this.setDerrotas(this.getDerrotas() + 1);
	}
	
	public void empatarLuta() {
		this.setEmpates(this.getEmpates() + 1);
	}
	
	public float chanceDeVencer() {
		Random gerador = new Random();
		int sorte = gerador.nextInt(11);
		float chance = (this.getAltura() * 1.5f) + 
				(this.getPeso() * 2.0f) +
				(this.getVitorias() * 2.5f) + 
				(sorte * 0.5f) +
				(this.getEmpates() * 1.0f) -
				(this.getDerrotas() * 2.5f);
		chance /= 10.0f;
		return chance;
	}
	
	public String getNome() {
		return nome;
	}

	public String getNacionalidade() {
		return nacionalidade;
	}

	public int getIdade() {
		return idade;
	}

	public float getAltura() {
		return altura;
	}
	
	public float getPeso() {
		return peso;
	}
	
	private void setPeso(float peso) {
		if (peso > 0) {
			this.peso = peso;
		} else {
			this.peso = 0f;
		}
		this.setCategoria();
	}

	public String getCategoria() {
		return categoria;
	}

	private void setCategoria() {
		if (this.peso < 52.2f) {
			this.categoria = "Inválido";
		} else if (this.peso <= 70.3f) {
			this.categoria = "Leve";
		} else if (this.peso <= 83.9f) {
			this.categoria = "Médio";
		} else if (this.peso <= 120.2f) {
			this.categoria = "Pesado";
		} else {
			this.categoria = "Inválido";
		}
	}

	public int getVitorias() {
		return vitorias;
	}

	private void setVitorias(int vitorias) {
		if (vitorias >= 0) {
			this.vitorias = vitorias;
		} else {
			this.vitorias = 0;
		}
	}

	public int getDerrotas() {
		return derrotas;
	}

	private void setDerrotas(int derrotas) {
		if (derrotas >= 0) {
			this.derrotas = derrotas;
		} else {
			this.derrotas = 0;
		}
	}

	public int getEmpates() {
		return empates;
	}

	private void setEmpates(int empates) {
		if (empates >= 0) {
			this.empates = empates;
		} else {
			this.empates = 0;
		}
	}
}
