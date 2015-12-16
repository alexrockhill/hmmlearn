import numpy as np
from sklearn.datasets.samples_generator import make_spd_matrix


def fit_hmm_and_monitor_log_likelihood(h, X, lengths=None, n_iter=1):
    h.n_iter = 1        # make sure we do a single iteration at a time
    h.init_params = ''  # and don't re-init params
    loglikelihoods = np.empty(n_iter, dtype=float)
    for i in range(n_iter):
        h.fit(X, lengths=lengths)
        loglikelihoods[i] = h.score(X, lengths=lengths)
    return loglikelihoods


def make_covar_matrix(covariance_type, n_components, n_features):
    mincv = 0.1
    rand = np.random.random
    return {
        'spherical': (mincv + mincv * np.dot(rand((n_components, 1)),
                                             np.ones((1, n_features)))) ** 2,
        'tied': (make_spd_matrix(n_features)
                 + mincv * np.eye(n_features)),
        'diag': (mincv + mincv * rand((n_components, n_features))) ** 2,
        'full': np.array([(make_spd_matrix(n_features)
                           + mincv * np.eye(n_features))
                          for x in range(n_components)])
    }[covariance_type]