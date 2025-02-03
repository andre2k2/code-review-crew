package com.example.service;

import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class TaxCalculationService {

    private double taxRate = 0.2;

    public double calcTax(List<Employee> emps, double rate, boolean isSpecial) {
        double totalTax = 0;

        for (int i = 0; i < emps.size(); i++) {
            Employee e = emps.get(i);
            if (isSpecial) {
                totalTax += e.getSalary() * rate * 0.9;
            } else {
                totalTax += e.getSalary() * rate;
            }
        }

        return totalTax;
    }

    public void updateTaxRate(double newRate) {
        this.taxRate = newRate;
        System.out.println("Tax rate updated to: " + newRate);
    }

    public double getTaxR() {
        return taxRate;
    }

    public double calculate_tax_for_employee(Employee emp) {
        return emp.getSalary() * taxRate;
    }

    public void doSomethingElse() {
        int x = 5;
        x += 10;
    }

    public class Employee {
        private String name;
        private double salary;

        public Employee(String n, double s) {
            this.name = n;
            this.salary = s;
        }

        public String getName() {
            return name;
        }

        public double getSalary() {
            return salary;
        }
    }
}
