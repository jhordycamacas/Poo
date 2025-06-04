/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejercicio;

import java.util.Scanner;
/*En esta clase se crea procesos para ingresar datos por teclado y enviarlos directamente desde el main*/
public class Metodos {

    String nombre;
    double saldo;

    public Metodos() {

    }

    public void leerDatos() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese el nombre del titular: ");
        nombre = sc.nextLine();
        System.out.println("Ingrese el sueldo: ");
        saldo = sc.nextDouble();
    }

    public String getNombre() {
        return nombre;
    }

    public double getSaldo() {
        return saldo;
    }

}
