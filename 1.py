import stylecloud

words = [
    '樱桃', '樱桃', '樱桃', '樱桃', '樱桃', '樱桃', '樱桃', '樱桃', '芒果', '芒果', '芒果', '芒果',
    '芒果', '芒果', '桃子', '桃子', '苹果', '枣子', '榴莲', '葡萄', '柠檬', '荔枝', '芒果', '橄榄',
    '橘子', '桃子', '柚子', '菠萝', '核桃'
]

stylecloud.gen_stylecloud(' '.join(words),
                          font_path='data/HanYiKaiTiJian.ttf',
                          output_name='data/2.png',
                          custom_stopwords=['芒果'],
                          icon_name='fas fa-square')
