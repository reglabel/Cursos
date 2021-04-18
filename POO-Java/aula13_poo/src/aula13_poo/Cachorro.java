package aula13_poo;

public class Cachorro extends Lobo {

	public Cachorro(String corPelo, float peso, int idade, int membros) {
		super(corPelo, peso, idade, membros);
	}

	@Override
	public void emitirSom() {
		System.out.println("Au! Au! Au!");
	}
	
	@Override
	public String toString() {
		return "\r\n--- Cachorro ---\r\n-> Peso: " + peso +
				"\r\n-> Idade: " + idade +
				"\r\n-> Membros: " + membros +
				"\r\n-> CorPelo: " + corPelo + "\r\n";
	}
	
	public void reagir(String frase) {
		if(frase.equals("toma comida") || frase.equals("ola")) {
			System.out.println("\r\nGostou da frase! Abanou e latiu!");
		} else {
			System.out.println("\r\nNão gostou da frase! Rosnou!");
		}
	}
	
	public void reagir(int hora, int min) {
		if(hora < 12) {
			System.out.println("\r\nHorário agradável! Abanou!");
		} else if (hora >= 18) {
			System.out.println("\r\nMuito tarde! Ignorou!");
		} else {
			System.out.println("\r\nHora da agitação! Abanou e latiu!");
		}
	}
	
	public void reagir(boolean dono) {
		if (dono) {
			System.out.println("\r\nÉ você! Ele te ama! Abanou!");
		} else {
			System.out.println("\r\nNunca nem vi! Rosnou e latiu!");
		}
	}
	
	public void reagir(int idade, float peso) {
		if(idade < 5) {
			if (peso < 10) {
				System.out.println("\r\nSou novo e leve! Abanou!");
			} else {
				System.out.println("\r\nSou novo e pesado! Latiu!");
			}
		} else {
			if (peso < 10) {
				System.out.println("\r\nSou velho e leve! Rosnou!");
			} else {
				System.out.println("\r\nSou velho e pesado! Ignorou!");
			}
		}
	}
}
