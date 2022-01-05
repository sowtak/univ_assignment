import MeCab

mecab=MeCab.Tagger('-Ochasen')
mecab.parse('')
text_node=mecab.parseToNode(input())

while text_node:
    print(text_node.surface, text_node.feature)
    text_node=text_node.next


