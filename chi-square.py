# options: to calculate p value, to show work in a table,
import scipy
import scipy.stats as stats





obs = input("Enter list of observed values seperated by spaces: ")
obs = obs.split(' ')
obs = [int(i) for i in obs]

exp = input("Enter list of expexted values seperated by spaces: ")
exp = exp.split(' ')
exp = [int(i) for i in exp]




pvalue = input("Do you need the p-value? [y/n]:")

if len(obs) != len(exp):
    print('Error: length of lists do not match')
    exit()


chi2 = 0
for i in range(len(obs)) :
    chi2 += ((obs[i]-exp[i])**2)/exp[i]

print(f'Chi-Sqaure equals: {chi2}')

print(f'The p-value is: {1 - stats.chi2.cdf(chi2, len(obs) - 1)}')

