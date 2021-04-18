package aula14_poo;

public class Main {

	public static void main(String[] args) {
		Video v[] = new Video[3];
		
		v[0] = new Video("Phanton Blood Opening");
		v[1] = new Video("Battle Tendency Opening");
		v[2] = new Video("Stardust Crusaders Opening");
		
		/*
		System.out.println("\t -=-= NOSSAS OBRAS DE ARTE =-=-");
		for(Video i: v) {
			System.out.println(i.toString());
		}
		*/

		Gafanhoto g[] = new Gafanhoto[2];
		
		g[0] = new Gafanhoto("Jonathan", 20, "M", "best_boi_1");
		g[1] = new Gafanhoto("Joseph", 19, "M", "outsmarting_dude_2");
	
		/*
		System.out.println("\t -=-= NOSSOS BOYS =-=-");
		for(Gafanhoto i: g) {
			System.out.println(i.toString());
		}
		*/
		
		Visualizacao vis[] = new Visualizacao[4];
		
		vis[0] = new Visualizacao(g[0], v[0]); // Jonathan vê Op 1
		vis[0].avaliar(10);
		
		vis[1] = new Visualizacao(g[1], v[0]); // Joseph vê Op 1
		vis[1].avaliar();
		
		vis[2] = new Visualizacao(g[0], v[1]); // Jonathan vê Op 2
		vis[2].avaliar(7);
		
		vis[3] = new Visualizacao(g[1], v[1]); // Joseph vê Op 2
		vis[3].avaliar(100f);
		
		/*
		for(Visualizacao i: vis) {
			System.out.println(i.toString());
		}
		*/
	}
}
