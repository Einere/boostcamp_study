package com.company.boostcamp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Q9012 {
    void main() {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int balance = 0;
        try {
            int instructions = Integer.parseInt(br.readLine());

            for (int i = 0; i < instructions; i++) {
                String instruction = br.readLine();

                for (int j = 0; j < instruction.length(); j++) {
                    if (instruction.charAt(j) == '(') {
                        balance++;
                    } else if (instruction.charAt(j) == ')') {
                        balance--;
                    }
                }

                if (balance == 0) System.out.println("YES");
                else System.out.println("NO");
                balance = 0;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
