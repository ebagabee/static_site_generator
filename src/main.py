from textnode import TextNode, TextType

def main():
    teste = TextNode("This is some anchor text", TextType.TEXT, "https://www.boot.dev")
    print(teste)
main()