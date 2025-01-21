class CarWash:
    def __init__(self, workers, n_cars):
        self.workers = workers
        self.n_cars = n_cars
    
    def current_throughput(self):
        # Calculate the total time per worker
        worker_sum = sum(worker.total for worker in self.workers)  
        average = worker_sum / len(self.workers)  
        # Current throughput calculation: throughput = (60 / average time) * number of workers
        throughput = (60 / average) * len(self.workers)  
        return throughput
    
    def optimized_throughput(self):
        # Sort workers by vacuuming time (the key to optimizing vacuuming task)
        sorted_workers = sorted(self.workers, key=lambda w: w.vacuuming_time)
        
        # Split the workers into two halves: vacuumers (who do vacuuming) and others (who do the rest)
        vacuumers = sorted_workers[:len(self.workers)//2]
        others = sorted_workers[len(self.workers)//2:]

        # Calculate average times for both groups
        average_vacuuming = sum(i.vacuuming_time for i in vacuumers) / len(vacuumers)
        average_others = sum(i.wiping_time + i.pressure_time for i in others) / len(others)

        # Optimized throughput calculation: throughput = (60 / max of the two groups) * number of vacuumers
        throughput = (60 / max(average_others, average_vacuuming)) * len(vacuumers)
        return throughput
    
    def optimization_potential(self):
        current = self.current_throughput()
        optimized = self.optimized_throughput()
        # Calculate optimization potential as the percentage increase in throughput
        potential = (optimized - current) / current
        return potential   


class Worker:
    def __init__(self, vacuuming_time, wiping_time, pressure_time):
        self.vacuuming_time = vacuuming_time
        self.wiping_time = wiping_time
        self.pressure_time = pressure_time
        self.total = self.vacuuming_time + self.pressure_time + self.wiping_time


# Example dataset of workers
workers = [
    Worker(10, 4 ,2), 
    Worker(6, 4, 2),  
    Worker(8, 4 , 4), 
    Worker(12, 5, 3), 

]

# Initialize car wash
carwash = CarWash(workers, n_cars=50)

# Calculate throughput and optimization potential
print("Current Throughput:", carwash.current_throughput())
print("Optimized Throughput:", carwash.optimized_throughput())
print("Optimization Potential:", carwash.optimization_potential())

