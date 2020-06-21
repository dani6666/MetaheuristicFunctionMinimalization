import copy
import random
import time

from Particle import Particle


class ParticleSwarm:
    number_of_particles = 20
    breaking_factor = 0.9
    local_approach_factor = 0.3
    swarm_approach_factor = 0.3

    @staticmethod
    def minimalize_function(f, x, time_to_run):
        deadline = time.time() + time_to_run
        ParticleSwarm.number_of_particles *= time_to_run

        particles = []
        for i in range(ParticleSwarm.number_of_particles):
            particles.append(Particle(x))

        swarm_best_position = copy.deepcopy(particles[0].best_position)
        swarm_best_value = f(*ParticleSwarm.to_function_args(swarm_best_position))
        for particle in particles[1:]:
            particle.best_value = f(*ParticleSwarm.to_function_args(particle.best_position))
            if particle.best_value < swarm_best_value:
                swarm_best_position = copy.deepcopy(particle.best_position)
                swarm_best_value = particle.best_value

        while time.time() < deadline:
            for particle in particles:
                for i in range(4):
                    particle.velocity[i] = particle.velocity[i] * ParticleSwarm.breaking_factor + \
                                           ParticleSwarm.local_approach_factor * random.random() * \
                                           (particle.best_position[i] - particle.position[i]) + \
                                           ParticleSwarm.swarm_approach_factor * random.random() * \
                                           (swarm_best_position[i] - particle.position[i])
                    particle.position[i] = particle.position[i] + particle.velocity[i]
                try:
                    particle_value = f(*ParticleSwarm.to_function_args(particle.position))
                except OverflowError:
                    continue

                if particle.best_value > particle_value:
                    particle.best_value = particle_value
                    particle.best_position = copy.deepcopy(particle.position)
                    if particle_value < swarm_best_value:
                        swarm_best_value = particle_value
                        swarm_best_position = copy.deepcopy(particle.position)

        return swarm_best_position, swarm_best_value

    @staticmethod
    def to_function_args(position):
        return position[0], position[1], position[2], position[3]
