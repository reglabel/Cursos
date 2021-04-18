package aula06_poo;

public class Principal {

	public static void main(String[] args) {
		Controlador c = new ControleRemoto();
		
		c.ligar();
		c.abrirMenu();
		c.maisVolume();
		c.abrirMenu();
		c.ligarMudo();
		c.abrirMenu();
		c.fecharMenu();
		
	}

}
