package aula12_poo;

public class Principal {

	public static void main(String[] args) {
		//Animal n = new Animal();
		Mamifero m = new Mamifero("Marrom", 12.5f, 9, 4);
		Reptil r = new Reptil("Verde Neon", 20f, 13, 6);
		Peixe p = new Peixe("Rosa Choque", 3f, 2, 0);
		Ave a = new Ave("Amarela", 2f, 5, 2);
		
		System.out.println(m.toString());
		m.locomover();
		m.alimentar();
		m.emitirSom();
		
		System.out.println(r.toString());
		r.locomover();
		r.alimentar();
		r.emitirSom();
		
		System.out.println(p.toString());	
		p.locomover();
		p.alimentar();
		p.emitirSom();
		
		System.out.println(a.toString());	
		a.locomover();
		a.alimentar();
		a.emitirSom();
		
		Cachorro ca = new Cachorro("Preto", 5f, 5, 4);
		Canguru gu = new Canguru("Marrom", 20.6f, 6, 4);
		Tartaruga ta = new Tartaruga("Verde", 10f, 50, 4);
		Cobra co = new Cobra("Vermelha", 0.9f, 9, 0);
		Goldfish go = new Goldfish("Gold", 0.1f, 4, 0);
		Arara ara = new Arara("Azul", 1.1f, 30, 2);
	
		System.out.println(ca.toString("Cachorro"));
		ca.locomover();
		ca.alimentar();
		ca.emitirSom();
		ca.enterrarOsso();
		ca.abanarRabo();
		
		System.out.println(gu.toString("Canguru"));
		gu.locomover();
		gu.alimentar();
		gu.emitirSom();
		gu.usarBolsa();
		
		System.out.println(ta.toString("Tartaruga"));	
		ta.locomover();
		ta.alimentar();
		ta.emitirSom();
		
		System.out.println(co.toString("Cobra"));	
		co.locomover();
		co.alimentar();
		co.emitirSom();
		
		System.out.println(go.toString("Goldfish"));
		go.locomover();
		go.alimentar();
		go.emitirSom();
		
		System.out.println(ara.toString("Arara"));
		ara.locomover();
		ara.alimentar();
		ara.emitirSom();
	}
}
