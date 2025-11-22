public class MathFunction {
    public Functions function;
    public long argument;

    public MathFunction(Functions function, long argument) {
        this.function = function;
        this.argument = argument;
    }

    public double getValue() {
        switch (function) {
            case SIN:
                return Math.sin(argument);
        }
    return 0;
    }
}
