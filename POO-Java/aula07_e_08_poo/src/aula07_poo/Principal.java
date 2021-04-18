package aula07_poo;

import java.util.Random;

public class Principal {

	public static void main(String[] args) {
		Random gerador = new Random();
		Luta uec = new Luta();
		Lutador[] l = new Lutador[6];
		
		l[0] = new Lutador("Pretty Boy",
				"França",
				31, 1.75f, 68.9f,
				11, 2, 1);
		
		l[1] = new Lutador("Putscript",
				"Brasil",
				29, 1.68f, 57.8f,
				14, 2, 3);
		
		l[2] = new Lutador("Snapshadow",
				"EUA",
				35, 1.65f, 80.9f,
				12, 2, 1);
		
		l[3] = new Lutador("Dead Code",
				"Austrália",
				28, 1.93f, 81.6f,
				13, 0, 2);
		
		l[4] = new Lutador("Ufocobol",
				"Brasil",
				37, 1.70f, 119.3f, 5, 4, 3);
		
		l[5] = new Lutador("Nerdaard",
				"EUA",
				30, 1.81f, 105.7f,
				12, 2, 4);
		
		boolean continuar = true;
		System.out.println("O UEC começou!");
		while(continuar) {
			Lutador lutador1 = l[gerador.nextInt(6)];
			Lutador lutador2 = l[gerador.nextInt(6)];
			
			uec.marcarLuta(lutador1, lutador2);
			uec.placarzinho(lutador1, lutador2);
			int resultado = uec.lutar();
			uec.resultado(resultado, lutador1, lutador2);
			
			if(gerador.nextInt(11) > 8) {
				continuar = false;
			} else {
				System.out.println("\r\nO UEC continua...");
			}
			
		}
		if(!continuar) {
			System.out.println("\r\nO UEC acabou...");
		}
		
	}

}
