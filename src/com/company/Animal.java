package com.company;

public class Animal implements Talking{
   private String name;
   private  int age;

   public Animal(String name, int age) {
       this.name = name;
       this.age = age;
   }
    @Override
    public void say(){
       System.out.println("this animal name is " + name);
       System.out.println(String.format("this animal age is %d", age));
    }
}
