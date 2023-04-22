import pandas as pd
from pybliometrics import scopus

def create_abstract_text_file(bibliographic_dataframe, file_name='compiled_abstracts.txt', autocloud=False, **kwds):
    '''
    Create text file combining all abstracts for a given bibliography.
    bibliographic_dataframe (pandas.DataFrame): expects index column to be of EIDs.
    file_name (str): name to be assigned to outputted text file
    autocloud (bool): if True, automatically returns a wordcloud representation of the text file.
    '''
    import pandas as pd
    from pybliometrics import scopus
    
    abstract_string = ' '
    for eid in bibliographic_dataframe.index:
        new_abstract = scopus.AbstractRetrieval(eid, view='FULL').abstract
        if new_abstract:
            abstract_string+=' '+new_abstract

    text_file = open(file_name, "w")
    text_file.write(abstract_string)
    text_file.close()
    
    if autocloud:
        wc = WordCloud(**kwds).generate(abstract_string)
        return ax.imshow(wc)