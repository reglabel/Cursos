package aula05_poo;

public class Principal {

	public static void main(String[] args) {
		ContaBanco p1 = new ContaBanco();
		ContaBanco p2 = new ContaBanco();
		
		p1.setNumConta(1111);
		p1.setDono("Jubileu");
		p1.abrirConta("cc");
		
		p2.setNumConta(2222);
		p2.setDono("Creuza");
		p2.abrirConta("cp");
		
		p1.depositar(100);
		p2.depositar(500);
		
		p2.sacar(100);
		p1.sacar(150);
		
		p1.fecharConta();
		
		p1.perfil();
		p2.perfil();
	}

}
