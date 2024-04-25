# Subspace Parameter Selection Report [WIP]


*Fig: Speed run over the [`PSuU` workflow analysis notebook](https://github.com/BlockScience/subspace/blob/recommendations-v1/notebooks/workflows/psuu.ipynb)*
![Screen Recording 2024-04-24 at 23.05.38](https://hackmd.io/_uploads/B1CNiEv-R.gif)


## Intro

**Summary**
Following the [economic design initiative](https://hackmd.io/fWCDFbEASJK50OpIQfEo4Q?view) to propose the Subspace Issuance Function, this parameter selection initiative will involve a computational science workflow to support the parameter selection decision-making process for the subspace economic system.

The goal of this document is to outline the *governance surface* (system parameters) of the Subspace system that is considered for the parameter selection workflow, as well as the corresponding rational for the values selected.

**Project Goal**
Determine the "best" initial parameter ranges for the newly designed issuance function, as well as other key system parameters, at launch of the Subspace protocol.

## Simulation Details

The simulations were prepared and interpreted as per the [Subspace PSuU Methodology](/iFeP7NemRH--KtWbPP_W0w) document. The model and notebooks used by the analysis can be found on the `BlockScience/subspace` GitHub repository, tagged as [`recommendations-v1`](https://github.com/BlockScience/subspace/tree/recommendations-v1). In particular, we've used the [`exploratory/inspect_psuu_timestep_tensor` notebook](https://github.com/BlockScience/subspace/blob/recommendations-v1/notebooks/exploratory/inspect_psuu_timestep_tensor.ipynb) for inspecting individual runs and the [`workflows/psuu.ipynb` notebook](https://github.com/BlockScience/subspace/blob/recommendations-v1/notebooks/workflows/psuu.ipynb) for interprating the aggregated data.

The data (timestep and trajectory tensors) can be found on an Amazon S3 bucket located at https://subspace-simulations.s3.us-east-2.amazonaws.com.

**Characteristics of the Resulting Dataset (or Timestep Tensor)**
- Temporal Coverage: Daily Measurements over 3 years (`1,096` state measurements per simulation trajectory)
- Count of Controllable Parameter Combinations: `5,832`
- Count of Environmental Parameter Combinations: `12`
- Count of Total Parameter Combinations: `69,984`
- Monte Carlo Runs: `3`
- Count of Simulation Trajectories: `209,952`
- Count of State Measurements: `230,108,392`

**Controllable Parameters values swept**
|Controllable Parameter|Values|
|---|---|
|$\tau_{0, 1}$ :`component_1_initial_period_start`|{0, 14 days, 30 days}|
|$\alpha_1$ :`component_1_max_reference_subsidy`|{1SSC/blk, 4SSC/blk, 7SSC/blk}|
|$\Omega_1$ :`component_1_max_cumulative_subsidy`|{10%, 30% and 50%}|
|$\tau_{0, 2}$ :`component_2_initial_period_start`|{0, 14 days, 30 days}|
|$\tau_{1, 2}$ :`component_2_initial_period_duration`|{6mo, 1yr, 2yr, 4yr}|
|$\alpha_2$ :`component_2_max_reference_subsidy`|{1SSC/blk, 4SSC/blk, 7SSC/blk}|
|$\Omega_2$ :`component_2_max_cumulative_subsidy`|{10%, 30% and 50%}|
|$\alpha$ :`reward_proposer_share`|{10%, 33%}|
|$\omega$ :`weight_to_fee`|{1, 100, 1,000, 10,000}|


## Simulation Interpretation

In this section we provide correlation & confidence interpretations for 
1. each parameter relative to a single KPI label (e.g. 0 or 1) and
2. each parameter relative to a System Goal individually (e.g. aggregation of KPIs)


**KPI legend**
* KPI 1: `mean_relative_community_owned_supply`
* KPI 2: `mean_farmer_subsidy_factor`
* KPI 3: `mean_proposing_rewards_per_newly_pledged_space`
* KPI 4: `mean_proposer_reward_minus_voter_reward`
* KPI 5: `cumm_rewards_before_1yr`
* KPI 6: `abs_sum_storage_fees_per_sum_compute_fees`
* KPI 7: `cumm_rewards`

**System Goal legend**
* Goal 1: Rational Economic Incentives
* Goal 2: Community Incentivization
* Goal 3: Supply and Demand Equilibrium / Distributional Equilibrium


**Interpretation legend**
*Relationship of Parameter to KPI label* (i.e. for positive, larger values of parameter leads to more KPI = true outcomes)
* +: Positive correlation against the KPI label (eg. larger parameter values reinforces the intent)
* -: Negative correlation against the KPI label (eg. smaller parameter values reinforces the intent)
* o: Uncorrelated against the KPI label
* ?: Inconclusive

*Confidence and/or Effect Strength*
* C: Conclusive and/or Large Importance
* I: Indicative and/or Minor Importance
* ?: Inconclusive and/or Un-important


### Interpretation #1: each parameter relative to a single KPI label (e.g. 0 or 1)

|Parameter / KPI|1|2|3|4|5|6|7|
|---|---|---|---|---|---|---|---|
|$\tau_{0, 1}$:`component_1_initial_period_start`|-,C|?|?|?|-,I|?|-,I|
|$\alpha_1$:`component_1_max_reference_subsidy`|+,C|-,C|+,C|+,C|+,C|?|+,C|
|$\Omega_1$:`component_1_max_cumulative_subsidy`|o, I|?|?|?|?|?|?|
|$\tau_{0, 2}$:`component_2_initial_period_start`|-,C|?|?|?|-,I|?|-,I|
|$\tau_{1, 2}$:`component_2_initial_period_duration`|?|?|?|?|?|?|?|
|$\alpha_2$:`component_2_max_reference_subsidy`|+,C|-,C|+,C|+,C|+,C|?|+,C|
|$\Omega_2$:`component_2_max_cumulative_subsidy`|?|?|?|?|+,C|?|?|
|$\alpha$:`reward_proposer_share`|o,C|o,C|?|?|o,C|?|o,C|
|$\omega$:`weight_to_fee`|o,C|?|o,C|o,C|o,C|?|o,C


### Interpretation #2: each parameter relative to a System Goal individually (e.g. aggregation of KPIs)

**System Goal <> KPI mapping**
* Goal 1 <> KPI 3, 4
* Goal 2 <> KPI 1, 5
* Goal 3 <> KPI 2, 6, 7

*Note: each KPI weighted equally in aggregation*

|Parameter|Goal 1|Goal 2|Goal 3|Combined|
|---|---|---|---|-|
|$\tau_{0, 1}$ :`component_1_initial_period_start`|-,I|?|+,I|-C|
|$\alpha_1$ :`component_1_max_reference_subsidy`|+,C|+,C|-,C|+,C|
|$\Omega_1$ :`component_1_max_cumulative_subsidy`|?|?|?|?|
|$\tau_{0, 2}$ :`component_2_initial_period_start`|-,I|-,I|?|-C|
|$\tau_{1, 2}$ :`component_2_initial_period_duration`|+,?|?|?|?|
|$\alpha_2$ :`component_2_max_reference_subsidy`|+,C|+,C|-,C|+,C|
|$\Omega_2$ :`component_2_max_cumulative_subsidy`|+,I|?|?|?|
|$\alpha$ :`reward_proposer_share`|?|?|?|?|
|$\omega$ :`weight_to_fee`|o,C|o,C|?|?|


---
---
---

## Parameter Recommendations

In this section we provide 3 sets of parameter recommendations based on the simulation output data, and correlation evaluation from above.

1. **Global Point number** - A single value for each parameter, assuming all system goals equally weighted, and following the decision-making heuristic:
    * Positive correlation -> pick highest sweep value
    * Negative correlation -> pick lowest sweep value
    * Uncorrelated or inconclusive -> pick mid-point of sweep values
    * Average selected values

    |Parameter|Value|
    |---|---|
    |$\tau_{0, 1}$ :`component_1_initial_period_start`|0 days|
    |$\alpha_1$ :`component_1_max_reference_subsidy`|7.0 SSC/blk|
    |$\Omega_1$ :`component_1_max_cumulative_subsidy`|30% of `MaxIssuance`|
    |$\tau_{0, 2}$ :`component_2_initial_period_start`|0 days|
    |$\tau_{1, 2}$ :`component_2_initial_period_duration`|1.5 years|
    |$\alpha_2$ :`component_2_max_reference_subsidy`|7.0 SSC/blocks|
    |$\Omega_2$ :`component_2_max_cumulative_subsidy`|30% of `MaxIssuance`|
    |$\alpha$ :`reward_proposer_share`|20%|
    |$\omega$ :`weight_to_fee`|500 Shannon|

2. **Local Range for Single Goal Optimization** - A range of values for each parameter that optimize for a single goal, following the decision-making heuristic:
    * Positive correlation -> select top two sweep values (use mid-point if only two values swept)
    * Negative correlation -> select bottom two sweep values (use mid-point if only two values swept)
    * Uncorrelated or inconclusive -> full range of sweep values

    |Parameter|Max Goal 1|Max Goal 2|Max Goal 3|
    |---|---|---|---|
    |$\tau_{0, 1}$:`component_1_initial_period_start`|0 days|14 days|30 days|
    |$\alpha_1$:`component_1_max_reference_subsidy`|7.0 SSC/blk|7.0 SSC/blk|1.0 SSC/blk|
    |$\Omega_1$:`component_1_max_cumulative_subsidy`|30% of `MaxIssuance`|30% of `MaxIssuance`|30% of `MaxIssuance`|
    |$\tau_{0, 2}$:`component_2_initial_period_start`|0 days|0 days|14 days|
    |$\tau_{1, 2}$:`component_2_initial_period_duration`|1.5 years|1.5 years|1.5 years|
    |$\alpha_2$:`component_2_max_reference_subsidy`|7.0 SSC/blk|7.0 SSC/blk|1.0 SSC/blk|
    |$\Omega_2$:`component_2_max_cumulative_subsidy`|30% of `MaxIssuance`|30% of `MaxIssuance`|30% of `MaxIssuance`|
    |$\alpha$:`reward_proposer_share`|20%|20%|20%|
    |$\omega$:`weight_to_fee`|500 Shannon|500 Shannon|500 Shannon|

3. **Global Range** - A range of values, assuming equally weighted system goals, and following the decision-making heuristic:
    * Positive correlation -> select top two sweep values (use mid-point if only two values swept)
    * Negative correlation -> select bottom two sweep values (use mid-point if only two values swept)
    * Uncorrelated or inconclusive -> full range of sweep values
    * Average both range values

    |Parameter|Global Range|
    |---|---|
    |$\tau_{0, 1}$ :`component_1_initial_period_start`|Between 0 and 7 days|
    |$\alpha_1$ :`component_1_max_reference_subsidy`|Between 5.5 and 7.0 SSC/blk|
    |$\Omega_1$ :`component_1_max_cumulative_subsidy`|Between 10% and 50% `MaxIssuance`|
    |$\tau_{0, 2}$ :`component_2_initial_period_start`|Between 0 and 7 days|
    |$\tau_{1, 2}$ :`component_2_initial_period_duration`|Between 6mo and 4 years|
    |$\alpha_2$ :`component_2_max_reference_subsidy`|Between 5.5 and 7.0 SSC/blk|
    |$\Omega_2$ :`component_2_max_cumulative_subsidy`|Between 10% and 50% `MaxIssuance`|
    |$\alpha$ :`reward_proposer_share`|Between 10% and 33%|
    |$\omega$ :`weight_to_fee`|Between 1 and 10,000 Shannon|


## Governance Surface Overview
In this section we describe the full Governance Surface of Subspace

* **The Vectorial Block Reward function** defined by $\vec{B}(t)$ (see [Decoupled Issuance](https://hackmd.io/@blockscience/SkEPigvFa)) requires the following parameters:

|Parameter|Description|Domain|Current value|Unit|Considered for Parameter Sweep?|
|---|---|---|---|---|---|
|$c \in \mathbb{R}_+$|Hyperbolic Sensitivity Parameter|[0.1, 10]|0.99|float|No|
|$d \in [1, \infty]$|Saturation Velocity Parameter|[0,1]|1|float|No|
|$\langle n \rangle$|Expected Count of Voters|[1,20]|9(exp.)|int|No|
|$\langle n_p \rangle$|expected count of proposers|[1]|1|int|No|
|$\alpha$|relative proposer tax (bonus)|[0,100]|10%|%|No|

* **Two reference subsidy components** $s_{1,p}(t)$ and $s_{2,p}(t)$ (see [Component-based Piece-Wise Exponential Subsidies](https://hackmd.io/zu1jRV27SBy_HjPp_vKpYg?view)) require the following parameters:

|Parameter|Description|Domain|Current component value|Unit|Considered for Parameter Sweep?|
|---|---|---|---|---|---|
|$\alpha_1$|The maximum subsidy per block to be disbursed during the initial period|[0,1M]|0.1|SSC/block|Yes|
|$\tau_{0, 1}$|The beginning of the constant disbursal period|[0,$\infty$]|As soon as rewards are activated|Blocks|Yes|
|$\tau_{1, 1}$|The beginning of the exponential disbursal period|[$\tau_{0, i}, \infty$]|$\tau_{0, 1}$|Blocks|*n/a*|
|$\Omega_1$|The maximum subsidy that can be disbursed through the component lifetime|[0,$\Omega_I$]|100M|SSC|Yes|
|$\alpha_2$|The maximum subsidy per block to be disbursed during the initial period|[0,1M]|0.1|SSC/block|Yes|
|$\tau_{0, 2}$|The beginning of the constant disbursal period|[0,$\infty$]|As soon as rewards are activated|Blocks|Yes|
|$\tau_{1, 2}$|The beginning of the exponential disbursal period|[$\tau_{0, 2}, \infty$]|$\tau_{0, 2}$+2yr|Blocks|Yes|
|$\Omega_2$|The maximum subsidy that can be disbursed through the component lifetime|[0,$\Omega_I$]|100M|SSC|Yes|

* Additional **System Parameters**:

|Parameter|Description|Domain|Current value|Unit|Considered for Parameter Sweep?|
|---|---|---|---|---|---|
|$\Omega$|Total SSC supply|[1B,3B]|1B|SSC|No|
||Percentage of compute fees to farmers|[0,50]|0|%|No|
||Percentage of compute fees to operators independently of the pool composition (Operator Tax)|[0,100]||%|No|
||Percentage of slash to burn|[0,100]|0|%|No|
||Percentage of slash to the foundation|[0,100]|100|%|No|
||Percentage of slash to farmers|[0,100]|0|%|No|
|$\omega$|Compute Fee Weight To Fee|||ComputePicosecond Per Shannon|Yes|


## Other resources
