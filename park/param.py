import argparse

parser = argparse.ArgumentParser(description='parameters')

# -- Basic --
parser.add_argument('--seed', type=int, default=42,
                    help='random seed (default: 42)')
parser.add_argument('--eps', type=float, default=1e-6,
                    help='epsilon (default: 1e-6)')
parser.add_argument('--logging_level', type=str, default='info',
                    help='logging level (default: info)')
parser.add_argument('--log_to', type=str, default='print',
                    help='logging destination, "print" or a filepath (default: print)')

# -- Load balance --
parser.add_argument('--num_servers', type=int, default=10,
                    help='number of servers (default: 10)')
parser.add_argument('--num_stream_jobs', type=int, default=1000,
                    help='number of streaming jobs (default: 1000)')
parser.add_argument('--service_rates', type=float,
                    default=[0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95, 1.05],
                    nargs='+', help='workers service rates '
                    '(default: [0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95, 1.05])')
parser.add_argument('--job_interval', type=int, default=55,
                    help='job arrival interval (default: 55)')
parser.add_argument('--job_size_pareto_shape', type=float, default=1.5,
                    help='pareto job size distribution shape (default: 1.5)')
parser.add_argument('--job_size_pareto_scale', type=float, default=100.0,
                    help='pareto job size distribution scale (default: 100.0)')
parser.add_argument('--load_balance_obs_high', type=float, default=50000.0,
                    help='observation cap for load balance env (default: 5000.0)')

# -- AQM --
parser.add_argument('--aqm_link_delay', type=int, default=10,
                    help='mahimahi link delay in millisecond (default: 10)')
parser.add_argument('--aqm_step_num', type=int, default=300,
                    help='total number of steps (default: 300)')
parser.add_argument('--aqm_step_interval', type=int, default=100,
                    help='time interval of each step in millisecond (default: 100)')
parser.add_argument('--aqm_uplink_trace', type=str, default="park/envs/aqm/mahimahi/trace10",
                    help='mahimahi uplink trace file')
parser.add_argument('--aqm_downlink_trace', type=str, default="park/envs/aqm/mahimahi/trace10",
                    help='mahimahi downlink trace file')

# -- Spark --
parser.add_argument('--exec_cap', type=int, default=50,
                    help='Number of total executors (default: 50)')
parser.add_argument('--num_init_dags', type=int, default=20,
                    help='Number of initial DAGs in system (default: 20)')
parser.add_argument('--num_stream_dags', type=int, default=100,
                    help='number of streaming DAGs (default: 100)')
parser.add_argument('--stream_interval', type=int, default=25000,
                    help='inter job arrival time in milliseconds (default: 25000)')
parser.add_argument('--moving_delay', type=int, default=2000,
                    help='Moving delay (milliseconds) (default: 2000)')
parser.add_argument('--warmup_delay', type=int, default=1000,
                    help='Executor warming up delay (milliseconds) (default: 1000)')

# -- Query Optimizer --
parser.add_argument('--qopt_port', type=int, default=2654,
                    help="port for communicaton with calcite backend")
## TODO: describe these better
parser.add_argument('--qopt_query', type=int, default=0,
                    help="query to run")
parser.add_argument('--qopt_train', type=int, default=1,
                    help="0 or 1, to run in training mode or test mode")
parser.add_argument('--qopt_only_final_reward', type=int,default=0, help="0 or 1")
parser.add_argument('--qopt_lopt', type=int,default=0, help="0 or 1")
parser.add_argument('--qopt_exh', type=int,default=0, help="0 or 1")
parser.add_argument('--qopt_verbose', type=int,default=0, help="0 or 1")
parser.add_argument('--qopt_left_deep', type=int,default=0, help="0 or 1")
parser.add_argument('--qopt_execute_on_db', type=int,default=0, help="0 or 1")

parser.add_argument('--qopt_reward_normalization', type=str, required=False,
                            default='min_max', help='type of reward normalization')
parser.add_argument('--qopt_cost_model', type=str, required=False,
                            default='rowCount', help='')
parser.add_argument('--qopt_dataset', type=str, required=False,
                            default='JOB', help='')

config = parser.parse_args()
