name: "VaR and ES calculator"
about: The code calculates VaR and ES for a given portfolio using historical returns data and prints the results.
labels: Quantitative Finance

---

## Description
The code calculates Value-at-Risk (VaR) and Expected Shortfall (ES) for a given portfolio using historical returns data.

Function Definitions:

calculate_var(portfolio, alpha=0.05): calculates the VaR for the given portfolio. The function takes two inputs:

portfolio: a pandas series or dataframe containing historical portfolio values.

alpha: the significance level for the VaR calculation. The default value is 0.05, which corresponds to a 95% confidence level.

calculate_es(portfolio, alpha=0.05): calculates the ES for the given portfolio. The function takes two inputs:

portfolio: a pandas series or dataframe containing historical portfolio values.

alpha: the significance level for the ES calculation. The default value is 0.05, which corresponds to a 95% confidence level.


### Environment
Libraries:
numpy
pandas
scipi.stats

### Basic example
Include a basic example or links here.
To reproduce this example please download the csv file attached in this repository.

<img width="790" alt="image" src="https://user-images.githubusercontent.com/129782426/231907230-3213cafd-4697-4c69-a239-7c27e131d01e.png">


