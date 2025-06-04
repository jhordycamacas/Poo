package com.mycompany.practica;

public class Perro extends Animal {

    String raza;



    public Perro(String tipo, int edad, String raza) {
        super(tipo, edad);

        this.raza = raza;
    }

    public void ladrar() {
        System.out.println("Guau guau - Soy un " + raza);

    }

    public void vacunas() {
        if (edad <= 3) {
            System.out.println("Su perro necesita 4 vacunas");
        } else {
            System.out.println("Su perro necesita 7 vacunas");

        }

    }
}
