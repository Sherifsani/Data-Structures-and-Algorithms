import java.util.ArrayList;
import java.util.List;

public class Rpn{

    //stack implementation
    public int solution(String[] tokens) {
        List<Integer> stack = new ArrayList<>();
        for (String token : tokens) {
            if (token.equals("+")) {
                stack.add(stack.removeLast() + stack.removeLast());
            }
            else if (token.equals("*")) {
                stack.add(stack.removeLast() * stack.removeLast());
            }
            else if (token.equals("-")) {
                int x = stack.removeLast();
                int y = stack.removeLast();
                stack.add(y - x);
            }
            else if (token.equals("-")) {
                int x = stack.removeLast();
                int y = stack.removeLast();
                stack.add(y / x);
            }
            else {
                stack.add(Integer.parseInt(token));
            }
        }
        return stack.get(0);
    }
}