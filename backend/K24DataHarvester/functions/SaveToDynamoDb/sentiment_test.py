import os
import json
import pandas as pd
from flair.data import Sentence
from flair.models import SequenceTagger
from flair.models import TextClassifier

def _get_file_content_as_json(file_path):
    with open(file_path, 'r') as f:
        file_content = f.read()
        return json.loads(file_content)

def _perform_sentiment_analysis(data):
    df = pd.DataFrame.from_dict(data)
    tagger = SequenceTagger.load('ner')
    classifier = TextClassifier.load('en-sentiment')

    for key in data.keys():
        row = data[key]
        cleanedTweet = row['text'].replace("#", "")
        sentence = Sentence(cleanedTweet, use_tokenizer=True)
        # predict NER tags
        tagger.predict(sentence)

        # get ner
        ners = sentence.to_dict(tag_type='ner')['entities']
        
        # predict sentiment
        classifier.predict(sentence)
        
        label = sentence.labels[0]
        response = {'result': label.value, 'polarity':label.score}

        # add more code here

        sentiment_data = {}
        sentiment_data["sentiment"] = "Negative"
        sentiment_data["polarity"] = 0
        sentiment_data["adj_polarity"] = -1
        
        data[key] = {**data, **sentiment_data}

    return data

data = _get_file_content_as_json('data.json')
df = _perform_sentiment_analysis(data)
print(df)

