# Spacy based Named Entity Recognition model with test data on roll call.
# Roll call seems to work best with en_core_web_md rather than en_core_web_sm or en_core_web_lg in actually identifying names.

import spacy
import re

def run():
    ner_spacy()

def ner_spacy():
    # load spacy model
    nlp = spacy.load('en_core_web_md')
    
    # load data
    data = data_test_5
    nlp = spacy.blank("en")
    ruler = nlp.add_pipe("entity_ruler")

    patterns = [{"label": "IDENTIFIER", "pattern": "(Citizen Member [A-Z]\w+|Councillor [A-Z]\w+|Citizen Representative [A-Z]\w+)"}]

    ruler.add_patterns(patterns)
    doc = nlp(data)

    for ent in doc.ents:
        print(ent.text, ent.label_)
    
    # pattern = r"(Citizen Member [A-Z]\w+|Councillor [A-Z]\w+|Citizen Representative [A-Z]\w+)"
    # matches = re.finditer(pattern, data)
    
    
    
    # doc = nlp(data)
    
    # # print entities
    # for ent in doc.ents:
    #     print(ent.text, ent.label_)

"""
Needs:
- method for direct data transmission (import data)
    - method to turn audio data into text data to then be run through OR,
    - take one of the scrapper inputs as a string to be run through.
        - NER system seems reliant on context words which don't seem avaliable in scrapper data.
- 

"""

# Test string for call to order, direct text
data_test_1 = "Good morning. Are we, ready to go folks? That's correct madame chair we're now live. Fantastic thank you. Um, so I'd like to call this meeting to order and if I could get the clerk to please conduct role call before we get going. Certainly, on the role call Citizen Member Nenshi. Here! Thank you. Vice-Chair Holub. Here! Thank you, and chair Bodnaryk. Here! All members are present. Thank you so much."
data_test_2 = "Chair Bodnaryk called the Meeting to order at 9:31 a.m. ROLL CALL Citizen Member Holub, Citizen Member Nenshi, and Chair Bodnaryk."
data_test_3 = "Chair Bodnaryk provided opening remarks and a traditional land acknowledgement."
data_test_4 = "Moved byCitizen Member Holub That the Agenda for the 2022 February 3 Regular Meeting of the Citizen-Led Selection Committee for the Integrity Commissioner be confirmed."
data_test_5 = "Councillor Pootmans called the Meeting to order at 9:32 a.m. ROLL CALL Councillor Wong, Councillor Spencer, Councillor Wyness, Citizen Representative Lambert, Citizen Representative Kim, and Councillor Pootmans. Absent from Roll Call: Citizen Member Caltagirone "

# Transfer learning on results





run()