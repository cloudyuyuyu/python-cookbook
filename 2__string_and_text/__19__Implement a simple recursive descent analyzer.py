from util.separator import separator_content

if __name__ == "__main__":
    """
    问题
        你想根据一组语法规则解析文本并执行命令，或者构造一个代表输入的抽象语法树。 
        
        如果语法非常简单，你可以不去使用一些框架，而是自己写这个解析器。

    解决方案
        在这个问题中，我们集中讨论根据特殊语法去解析文本的问题。 
        
        为了这样做，你首先要以 BNF 或者 EBNF 形式指定一个标准语法。
        
        比如，一个简单数学表达式语法可能像下面这样：
        expr ::= expr + term
             |   expr - term
             |   term

        term ::= term * factor
             |   term / factor
             |   factor

        factor ::= ( expr )
             |   NUM
             
             
        或者，以EBNF形式：
        expr ::= term { (+|-) term }*

        term ::= factor { (*|/) factor }*

        factor ::= ( expr )
               |   NUM
    """
    separator_content()