public class ScientificCalculator {
    public static void main(String args[]) {
        if(args.length == 1) {
            Parser parser = new Parser(args[0]);
            MathFunction mathFunction = new MathFunction(
                    parser.getFunction(),
                    parser.getArgument());
            System.out.println(mathFunction.function + "(" +
                    mathFunction.argument + ")" + 
                    " = " + mathFunction.getValue());
            
        } else if (args.length == 3) {
        } else {
            System.out.println("Usage examples:");
            System.out.println("java ScientificCalculator \"sin(3)\"");
            System.out.println("java ScientificCalculator \"cos(1)\"");
            System.out.println("java ScientificCalculator \"sqrt(9)\"");
            System.out.println("java ScientificCalculator \"2 + 2\"");
            System.out.println("java ScientificCalculator \"tan(4) / 2\"");
            System.out.println("java ScientificCalculator \"log(5) x ln(6)\"");
            System.out.println("java ScientificCalculator \"exp(5) - e^2\"");
        }
    }
}
