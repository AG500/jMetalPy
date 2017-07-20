import logging
import threading
import time
from typing import TypeVar, Generic, List

from jmetal.core.solution import FloatSolution

from jmetal.util.time import get_time_of_execution

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

S = TypeVar('S')
R = TypeVar('R')


class Algorithm(Generic[S, R], threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.observable = None
        self.evaluations: int = 0
        self.start_computing_time: int = 0
        self.total_computing_time: int = 0

    def get_name(self) -> str:
        pass

    def get_evaluations(self) -> int:
        return self.evaluations

    def get_current_computing_time(self) -> float:
        return time.time() - self.start_computing_time


class EvolutionaryAlgorithm(Algorithm[S, R]):
    def __init__(self):
        super(EvolutionaryAlgorithm,self).__init__()
        self.population = []

    def create_initial_population(self) -> List[S]:
        pass

    def evaluate_population(self, population: List[S]) -> List[S]:
        pass

    def init_progress(self) -> None:
        pass

    def is_stopping_condition_reached(self) -> bool:
        pass

    def selection(self, population: List[S]) -> List[S]:
        pass

    def reproduction(self, population: List[S]) -> List[S]:
        pass

    def replacement(self, population: List[S], offspring_population: List[S]) -> List[S]:
        pass

    def update_progress(self):
        pass

    def get_result(self) -> R:
        pass

    @get_time_of_execution
    def run(self):
        """
        Step One: Generate the initial population of individuals randomly. (First generation)
        Step Two: Evaluate the fitness of each individual in that population (time limit, sufficient fitness achieved, etc.)
        Step Three: Repeat the following regenerational steps until termination:
            1. Select the best-fit individuals for reproduction. (Parents)
            2. Breed new individuals through crossover and mutation operations to give birth to offspring.
            3. Evaluate the individual fitness of new individuals.
            4. Replace least-fit population with new individuals.
        """

        self.start_computing_time = time.time()

        self.population = self.create_initial_population() # Step One
        self.population = self.evaluate_population(self.population) # Step Two
        self.init_progress()

        while not self.is_stopping_condition_reached(): # Step Three
            mating_population = self.selection(self.population) # Step Three.1
            offspring_population = self.reproduction(mating_population) # Step Three.2
            offspring_population = self.evaluate_population(offspring_population) # Step Three.3
            self.population = self.replacement(self.population, offspring_population) # Step Three.4
            self.update_progress()

        self.total_computing_time = self.get_current_computing_time()


class ParticleSwarmOptimization(Algorithm[FloatSolution, R]):
    def __init__(self):
        super(ParticleSwarmOptimization, self).__init__()
        self.swarm = []

    def init_progress(self) -> None :
        pass

    def update_progress(self) -> None :
        pass

    def is_stopping_condition_reached(self) -> bool:
        pass

    def evaluate_swarm(self, swarm: List[S]) -> List[S]:
        pass

    def initialize_global_best(self, swarm: List[S]) -> None:
        pass

    def initialize_particle_best(self, swarm: List[S]) -> None:
        pass

    def initialize_velocity(self, swarm: List[S]) -> None:
        pass

    def update_velocity(self, swarm: List[S]) -> None:
        pass

    def update_position(self, swarm: List[S]) -> None:
        pass

    def perturbation(self, swarm: List[S]) -> None:
        pass

    def update_global_best(self, swarm: List[S]) -> None:
        pass

    def update_particle_best(self, swarm: List[S]) -> None:
        pass

    def get_result(self) -> R:
        pass

    def run(self):
        """
        """
        self.start_computing_time = time.time()

        self.swarm = self.create_initial_swarm()
        self.swarm = self.evaluate_swarm(self.population)
        self.initialize_velocity(self.swarm)
        self.initialize_particle_best(self.swarm)
        self.initialize_global_best(self.swarm)
        self.init_progress()

        while not self.is_stopping_condition_reached():
            self.update_velocity(self.swarm)
            self.update_position(self.swarm)
            self.perturbation(self.swarm)
            self.swarm = self.evaluate_swarm(self.swarm)
            self.update_global_best(self.swarm)
            self.update_particle_best(self.swarm)
            self.update_progress()

        self.total_computing_time = self.get_current_computing_time()
