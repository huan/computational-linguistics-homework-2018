'''
doc
'''
import tensorflow as tf
import numpy as np

from chinese_segmentation.config import MAX_LEN
from chinese_segmentation.vocabulary import Vocabulary
from chinese_segmentation.model import build_model
from chinese_segmentation.data_loader import load_data

def main () -> int:
    with open('data/corpus_preprocessed.txt', 'r') as f:
        raw_text = f.read()

    voc = Vocabulary(raw_text)
    model = build_model(voc.size)

    X, y = load_data()
    X = voc.texts_to_padded_sequences(X)


    model.load_weights('./data/checkpoints/my_checkpoint')
    model.fit(X, y, batch_size=16, epochs=1)
    model.save_weights('./data/checkpoints/my_checkpoint')

    predicted = model.predict(X[0:3])
    result = np.ones(
        (
            predicted.shape[0],
            predicted.shape[1],
            predicted.shape[2],
        )
    ) * (predicted > 0.5)
    print(result)
    print('-'*80)
    print(y[0:3])
    print('-'*80)
    import pdb; pdb.set_trace()

    a = result - y[0:3]
    b = np.mean(a)

main()
