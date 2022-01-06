import time

import hydra


def preprocess_step(kernel_name):
    print(f"Preprocessing using {kernel_name=}")

    return f"Preprocessed {kernel_name}"


def train_step(data, model_name, epochs, batch_size):
    print(f"Training using {data=}, {model_name=}, {epochs=}, {batch_size=}")
    time.sleep(15)


@hydra.main(config_path=".", config_name="configuration")
def run_experiment(config):
    print(f"Start running experiment {config.project_name}")
    data = preprocess_step(**config.preprocess)
    train_step(data=data, **config.train)
    print("Experiment finished successfully.")


if __name__ == "__main__":
    run_experiment()
