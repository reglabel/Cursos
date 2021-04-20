package com.rbcl.entities;

//import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;
import java.awt.image.BufferedImage;

import com.rbcl.main.Game;
import com.rbcl.main.Sound;
import com.rbcl.world.Camera;
import com.rbcl.world.World;

public class Enemy extends Entity{

	private double speed;
	private BufferedImage[] sprites = new BufferedImage[2];
	private double life = 10;
	private boolean isDamaged = false;
	private int damagedFrames = 10, currentFrame = 0;
	
	public Enemy(int x, int y, int width, int height, BufferedImage sprite) {
		super(x, y, width, height, null);
				
		sprites[0] = Game.spritesheet.getSprite(112, 16, 16, 16);
		sprites[1] = Game.spritesheet.getSprite(128, 16, 16, 16);
		
		setMask(3,3,10,10);

		this.speed = 0.3;
		setSeqAnimation(0,10,0,1);
	}
	
	public void tick() {
		int xDoPlayer = Game.player.getX();
		int yDoPlayer = Game.player.getY();
		int xDoEnemy = this.getX();
		int yDoEnemy = this.getY();
		int subir = (int) (y - speed);
		int descer = (int) (y + speed);
		int direita = (int) (x + speed);
		int esquerda = (int) (x - speed);
		
		if(!(this.isCollindingWithPlayer())) {
			if(xDoEnemy < xDoPlayer &&
					World.isFree(direita, yDoEnemy) && 
					!(isColliding(direita, yDoEnemy))) {
				x += speed;
			} else if (xDoEnemy > xDoPlayer &&
					World.isFree(esquerda, yDoEnemy) && 
					!(isColliding(esquerda, yDoEnemy))){
				x -= speed;
			}
			
			else if(yDoEnemy < yDoPlayer &&
					World.isFree(xDoEnemy, descer) && 
					!(isColliding(xDoEnemy, descer))) {
				y += speed;
			} else if (yDoEnemy > yDoPlayer &&
					World.isFree(xDoEnemy, subir) && 
					!(isColliding(xDoEnemy, subir))){
				y -= speed;
			}
		} else {
			if(Game.rand.nextInt(100) < 10) {
				Sound.hurtPlayer.play();
				Game.player.life -= Game.rand.nextInt(10);
				Game.player.isDamaged = true;
			}
		}
		
		animar();
		
		collidingShoot();
		
		if(life <= 0) {
			Sound.deathEnemy.play();
			destroySelf();
			return;
		}
		
		if(isDamaged) {
			currentFrame++;
			if(currentFrame == damagedFrames) {
				currentFrame = 0;
				isDamaged = false;
			}
		}
	}
	
	public void destroySelf() {
		Game.entities.remove(this);
		Game.enemies.remove(this);
	}
	
	public void collidingShoot() {
		for(int i = 0; i < Game.weaponShoots.size(); i++) {
			Entity e =Game.weaponShoots.get(i);
			if(Entity.isColliding(this, e)) {
				Sound.hurtEnemy.play();
				isDamaged = true;
				life = life - 2;
				Game.weaponShoots.remove(e);
				return;
			}
		}
	}
	
	public boolean isCollindingWithPlayer() {
		Rectangle currentEnemy = new Rectangle(this.getX() + maskx, this.getY() + masky, mwidth, mheight);
		Rectangle player = new Rectangle(Game.player.getX(), Game.player.getY(), 16, 16);
		
		return currentEnemy.intersects(player);
	}
	
	public boolean isColliding(int xNext, int yNext) {
		Rectangle currentEnemy = new Rectangle(xNext + maskx, yNext + masky, mwidth, mheight);
		for(int i = 0; i < Game.enemies.size(); i++) {
			Enemy en = Game.enemies.get(i);
			if(en == this) {
				continue;
			}
			
			Rectangle targetEnemy = new Rectangle(en.getX() + maskx, en.getY() + masky, mwidth, mheight);
			if(currentEnemy.intersects(targetEnemy)) {
				return true;
			}
		}
		
		return false;
	}
	
	public void render(Graphics g) {
		if(!isDamaged) {
			g.drawImage(sprites[index], this.getX() - Camera.getX(), this.getY() - Camera.getY(), null);
		} else {
			g.drawImage(Entity.ENEMY_FEEDBACK, this.getX() - Camera.getX(), this.getY() - Camera.getY(), null);
		}
	}
	
}
