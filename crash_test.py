
import time
import sdnotify
import argparse, yaml

"""
should run and restart on fail/stall from /etc/systemd/system/crash_test.service config, with --config some_name_from_local_yaml_config
default working path = directory of this file itself, set in systemd service config
"""

def get_config():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()

    with open("collector_config.yaml") as f:
        config = yaml.safe_load(f)

    return config["collectors"][args.config]

# use: config['mongo_uri'], config['redis_uri'], config['log_file'] ...
config = get_config()
#print(f"config data: {config.test_param1}")



sd_notify = sdnotify.SystemdNotifier()

def Test_ErrorCrash():
    for i in range(1,60):
        print(f'{i} working', flush=True)
        sd_notify.notify("WATCHDOG=1")
        if i == 25:
            time.sleep(35) # test stalling reloads (no sd notify calls)
            #raise ValueError(f'{i} random unhandled error!') # test crashing reloads
        time.sleep(1)

Test_ErrorCrash()

