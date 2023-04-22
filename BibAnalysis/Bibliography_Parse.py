import pandas as pd
from pybliometrics import scopus

def clean_bibliography(uncleaned_bibliography, DOI=True, Title=True, EID=True, ISBN=True, PMID=True, positive=True, **kwargs):
    '''
    Take in table of identifying information. Massage into dataframe of scopus metadata. Dataframe sets EID
    (unique identifying number in Scopus database) as index column for convenience.
    
    Parameters
    ----------
    uncleaned_bibliography : pandas DataFrame
        Should have columns named exactly the same as the parameters.
    DOI : boolean
        Set to False to suppress DOI checking
    Title : boolean
        set to False to suppress title checking
    EID : boolean
        Set to False to suppress EID checking
    ISBN : boolean
        Set to False to suppress ISBN checking
    PMID : boolean
        Set to False to suppress PMID checking
    positive: boolean
        Set to False to suppress checking if entry is labeled as a true positive
    '''

    
    bibliography=pd.DataFrame()
    for i in range(len(uncleaned_bibliography)):
        row = uncleaned_bibliography.iloc[i, :]
        if positive and not row['Positive?']: #we want lazy! we want lazy!
            continue
        if DOI:
            bibliography = pd.concat([bibliography, pd.DataFrame(scopus.ScopusSearch(f'DOI("{row.DOI}")',\
                                                                        subscriber=False, **kwargs).results)])
        if Title:
            bibliography = pd.concat([bibliography, pd.DataFrame(scopus.ScopusSearch(f'TITLE("{row.Title}")',\
                                                                        subscriber=False, **kwargs).results)])
        if EID:
            bibliography = pd.concat([bibliography, pd.DataFrame(scopus.ScopusSearch(f'EID({row.EID})', \
                                                                        subscriber=False, **kwargs).results)])
        if PMID:
            bibliography = pd.concat([bibliography, pd.DataFrame(scopus.ScopusSearch(f'PMID({row.PMID})', \
                                                                        subscriber=False, **kwargs).results)])
        if ISBN:
            bibliography = pd.concat([bibliography, pd.DataFrame(scopus.ScopusSearch(f'ISBN({row.ISBN})', \
                                                                        subscriber=False, **kwargs).results)])
        
    bibliography.set_index('eid', inplace=True)
   
    
    return bibliography
