import numpy as np

AV = {'L': 0.395, 'A': 0.646, 'N': 1.0}
AC = {'H': 0.35, 'M': 0.61, 'L': 0.71}
Au = {'M': 0.45, 'S': 0.56, 'N': 0.704}
C = {'N': 0.0, 'P': 0.275, 'C': 0.66}
I = {'N': 0.0, 'P': 0.275, 'C': 0.66}
A = {'N': 0.0, 'P': 0.275, 'C': 0.66}

av = AV.get(input('Access vector:\n'))
ac = AC.get(input('Access complexity:\n'))
au = Au.get(input('Authentication:\n'))
c = C.get(input('Confidentiality:\n'))
i = I.get(input('Integrity:\n'))
a = A.get(input('Availability:\n'))

Impact = 10.41 * (1 - (1 - i) * (1 - c) * (1 - a))

f_Impact = Impact if Impact == 0 else 1.176

Exploitability = 20 * av * ac * au

BaseScore = np.round(((0.6 * Impact) + (0.4 * Exploitability) - 1.5) * f_Impact, decimals=1)

print(f'Base score: {BaseScore}')

E = {'ND': 1, 'U': 0.85, 'POC': 0.9, 'F': 0.95, 'H': 1}
RL = {'ND': 1, 'OF': 0.87, 'TF': 0.9, 'W': 0.95, 'U': 1}
RC = {'ND': 1, 'UC': 0.9, 'UR': 0.95, 'C': 1}

e = E.get(input('Exploitability:\n'))
rl = RL.get(input('Remediation level:\n'))
rc = RC.get(input('Report Confidence:\n'))

TemporalScore = np.round(BaseScore * e * rl * rc, decimals=1)

print(f'Temporal score: {TemporalScore}')

CDP = {'ND': 0, 'N': 0, 'L': 0.1, 'LM': 0.3, 'MH': 0.4, 'H': 0.5}
TD = {'ND': 1, 'N': 0, 'L': 0.25, 'M': 0.75, 'H': 1}
CR = {'ND': 1, 'L': 0.5, 'M': 1, 'H': 1.51}
IR = {'ND': 1, 'L': 0.5, 'M': 1, 'H': 1.51}
AR = {'ND': 1, 'L': 0.5, 'M': 1, 'H': 1.51}

td = TD.get(input('Target Distribution:\n'))
cdp = CDP.get(input('Collateral Damage Potential:\n'))
ar = AR.get(input('Availability Requirements:\n'))
cr = CR.get(input('Confidentiality Requirements:\n'))
ir = IR.get(input('Integrity Requirements:\n'))

AdjustedImpact = min(10, 10.41 * (1 - (1 - c * cr) * (1 - i * ir) * (1 - a * ar)))
AdjustedBaseScore = ((0.6 * AdjustedImpact) + (0.4 * Exploitability) - 1, 5) * f_Impact
AdjustedTemporal = AdjustedBaseScore * e * rl * rc
EnvironmentalScore = np.round((AdjustedTemporal + (10 - AdjustedTemporal) * cdp) * td)
