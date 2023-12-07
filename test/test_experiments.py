from subspace_model.experiments.experiment import (
    fund_inclusion,
    issuance_sweep,
    sanity_check_run,
    standard_stochastic_run,
)


def test_sanity_check_run():
    sim_df = sanity_check_run(SIMULATION_DAYS=700, TIMESTEP_IN_DAYS=1, SAMPLES=1)


def test_standard_stochastic_run():
    sim_df = standard_stochastic_run(SIMULATION_DAYS=700, TIMESTEP_IN_DAYS=1, SAMPLES=2)


def test_issuance_sweep():
    sim_df = issuance_sweep(SIMULATION_DAYS=700, TIMESTEP_IN_DAYS=1, SAMPLES=2)


def test_fund_inclusion():
    sim_df = fund_inclusion(SIMULATION_DAYS=700, TIMESTEP_IN_DAYS=1, SAMPLES=2)
