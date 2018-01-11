class AnnualStats:
    """Collect (year, measurement) data for statistical analysis.
    >>> from ch_5_ex_4 import AnnualStats
    >>> test = AnnualStats( [(2000, 2),
    ...    (2001, 4),
    ...    (2002, 4),
    ...    (2003, 4),
    ...    (2004, 5),
    ...    (2005, 5),
    ...    (2006, 7),
    ...    (2007, 9),] )
    ...
    >>> test.min_year()
    2000
    >>> test.max_year()
    2007
    >>> test.mean()
    5.0
    >>> test.median()
    4.5
    >>> test.mode()
    4
    >>> test.stddev()
    2.0
    >>> list(test.stdscore())
    [-1.5, -0.5, -0.5, -0.5, 0.0, 0.0, 1.0, 2.0]
    """
