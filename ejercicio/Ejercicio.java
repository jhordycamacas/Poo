/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.ejercicio;

/*Este es el main en el que se envian los datos, en este apartado se quema el dato del porcentaje puede ser 5 o 7*/
public class Ejercicio {

    public static void main(String[] args) {
        Metodos metodos = new Metodos();
        metodos.leerDatos();
        Cta_Ahorro t = new Cta_Ahorro(metodos.getNombre(), metodos.getSaldo(), 5);
        t.mostrarTitular();
        t.mostrarSaldo();
        t.tipo_interes();
    }
}
