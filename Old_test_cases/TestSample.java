/**
 * This is a file level Javadoc comment
 * Total Javadoc comments: 3
 * Total classes: 2 (1 main + 1 inner)
 * Total methods: 4
 * Total variables: 6
 * Total comments: 5
 * Total keywords used: 15 (public, class, private, static, void, int, double, String, final, if, else, for, return, new, package)
 * Total identifiers: 10
 * Total literals: 7
 */

public class TestSample {
    // Class level constants and variables
    private static final int MAX_VALUE = 1000;
    private String message = "Java Test Sample";
    private double[] numbers = {1.0, 2.0, 3.0, 4.0, 5.0};

    /**
     * Inner class demonstration
     */
    private class InnerCalculator {
        private double multiplier;

        public InnerCalculator(double multiplier) {
            this.multiplier = multiplier;
        }

        public double calculate(double input) {
            return input * multiplier;
        }
    }

    /**
     * Method to process array of numbers
     * @param input array to process
     * @return sum of processed numbers
     */
    public double processNumbers(double[] input) {
        InnerCalculator calc = new InnerCalculator(2.5);
        double sum = 0.0;
        
        // Process each number
        for (double num : input) {
            if (num > 0) {
                sum += calc.calculate(num);
            } else {
                sum += num;
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        TestSample sample = new TestSample();
        double result = sample.processNumbers(sample.numbers);
        System.out.println("Result: " + result);
    }
} 