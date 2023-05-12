# -*- coding: utf-8 -*-
"""
Created on Thu May 11 22:15:43 2023

@author: chris
"""
#Purpose
The United States government has announced a goal of deploying 30 gigawatts (GW) of offshore wind energy by 2030. Deploying 30 GW of offshore wind energy has the potential to create new domestic manufacturing industries in the United States in pursuit of decarbonizing our nation's electric grid. 

However, creating a domestic offshore wind energy industry and deploying 30 GW of offshore wind energy will require the federal government, states, and private corporations to expend substantial capital and political will in pursuit of this goal. Policymakers seeking to decarbonize our nation's electric grid must utilize resources efficiently in support of decarbonizing our country's electric grid. 

This analysis will seek to determine the conditions that an offshore wind project will need to meet to more efficiently offset carbon emissions than other renewable energy sources. It will then calculate the efficiency of reducing greenhouse gas emissions with offshore wind relative to an estimated social cost of carbon emissions. 

#Input Data 
No input data needs to be downloaded. Assumptions built into this script can be found in the resources copied below. However, the script can be edited based on alternative assumptions regarding renewable energy capacity factor, capital expenditures, and price estimates.

Capacity factor estimates for offshore wind (oswcf). solar (solar_low), and land based wind from NREL Technology projections https://atb.nrel.gov/electricity/2021/technologies

Emissions coefficients https://www.eia.gov/totalenergy/data/monthly/pdf/mer.pdf, https://www.eia.gov/environment/emissions/co2_vol_mass.php

Cap_ex from US DOE Office of Energy Efficiency and Renewable Energy Offshore Wind Market Report figure 41, which states that average capital expenditures for US based projects that have disclosed cost data and are larger than 500MW are $3400/kWh: https://www.energy.gov/sites/default/files/2022-09/offshore-wind-market-report-2022-v2.pdf

# Scripts
There is one script in this repository. 

Wind.py calculates:
1) Greenhouse gas emissions reductions associated with 1GW offshore wind, and land-based solar and wind projects based on typical capacity factors, 1 GW of nameplate capacity, and the fossil fuel source they displace
2) Calculates value of emissions reductions assuming a $50/ton social cost of carbon
3) Emmissions.png plots the emissions reduction potential of offshore wind, land-based wind, and solar projects based on a 1 GW project and the fossil fuel source the project would displace 
4) Calculates the estimated capital expenditures for a sample 1GW offshore wind project
5) Calculates the annualized cost of the sample project assuming a 20-year lifetime and a 5% interest rate. 
6) Calculates and plots (Emission Reduction Costs.png) the unsubsidized monetary cost of reducing greenhouse gas emissions from the sample project relative to the social cost of carbon

# Results
Emissions.png shows that offshore wind projects generally must have a capacity factor >.5 for the greenhouse gas emissions reduction potential for offshore wind energy to exceed the most efficient land-based wind energy sources. Offshore wind is expected to displace more emissions than solar projects that take natural gas projects offline, though solar projects that displace coal energy are generally more efficient at reducing emissions than offshore wind projects that displace natural gas power. 
Emissions Reduction Costs.png shows that, based on current capital expenditure estimates for offshore wind projects, all offshore wind projects regardless of capacity factor can be economically justified based on a $50 social cost of carbon estimate. 
This script provides policymakers with a tool to determine whether proposed offshore wind projects will more efficiently reduce carbon emissions than other renewable projects that may be available based on capacity factor. This script also shows that the benefits provided by offsetting damages associated with carbon emissions exceed the costs of the sample offshore wind project. 

# Limitations
1) This analysis only includes capital expenditures. Information on operational expenditures, and cost estimates for infrastructure needed to deploy offshore wind energy (i.e. port infrastructure improvements, transmission infrastructure) was not readily available. Including these will likely significantly affect project cost.
2) Cost analysis does not account for federal or state tax incentives related to offshore wind that could further drive down offshore wind deployment costs. 
