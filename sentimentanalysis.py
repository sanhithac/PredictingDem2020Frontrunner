def gc_sentiment(text):  
    from google.cloud import language
    
    path = '/Users/Sonya/Documents/green-antonym-273518-61a99f32289c.json' #FULL path to your service account key
    client = language.LanguageServiceClient.from_service_account_json(path)
    document = language.types.Document(
            content=text,
            type=language.enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    return score, magnitude
    
    from tqdm import tqdm # This is an awesome package for tracking for loops
import pandas as pd
gc_results = [gc_sentiment(row) for row in tqdm(tokenized_word, ncols = 100)]
gc_score, gc_magnitude = zip(*gc_results) # Unpacking the result into 2 lists
gc = list(zip(tokenized_word, gc_score, gc_magnitude))
columns = ['text', 'score', 'magnitude']
gc_df = pd.DataFrame(gc, columns = columns)

gc_df
