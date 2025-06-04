/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejercicio;

/*Esta es la clase padre de la que se va a heredar*/
public class Cuenta {

    String titular;

    public Cuenta(String titular) {
        this.titular = titular;
    }

    public void mostrarTitular() {
        System.out.println("El titular es: " + titular);

    }
}
