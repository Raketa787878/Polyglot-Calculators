public class Parser {
    public String input;

    public Parser(String input) {
        this.input = input;
    }

    public Functions getFunction() {
        int openBracket = input.indexOf('(');
        String functionName = input.substring(0, openBracket).toUpperCase(); 
        return Functions.valueOf(functionName); 
    }

    public long getArgument() {
        int openBracket = input.indexOf('(');
        int closeBracket = input.indexOf(')');
        String functionArgument = input.substring(openBracket + 1, closeBracket);
        return Long.parseLong(functionArgument);
    }
}
