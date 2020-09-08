DEFAULT_FIGSIZE = (17, 5)

def plotAbsoluteCases(df):
    df.TotalConfirmedCases.plot(figsize=DEFAULT_FIGSIZE, title="Total Cases", legend=True)
    df.TotalDeathCases.plot(figsize=DEFAULT_FIGSIZE, legend=True)

def plotNewCases(df):
    df.NewConfirmedCases.plot(figsize=DEFAULT_FIGSIZE, title="New Cases", legend=True)
    df.NewDeathCases.plot(figsize=DEFAULT_FIGSIZE, legend=True)