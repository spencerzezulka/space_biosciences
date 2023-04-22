global pd
import pandas as pd
from pybliometrics import scopus

class Corpus():
    import pandas as pd
    from pybliometrics import scopus
    
    '''
    Define a corpus of true positives, provide methods to compare corpus to the results of a query; store history.
    '''
    def __init__(self, YTP):
        '''
        Initialize corpus using table of Your True Positives (YTP)
            YTP (pd.DataFrame): the (cleaned) table of Your True Positives
        '''
        import pandas as pd
        from pybliometrics import scopus
        self.YTP = YTP
        self.unique_EIDs_in_YTP = set(self.YTP.index)
        self.history=[]
        self.cumulative_EIDs_from_queries_in_YTP = set([])
        self.remaining_in_YTP = self.YTP

        
    def check_recall(self, query, **kwargs):
        '''
        Submit query to Scopus Search. Append query and results to history, store in object memory.
        Automatically check overlap between corpus of true positives and results of a given query.
        Append overlap metrics (recall), to history, store in object memory. Print out relevant
        details of corresponding query, including marginal improvement in recall, as well as current cumulative
        recall.
        
        Parameters
        ----------
        query : string
            Scopus query. Follows Scopus syntax. Use signifiers like TITLE-ABS-KEY() for specificity.
        
        Notes
        -----
        For performance reasons (the speed of check_recall is contingent on the number of search results
        for a given subquery), this method provides functionality to improve search strategies involving
        the breakup of a main query into subqueries, and then testing them sequentially.
        The subqueries can later be joined into a single total query using OR statements.
        
        The history attribute of the Corpus object will contain the relevant historical performance of the 
        queries against the Corpus.
        '''
        import pandas as pd
        from pybliometrics import scopus
        query_results=pd.DataFrame(scopus.ScopusSearch(query,subscriber=True, **kwargs).results)
        query_results.set_index('eid', inplace=True)
        query_index = set(query_results.index)
        YTP_index = set(self.remaining_in_YTP.index)
        
        marginal_overlap = query_index & self.unique_EIDs_in_YTP
        self.cumulative_EIDs_from_queries_in_YTP = self.cumulative_EIDs_from_queries_in_YTP | marginal_overlap
        not_covered_by_queries = YTP_index-marginal_overlap

        self.current_recall = len(self.cumulative_EIDs_from_queries_in_YTP)/len(self.unique_EIDs_in_YTP)
        
        results_size = len(query_results)
        marginal_recall = len(marginal_overlap)/len(YTP_index)
        self.history.append({'marginal recall': marginal_recall, 'marginal overlap': marginal_overlap, 'query_results': query_results})
        
        print(f'Marginal recall for subquery {query} is {marginal_recall}.')
        print(f'Total recall for union of all past subqueries is {self.current_recall}')
        print(f'Number of results rendered: {results_size}.')
        print(f'EIDs not covered by query: {not_covered_by_queries}')
        
        not_covered = self.remaining_in_YTP.loc[not_covered_by_queries]
        
#         global YTP
        self.remaning_in_YTP = not_covered
        
        return not_covered
        
    
    def visualize_performance(self):
        '''
        Visualize the performance of your queries over time.
        '''
        pass
  