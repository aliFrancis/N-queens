import pandas as pd


class Scoreboard():
    def __init__(self,population,metric_dict):
        self.population = population
        self.metric_names,self.metric_funcs = metric_dict.keys,metric_dict.values
        self.table = pd.DataFrame({'boards':self.population[:]})
        for name,metric_func in zip(self.metric_names,self.metric_funcs):
            self.table[name] = pd.Series([metric_func(board) for board in self.population[:]], index=self.table.index)

    def sort_by(metric_names):
        self.table.sort_values(by=metric_names,inplace=True)
