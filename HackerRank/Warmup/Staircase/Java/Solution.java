import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    /*
     * Complete the staircase function below.
     */
    static void staircase(int n) {
        String spaces, hashes = "";
        for (int i = 1; i <= n; i++) {
            spaces = "";
            hashes += "#";
            for (int j = n; j > i; j--)
                spaces += " ";
            System.out.println(spaces + hashes);
        }

    }

    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) {
        int n = Integer.parseInt(scan.nextLine().trim());

        staircase(n);
    }
}
