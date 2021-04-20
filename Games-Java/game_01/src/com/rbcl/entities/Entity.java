package com.rbcl.entities;

//import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;
import java.awt.image.BufferedImage;

import com.rbcl.main.Game;
import com.rbcl.world.Camera;

public class Entity {
	
	public static BufferedImage LIFEPACK_EN = Game.spritesheet.getSprite(96, 0, 16, 16);
	public static BufferedImage WEAPON_EN = Game.spritesheet.getSprite(128, 0, 16, 16);
	public static BufferedImage AMMOPACK_EN = Game.spritesheet.getSprite(96, 16, 16, 16);
	public static BufferedImage ENEMY_EN = Game.spritesheet.getSprite(112, 16, 16, 16);
	public static BufferedImage ENEMY_FEEDBACK = Game.spritesheet.getSprite(112, 32, 16, 16);

	public static BufferedImage WEAPON_UP = Game.spritesheet.getSprite(144, 32, 16, 16);
	public static BufferedImage WEAPON_DOWN = Game.spritesheet.getSprite(144, 16, 16, 16);
	public static BufferedImage WEAPON_LEFT = Game.spritesheet.getSprite(128, 32, 16, 16);
	public static BufferedImage WEAPON_RIGHT = Game.spritesheet.getSprite(144, 0, 16, 16);

	protected double x, y;
	protected int z;
	protected int width, height;
	protected int maskx, masky, mwidth, mheight;
	protected int frames, maxFrames, index, maxIndex;
	
	private BufferedImage sprite;

	public Entity(int x, int y, int width, int height, BufferedImage sprite) {
		this.x = x;
		this.y = y;
		this.width = width;
		this.height = height;
		this.sprite = sprite;
		
		this.maskx = 0;
		this.masky = 0;
		this.mwidth = width;
		this.mheight = height;
	}
	
	public void setMask(int maskx, int masky, int mwidth, int mheight) {
		this.maskx = maskx;
		this.masky = masky;
		this.mwidth = mwidth;
		this.mheight = mheight;
	}
	
	public void setX(int newX) {
		this.x = newX;
	}
	
	public void setY(int newY) {
		this.y = newY;
	}
	
	public void render(Graphics g) {
		g.drawImage(sprite, this.getX() - Camera.getX(), this.getY() - Camera.getY(), null);
		//g.setColor(Color.BLACK);
		//g.fillRect(this.getX()+maskx - Camera.getX(), this.getY()+masky-Camera.getY(), mwidth, mheight);
	}

	public void tick() {
		
	}
	
	public void setSeqAnimation(int frames, int maxFrames, int index, int maxIndex) {
		this.frames = frames;
		this.maxFrames = maxFrames;
		this.index = index;
		this.maxIndex = maxIndex;
	}
	
	protected void animar() {
		frames++;
		if(frames == maxFrames) {
			frames = 0;
			index++;
			if(index > maxIndex) {
				index = 0;
			}
		}
	}
	
	public static boolean isColliding(Entity e1, Entity e2) {
		Rectangle e1Mask = new Rectangle(e1.getX()+e1.maskx, e1.getY()+e1.masky, e1.mwidth, e1.mheight);
		Rectangle e2Mask = new Rectangle(e2.getX()+e2.maskx, e2.getY()+e2.masky, e2.mwidth, e2.mheight);

		if(e1Mask.intersects(e2Mask) && e1.z == e2.z) {
			return true;
		}
		return false;
	}
	
	public int getX() {
		return (int)this.x;
	}

	public int getY() {
		return (int)this.y;
	}

	public int getWidth() {
		return width;
	}

	public int getHeight() {
		return height;
	}
	
}
