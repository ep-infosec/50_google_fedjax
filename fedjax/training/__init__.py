# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""FedJAX training utilities."""

from fedjax.training import structured_flags

from fedjax.training.checkpoint import load_latest_checkpoint
from fedjax.training.checkpoint import save_checkpoint

from fedjax.training.federated_experiment import EvaluationFn
from fedjax.training.federated_experiment import FederatedExperimentConfig
from fedjax.training.federated_experiment import ModelFullEvaluationFn
from fedjax.training.federated_experiment import ModelSampleClientsEvaluationFn
from fedjax.training.federated_experiment import ModelTrainClientsEvaluationFn
from fedjax.training.federated_experiment import run_federated_experiment
from fedjax.training.federated_experiment import set_tf_cpu_only
from fedjax.training.federated_experiment import TrainClientsEvaluationFn

from fedjax.training.logging import Logger

from fedjax.training.tasks import ALL_TASKS
from fedjax.training.tasks import get_task
