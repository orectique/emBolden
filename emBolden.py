from keybert import KeyBERT

kb = KeyBERT()

import streamlit as st

st.title('emBolden')

def process(corpus):
    corpus = corpus.replace('\n', ' ')

    out  = ''

    for sent in corpus.split('.'):
        keys = kb.extract_keywords(sent, keyphrase_ngram_range=(1, 3), stop_words='english', use_maxsum=True, nr_candidates=20)

        wlist = []
        for key in keys:
            if key[1] > 0.35:
                temp = key[0].split()
                for i in temp:
                    wlist.append(i)

        wlist = set(wlist)
        
        for word in wlist:
            sent = sent.replace(word, f'**{word}**')

        out += sent + '. '

    return out


with st.form('In'):
    text = st.text_area('Enter text here', height=500)
    submit = st.form_submit_button('Submit')

    if submit:
        out = process(text)
        st.markdown(out)   

