import gensim, logging
import json
import os

data_path = '../data/demo/train_embeddings'
save_path = '../data/demo/embeddings.txt'

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            f = open(os.path.join(self.dirname, fname),encoding='utf-8')
            for line in f:
                contents = json.loads(line)
                for value in contents['documents']:
                    sentences = value.get('segmented_title', [])
                    if(sentences!= []):
                        yield sentences
                    paragraphs = value.get('segmented_paragraphs',[])
                    for v in paragraphs:
                        yield v
                answers = contents.get('segmented_answers',[])
                for answer in answers:
                    yield answer
                q = contents.get('segmented_question',[])
                if(q!=[]):
                    yield q
            f.close()

sentences = MySentences(data_path)
model = gensim.models.Word2Vec(sentences,size=50,min_count=1)
model.save('model')

with open(save_path,'w',encoding='utf-8') as fin:
    for key in model.wv.vocab.keys():
        try:
            fin.write(key + ' ')
            vv = list(model.wv[key])
            for v in vv:
                fin.write(str(v) + ' ')
            fin.write('\n')
        except:
            print(key)
fin.close()

