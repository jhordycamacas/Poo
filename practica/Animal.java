package com.mycompany.practica;

import java.util.Scanner;

public class Animal {

    String tipo;
    int edad;


    public Animal(String tipo, int edad) {
        this.tipo = tipo;
        this.edad = edad;
}

    public void describir() {
        System.out.println("Tipo: " + tipo);

    }

    public void calcularEdad() {
        String tamano = "";
        if (edad <= 3) {
            tamano = "Cachorro";
        } else if (edad > 3) {
            tamano = "Adulto";
        }
        System.out.println("Su perro es un " + tamano);

    }
    

}
