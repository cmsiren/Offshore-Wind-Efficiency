"""
wind.py
.
"""

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 300


hours = 8760

# Setting parameters for capacity factor estimates for technologies
# and emisisons coefficients. 

oswcf_low = 0.46
oswcf_high = 0.55

solar_low = 0.193
solar_high = 0.371

landwind_low = 0.44
landwind_high = 0.50

coal_mwh = 0.9972
gas_mwh = 0.4218

#%% 
# Creating dataframes that feature the capacity factor ranges of 
# offshore wind, solar, and land-based wind generation. 

oswcf = pd.Series([oswcf_low, oswcf_high])
osw_gwh_act = oswcf * hours
osw_gwh_act.index = oswcf

offshore_wind_data = pd.DataFrame(index=oswcf)

sun = pd.Series([solar_low, solar_high])
sun_gwh_act = sun * hours
sun_gwh_act.index = sun

sun_data = pd.DataFrame(index=sun)

landwind = pd.Series([landwind_low, landwind_high])
landwind_gwh_act = landwind * hours
landwind_gwh_act.index = landwind

landwind_data = pd.DataFrame(index=landwind)


#%% 
# Calculates the potential greenhouse gas emissions reductions associated
# with offshore wind, solar, and land-based wind.

offshore_wind_data['OSW - Coal'] = (osw_gwh_act*1e3 * coal_mwh) /1e6 
offshore_wind_data['OSW - Gas CC'] = (osw_gwh_act*1e3 * gas_mwh) /1e6

sun_data['Solar - Coal'] = (sun_gwh_act*1e3 * coal_mwh) /1e6
sun_data['Solar - Gas CC'  ] = (sun_gwh_act *1e3 * gas_mwh) /1e6

landwind_data['Land Wind - Coal'] = (landwind_gwh_act*1e3 * coal_mwh) /1e6
landwind_data['Land Wind - Gas CC'  ] = (landwind_gwh_act *1e3 * gas_mwh) /1e6

#%% Calculates the potential greenhouse gas emissions reductions associated
# with offshore wind, solar, and land-based wind. 

# Best and worst are defined# in relation to the turbine, where worst refers 
# to the projects with the # lowest capacity factor, while best refers to those
# with the highest capacity factor. 

osw_cc_worst   = offshore_wind_data['OSW - Gas CC'].min()
osw_cc_best    = offshore_wind_data['OSW - Gas CC'].max()
osw_coal_worst = offshore_wind_data['OSW - Coal'].min()
osw_coal_best  = offshore_wind_data['OSW - Coal'].max()
# 
sun_cc_worst   = sun_data['Solar - Gas CC'].min()
sun_cc_best    = sun_data['Solar - Gas CC'].max()
sun_coal_worst = sun_data['Solar - Coal'].min()
sun_coal_best  = sun_data['Solar - Coal'].max()

land_cc_worst   = landwind_data['Land Wind - Gas CC'].min()
land_cc_best    = landwind_data['Land Wind - Gas CC'].max()
land_coal_worst = landwind_data['Land Wind - Coal'].min()
land_coal_best  = landwind_data['Land Wind - Coal'].max()


#%% Social Cost of Carbon parameters - assumes $50/ton. 
scc_mult = 50

#%% Calculating value of emissions reductions assuming a $50/ton social cost of carbon
print('Annual Offshore Wind Value of Emissions Offset for 1GW project ($50 social cost of carbon):')
print(f'Emissions Reduction Range: {osw_cc_best:.03f} to {osw_coal_best:.03f} MMT')
print(f'Value of Offset Emissions (in million $):{osw_cc_best*scc_mult:.03f} to {osw_coal_worst*scc_mult:.03f}')

print('\nAnnual Solar Value of Emissions Offset for 1GW project($50 social cost of carbon):')
print(f'Emissions Reduction Range: {sun_cc_best:.03f} to {sun_coal_worst:.03f} MMT')
print(f'Value of Offset Emissions (in million $): {sun_cc_best*scc_mult:.03f} to {sun_coal_worst*scc_mult:.03f}')

