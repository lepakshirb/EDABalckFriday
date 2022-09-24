import pandas as pd
import sweetviz
train = pd.read_csv("blackFriday_train.csv")
test = pd.read_csv("blackFriday_test.csv")
my_report = sweetviz.analyze([train, "Train"],target_feat='Purchase')
#my_reportage = sweetviz.analyze([train, "Train"],target_feat='Occupation')
my_report.show_html('Sweetviz_report.html')