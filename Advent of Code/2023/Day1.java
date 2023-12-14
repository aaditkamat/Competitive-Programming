import java.util.List;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.ArrayList;
import java.io.File;

public class Day1 {
    public static void main(String[] args) {
        try {
            part1();
            part2();
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }

    /*
     * Process each line as characters, filter out those corresponding to digits
     *, and get the number formed by the first and last digits within the line. 
     * If there is only 1 digit in the line, then use that digit twice.
     * That is the calibration value.
     */
    private static Integer processLinePart1(String line) {
        List<Character> tokens = new ArrayList<Character>();
        for (int i = 0; i < line.length(); i++) {
            char ch = line.charAt(i);
            if (ch >= '0' && ch <= '9') {
                tokens.add(ch);
            }
        }
        if (line.length() > 1) {
            return Integer.parseInt("" + tokens.get(0) + tokens.get(tokens.size() - 1));
        } else {
            return Integer.parseInt("" + tokens.get(0) + tokens.get(0));
        }
    }

    /*
     * Process each line using regular expressions and modify words to respective digits.
     * Get the number formed by the first and last digits within the line as in part 1. 
     * If there is only 1 digit in the line, then use that digit twice.
     * That is the calibration value.
     */
    private static Integer processLinePart2(String line) {
        Pattern pattern = Pattern.compile("(one|two|three|four|five|six|seven|eight|nine|\\d)");
        Matcher m = pattern.matcher(line);
        List<String> groups = new ArrayList<String>();
        while(m.find()) {
            String group = m.group(1);
            if (Pattern.compile("\\d").matcher(group).matches()) {
                groups.add(group);
            } else {
                switch(group) {
                    case "one": groups.add("1");
                                break;
                    case "two": groups.add("2");
                                break;
                    case "three": groups.add("3");
                                break;
                    case "four": groups.add("4");
                                break;
                    case "five": groups.add("5");
                                break;
                    case "six": groups.add("6");
                                break;
                    case "seven": groups.add("7");
                                break;
                    case "eight": groups.add("8");
                                break;
                    case "nine": groups.add("9");
                                break;                    
                }
            }
        }
        if (line.length() > 1) {
            return Integer.parseInt("" + groups.get(0) + groups.get(groups.size() - 1));
        } else {
            return Integer.parseInt("" + groups.get(0) + groups.get(0));
        }
    }

    public static void part1() throws Exception {
        Scanner sc = new Scanner(new File("test.in"));
        int sum = 0;
        while(sc.hasNextLine()) {
            String line = sc.nextLine();
            int calibrationValue = processLinePart1(line);
            sum += calibrationValue;
        }
        sc.close();
        System.out.println(sum);
    }

     public static void part2() throws Exception {
         Scanner sc = new Scanner(new File("test.in"));
         int sum = 0;
        
        while(sc.hasNextLine()) {
             String line = sc.nextLine();
             int calibrationValue = processLinePart2(line);
             sum += calibrationValue;
         }
         sc.close();
         System.out.println(sum);
     }
}
