/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejercicio;

/*En esta clase es la clase hija o la subclase y en la cual tenemos especificamente el tipo de cuenta ahorro*/
public class Cta_Ahorro extends Cuenta {

    double saldo;
    int interes;

    public Cta_Ahorro(String titular, double saldo, int interes) {
        super(titular);
        this.saldo = saldo;
        this.interes = interes;
    }

    public void mostrarSaldo() {
        System.out.println("Su saldo es: " + saldo);

    }

    public void tipo_interes() {
        double calculo = 0;

        if (interes == 5) {
            calculo = saldo / 5;

        } else if (interes == 7) {
            calculo = saldo / 7;
        }
        double resultado = saldo + calculo;
        System.out.println("Porcentaje de interes: " + interes + "%");
        System.out.println("Su interes es de: " + calculo);
        System.out.println("Su saldo total con intereses seria de: " + resultado);
    }

}