print('\nAnnual Land Wind Value of Emissions Offset for 1GW project ($50 social cost of carbon):')
print(f'Emissions Reduction Range: {land_cc_worst:.03f} to {land_cc_best:.03f} MMT')
print(f'Value of Offset Emissions (in million $): {land_cc_best*scc_mult:.03f} to {land_coal_worst*scc_mult:.03f}\n')
#%%

#Plots the emissions reduction potential of offshore wind, land-based wind,
# and solar projects based on  the project's capacity factor and the fuel
# source it is taking offline or obviating the need for. 

fig1,ax1 = plt.subplots()

offshore_wind_data.plot.line(ax=ax1,title='Avoided Emissions per year for a 1GW Project', lw = 3 )
sun_data.plot.line(ax=ax1, lw = 1)
landwind_data.plot.line(ax=ax1, lw = 1)

ax1.set_xlabel('Capacity Factor')
ax1.set_ylabel('Million Metric Tons GHG ')
ax1.axhline(osw_cc_best,color='gray',ls='--',lw=1)
ax1.axhline(osw_coal_best,color='gray',ls='--',lw=1)
ax1.axhline(osw_cc_worst,color='gray',ls='--',lw=1)
ax1.axhline(osw_coal_worst,color='gray',ls='--',lw=1)
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.xlim(.1,.6)

fig1.tight_layout()
fig1.savefig('Emissions.png')

#%% Calculating cap ex for a 1GW sample offshore wind project. 

cap_ex_kw = 3400
cap_ex_1mw = (cap_ex_kw*1000)
cap_ex_1gw = (cap_ex_1mw*1000)

print('Expected Capital Expenditures for a 1GW Offshore Wind Project:',cap_ex_1gw,'\n')

#%% Calculating levelized cost of capital expenditures for annual GHG emissions
# cost efficiency estimates. 
# Assumes 20 year project life. 
r=.05

lc_cap_ex = (cap_ex_1gw*.05/(1-(1/(1+r)**20)))/1e6
print('\nLevelized cost of capital expenditures (in millions): $', lc_cap_ex)  
   
#%% Calculating the net cost of emissions reductions. Subtracts the product of 
# the wholesale price of electricity and the expected low and high end 
# capacity factors for offshore wind.

# Assumes an average wholesale cost of $50 per mWh. 
price = 50

net_cost_high = lc_cap_ex - price * 1000*hours*oswcf_low/1e6
net_cost_low = lc_cap_ex - price * 1000*hours*oswcf_high/1e6

print('Expected cost per mWh:', net_cost_high)
print('Expected cost per mWh:', net_cost_low)
#%%
# Calculating unsubsidized monetary cost of reducing greenhouse gas emissions
# gas_worst reflects offshore wind projects with the lowest expected capacity
# factor replacing a combined cycle gas plant, while gas_best refers to a 
# offshore wind project with the highest expected capacity factor. The same 
# naming convention applies to coal_worst and coal_best.   

gas_worst =(net_cost_high/osw_cc_worst)
gas_best = (net_cost_low/osw_cc_best)
coal_worst = (net_cost_high/osw_coal_worst)
coal_best = (net_cost_low/osw_coal_best)


#%%
# Creates a figure that shows how efficient an offshore wind project would 
# need to be to be justified for emissions benefits to outweigh project 
# construction costs. 

fig2,ax1 = plt.subplots()

fig2.suptitle('Cost of reducing emissions with offshore wind \nby fuel source and capacity factor')
ax1.set_ylabel('Dollars')
ax1.set_xlabel('Offshore Wind Project Capacity Factor')
ax1.axhline(scc_mult, color = 'purple', ls = '-', label = 'Social Cost of Carbon', lw = 1)
ax1.plot((gas_worst, gas_best), color='blue', ls='--', label='Gas', lw = 1)
ax1.plot((coal_worst, coal_best), color='red', ls='--', label='Coal', lw = 1)
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))

fig2.tight_layout()
fig2.savefig('Emission Reduction Costs.png')

