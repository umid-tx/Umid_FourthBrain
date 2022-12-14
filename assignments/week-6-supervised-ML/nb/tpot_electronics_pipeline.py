import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.pipeline import make_pipeline, make_union
from tpot.builtins import StackingEstimator
from tpot.export_utils import set_param_recursive

# NOTE: Make sure that the outcome column is labeled 'target' in the data file
#tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
#features = tpot_data.drop('target', axis=1)
#training_features, testing_features, training_target, testing_target = \
#            train_test_split(features, tpot_data['target'], random_state=42)

tpot_data = pd.read_csv('../dat/train.csv.gz')
test_df = pd.read_csv('../dat/test.csv.gz')
features = tpot_data.drop('Purchase', axis=1)
training_features = features
testing_features = test_df.drop('Purchase', axis=1)
training_target = tpot_data['Purchase']
testing_target = test_df['Purchase']


# Average CV score on the training set was: 1.0
exported_pipeline = make_pipeline(
    PCA(iterated_power=8, svd_solver="randomized"),
    StackingEstimator(estimator=BernoulliNB(alpha=0.001, fit_prior=False)),
    RandomForestClassifier(bootstrap=False, criterion="entropy", max_features=0.6500000000000001, min_samples_leaf=3, min_samples_split=18, n_estimators=100)
)
# Fix random state for all the steps in exported pipeline
set_param_recursive(exported_pipeline.steps, 'random_state', 42)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
