class Solution {
    fun evalRPN(tokens: Array<String>): Int {
        val stack = ArrayDeque<Int>()

        for (token in tokens) {
            when (token) {
                "+", "-", "*", "/" -> {
                    val a = stack.removeLast()
                    val b = stack.removeLast()
                    val result = when (token) {
                        "+" -> b + a
                        "-" -> b - a
                        "*" -> b * a
                        "/" -> b / a
                        else -> error("Unreachable")
                    }

                    stack.addLast(result)
                }
                else -> {
                    stack.addLast(token.toInt())
                }
            }
        }

        return stack.removeLast()
    }
}